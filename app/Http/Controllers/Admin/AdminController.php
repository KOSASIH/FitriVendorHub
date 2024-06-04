<?php

namespace App\Http\Controllers\Admin;

use Illuminate\Http\Request;
use App\Http\Controllers\Controller;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\Gate;
use Illuminate\Support\Facades\Lang;
use Illuminate\Support\Facades\Validator;
use Illuminate\Support\Str;
use Illuminate\Pagination\LengthAwarePaginator;
use Illuminate\Database\Eloquent\Builder;
use App\Models\Admin;
use App\Models\Vendors;
use App\Models\Orders;
use App\Models\Products;
use App\Enums\OrderStatus;
use App\Enums\ProductStatus;
use App\Enums\VendorsStatus;
use App\Jobs\SendVendorNotification;
use App\Jobs\UpdateOrderStatus;
use App\Listeners\VendorsEventListener;
use App\Observers\VendorsObserver;
use App\Repositories\VendorsRepository;
use App\Services\VendorsService;
use App\Transformers\VendorsTransformer;
use Carbon\Carbon;
use Illuminate\Support\Facades\Event;
use Illuminate\Support\Facades\Redis;
use Laravel\Telescope\Telescope;

class AdminController extends Controller
{
    private $vendorsRepository;
    private $vendorsService;

    public function __construct(VendorsRepository $vendorsRepository, VendorsService $vendorsService)
    {
        $this->vendorsRepository = $vendorsRepository;
        $this->vendorsService = $vendorsService;
    }

    public function index(Request $request)
    {
        // Advanced filtering and sorting using Laravel's query builder
        $vendors = $this->vendorsRepository->getAllVendors(
            $request->input('search'),
            $request->input('status'),
            $request->input('sort_by'),
            $request->input('sort_order')
        );

        // Paginate results using LengthAwarePaginator
        $vendors = new LengthAwarePaginator($vendors, $vendors->count(), 10);

        // Use a custom transformer to format the data
        $vendors = fractal($vendors, new VendorsTransformer());

        return view('admin.vendors.index', compact('vendors'));
    }

    public function create(Request $request)
    {
        // Use a custom request class to validate input
        $request->validate(VendorCreateRequest::rules());

        // Use a service class to handle business logic
        $vendor = $this->vendorsService->createVendor($request->all());

        // Dispatch a job to send a notification to the vendor
        SendVendorNotification::dispatch($vendor);

        return redirect()->route('admin.vendors.index')->with('success', 'Vendor created successfully!');
    }

    public function update(Request $request, $id)
    {
        // Use a custom request class to validate input
        $request->validate(VendorUpdateRequest::rules());

        // Use a service class to handle business logic
        $vendor = $this->vendorsService->updateVendor($id, $request->all());

        // Dispatch a job to update the order status
        UpdateOrderStatus::dispatch($vendor);

        return redirect()->route('admin.vendors.index')->with('success', 'Vendor updated successfully!');
    }

    public function destroy($id)
    {
        // Use a custom request class to validate input
        $request->validate(VendorDeleteRequest::rules());

        // Use a service class to handle business logic
        $this->vendorsService->deleteVendor($id);

        return redirect()->route('admin.vendors.index')->with('success', 'Vendor deleted successfully!');
    }

    public function getVendorOrders($id)
    {
        // Use a custom repository class to retrieve data
        $orders = $this->vendorsRepository->getVendorOrders($id);

        // Use a custom transformer to format the data
        $orders = fractal($orders, new OrdersTransformer());

        return response()->json($orders);
    }

    public function updateVendorStatus(Request $request, $id)
    {
        // Use a custom request class to validate input
        $request->validate(VendorStatusUpdateRequest::rules());

        // Use a service class to handle business logic
        $this->vendorsService->updateVendorStatus($id, $request->input('status'));

        returnredirect()->back()->with('success', 'Vendor status updated successfully!');
    }
}
