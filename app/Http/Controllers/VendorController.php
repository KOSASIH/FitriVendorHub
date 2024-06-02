<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Vendors;
use App\Models\Products;
use App\Models\Orders;
use App\Models\Ratings;
use App\Services\VendorsService;
use App\Transformers\VendorsTransformer;
use App\Transformers\ProductsTransformer;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\Storage;
use Illuminate\Support\Facades\Redis;
use Illuminate\Support\Str;

class VendorController extends Controller
{
    private $vendorsService;
    private $vendorsTransformer;
    private $productsTransformer;

    public function __construct(VendorsService $vendorsService, VendorsTransformer $vendorsTransformer, ProductsTransformer $productsTransformer)
    {
        $this->vendorsService = $vendorsService;
        $this->vendorsTransformer = $vendorsTransformer;
        $this->productsTransformer = $productsTransformer;
    }

    /**
     * Display the vendor dashboard.
     *
     * @return \Illuminate\Http\Response
     */
    public function index(Request $request)
    {
        $vendor = Auth::user()->vendor;
        $orders = $vendor->orders()->where('status', '!=', 'cancelled')->latest()->take(5)->get();
        $products = $vendor->products()->where('status', 'active')->latest()->take(5)->get();
        $ratings = $vendor->ratings()->latest()->take(5)->get();

        $data = [
            'orders' => $orders,
            'products' => $products,
            'ratings' => $ratings,
            'endor' => $vendor,
        ];

        return view('vendor.dashboard', $data);
    }

    /**
     * Display a list of products for a vendor.
     *
     * @return \Illuminate\Http\Response
     */
    public function products(Request $request)
    {
        $vendor = Auth::user()->vendor;
        $products = $vendor->products()->where('status', 'active')->paginate(10);

        $data = [
            'products' => $products,
            'endor' => $vendor,
        ];

        return view('vendor.products', $data);
    }

    /**
     * Display a product details page.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function productDetails(Request $request, $id)
    {
        $product = Products::find($id);
        $vendor = $product->vendor;
        $relatedProducts = $product->relatedProducts()->take(4)->get();

        $data = [
            'product' => $product,
            'endor' => $vendor,
            'elatedProducts' => $relatedProducts,
        ];

        return view('vendor.product-details', $data);
    }

    /**
     * Update a product.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function updateProduct(Request $request, $id)
    {
        $product = Products::find($id);
        $vendor = $product->vendor;

        $this->validate($request, [
            'name' => 'equired|string|max:255',
            'description' => 'equired|string',
            'price' => 'equired|numeric',
            'tock' => 'equired|numeric',
        ]);

        $product->update([
            'name' => $request->input('name'),
            'description' => $request->input('description'),
            'price' => $request->input('price'),
            'tock' => $request->input('stock'),
        ]);

        return redirect()->route('vendor.products')->with('success', 'Product updated successfully!');
    }

    /**
     * Delete a product.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function deleteProduct(Request $request, $id)
    {
        $product = Products::find($id);
        $vendor = $product->vendor;

        $product->delete();

        return redirect()->route('vendor.products')->with('success', 'Product deleted successfully!');
    }

    /**
     * Display a list of orders for a vendor.
     *
     * @return \Illuminate\Http\Response
     */
    public function orders(Request $request)
    {
        $vendor = Auth::user()->vendor;
        $orders = $vendor->orders()->where('status', '!=', 'cancelled')->paginate(10);

        $data = [
            'orders' => $orders,
            'endor' => $vendor,
        ];

        return view('vendor.orders', $data);
    }

    /**
     * Display an order details page.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function orderDetails(Request $request, $id)
    {
        $order= Orders::find($id);
        $vendor = $order->vendor;
        $products = $order->products;

        $data = [
            'order' => $order,
            'endor' => $vendor,
            'roducts' => $products,
        ];

        return view('vendor.order-details', $data);
    }

    /**
     * Update an order status.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function updateOrderStatus(Request $request, $id)
    {
        $order = Orders::find($id);
        $vendor = $order->vendor;

        $this->validate($request, [
            'tatus' => 'equired|string|max:255',
        ]);

        $order->update([
            'tatus' => $request->input('status'),
        ]);

        return redirect()->route('vendor.orders')->with('success', 'Order status updated successfully!');
    }

    /**
     * Display a list of ratings for a vendor.
     *
     * @return \Illuminate\Http\Response
     */
    public function ratings(Request $request)
    {
        $vendor = Auth::user()->vendor;
        $ratings = $vendor->ratings()->latest()->paginate(10);

        $data = [
            'ratings' => $ratings,
            'endor' => $vendor,
        ];

        return view('vendor.ratings', $data);
    }

    /**
     * Display a rating details page.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function ratingDetails(Request $request, $id)
    {
        $rating = Ratings::find($id);
        $vendor = $rating->vendor;
        $product = $rating->product;

        $data = [
            'rating' => $rating,
            'endor' => $vendor,
            'roduct' => $product,
        ];

        return view('vendor.rating-details', $data);
    }
}
