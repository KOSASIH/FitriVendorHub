<?php

namespace App\Http\Controllers\Admin;

use Illuminate\Http\Request;
use App\Http\Controllers\Controller;
use App\Models\Vendor;
use App\Models\VendorVerification;
use App\Repositories\VendorRepository;
use App\Services\VendorService;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\Gate;
use Illuminate\Support\Facades\Hash;
use Illuminate\Support\Facades\Storage;
use Illuminate\Support\Facades\Validator;

class VendorController extends Controller
{
    private $vendorRepository;
    private $vendorService;

    public function __construct(VendorRepository $vendorRepository, VendorService $vendorService)
    {
        $this->vendorRepository = $vendorRepository;
        $this->vendorService = $vendorService;
    }

    public function index()
    {
        Gate::authorize('view-vendors');
        $vendors = $this->vendorRepository->getAllVendors();
        return view('admin.vendor.index', compact('vendors'));
    }

    public function create()
    {
        Gate::authorize('create-vendors');
        return view('admin.vendor.create');
    }

    public function store(Request $request)
    {
        Gate::authorize('create-vendors');
        $validator = Validator::make($request->all(), [
            'name' => 'required|string|max:255',
            'email' => 'required|string|email|max:255|unique:vendors',
            'password' => 'required|string|min:8|confirmed',
            'password_confirmation' => 'required|string|min:8',
            'phone' => 'required|string|max:20',
            'address' => 'required|string|max:255',
            'document_type' => 'required|string|max:255',
            'document_number' => 'required|string|max:255',
            'expiration_date' => 'required|date',
        ]);

        if ($validator->fails()) {
            return redirect()->back()->withErrors($validator)->withInput();
        }

        $vendor = $this->vendorService->createVendor($request->all());
        return redirect()->route('admin.vendors.index')->with('success', 'Vendor created successfully');
    }

    public function show(Vendor $vendor)
    {
        Gate::authorize('view-vendors');
        return view('admin.vendor.show', compact('vendor'));
    }

    public function edit(Vendor $vendor)
    {
        Gate::authorize('edit-vendors');
        return view('admin.vendor.edit', compact('vendor'));
    }

    public function update(Request $request, Vendor $vendor)
    {
        Gate::authorize('edit-vendors');
        $validator = Validator::make($request->all(), [
            'name' => 'required|string|max:255',
            'email' => 'required|string|email|max:255|unique:vendors,email,'.$vendor->id,
            'phone' => 'required|string|max:20',
            'address' => 'required|string|max:255',
            'document_type' => 'required|string|max:255',
            'document_number' => 'required|string|max:255',
            'expiration_date' => 'required|date',
        ]);

        if ($validator->fails()) {
            return redirect()->back()->withErrors($validator)->withInput();
        }

        $this->vendorService->updateVendor($vendor, $request->all());
        return redirect()->route('admin.vendors.index')->with('success', 'Vendor updated successfully');
    }

    public function destroy(Vendor $vendor)
    {
        Gate::authorize('delete-vendors');
        $this->vendorService->deleteVendor($vendor);
        return redirect()->route('admin.vendors.index')->with('success', 'Vendor deleted successfully');
    }

    public function verify(Vendor $vendor)
    {
        Gate::authorize('verify-vendors');
        $this->vendorService->verifyVendor($vendor);
        return redirect()->route('admin.vendors.index')->with('success', 'Vendor verified successfully');
    }

    public function uploadDocument(Request $request, Vendor $vendor)
    {
        Gate::authorize('edit-vendors');
        $validator = Validator::make($request->all(), [
            'document' => 'required|file|max:2048',
        ]);

        if ($validator->fails()) {
            return redirect()->back()->withErrors($validator)->withInput();
        }

        $document = $request->file('document');
        $extension = $document->getClientOriginalExtension();
        $filename = $vendor->id.'-verification.'.$extension;
        Storage::putFileAs('public/vendor/verification', $document, $filename);

        $verification = $vendor->verification;
        $verification->document_number = $request->document_number;
        $verification->expiration_date = $request->expiration_date;
        $verification->document_path = '/storage/vendor/verification/'.$filename;
        $verification->save();

        return redirect()->back()->with('success', 'Verification document uploaded successfully');
    }
}
