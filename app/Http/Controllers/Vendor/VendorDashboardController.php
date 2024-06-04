<?php

namespace App\Http\Controllers\Vendor;

use Illuminate\Http\Request;
use App\Http\Controllers\Controller;
use App\Models\Vendor;
use App\Models\VendorVerification;
use App\Repositories\VendorRepository;
use App\Services\VendorService;
use Illuminate\Support\Facades\Auth;

class VendorDashboardController extends Controller
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
        $vendor = Auth::user()->vendor;
        return view('vendor.dashboard', compact('vendor'));
    }

    public function updateProfile(Request $request)
    {
        $vendor = Auth::user()->vendor;
        $this->vendorService->updateVendorProfile($vendor, $request->all());
        return redirect()->route('vendor.dashboard')->with('success', 'Profile updated successfully');
    }

    public function updateVerification(Request $request)
    {
        $vendor = Auth::user()->vendor;
        $this->vendorService->updateVendorVerification($vendor, $request->all());
        return redirect()->route('vendor.dashboard')->with('success', 'Verification updated successfully');
    }
}
