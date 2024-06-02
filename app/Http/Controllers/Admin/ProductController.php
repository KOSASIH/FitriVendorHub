<?php

namespace App\Http\Controllers\Admin;

use Illuminate\Http\Request;
use App\Http\Controllers\Controller;
use App\Models\Product;
use App\Services\ProductService;
use App\Repositories\ProductRepository;
use Illuminate\Support\Facades\Validator;
use Illuminate\Support\Facades\Redirect;
use Illuminate\Support\Facades\View;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\Gate;

class ProductController extends Controller
{
    /**
     * @var ProductService
     */
    private $productService;

    /**
     * @var ProductRepository
     */
    private $productRepository;

    public function __construct(ProductService $productService, ProductRepository $productRepository)
    {
        $this->productService = $productService;
        $this->productRepository = $productRepository;
    }

    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function index(Request $request)
    {
        // Check if the user has permission to view products
        if (!Gate::allows('view-products')) {
            abort(403);
        }

        // Get the products with pagination and filtering
        $products = $this->productRepository->getAll($request->all());

        // Return the view with the products
        return View::make('admin.products.index', compact('products'));
    }

    /**
     * Show the form for creating a new resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function create()
    {
        // Check if the user has permission to create products
        if (!Gate::allows('create-products')) {
            abort(403);
        }

        // Return the create form view
        return View::make('admin.products.create');
    }

    /**
     * Store a newly created resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function store(Request $request)
    {
        // Check if the user has permission to create products
        if (!Gate::allows('create-products')) {
            abort(403);
        }

        // Validate the request data
        $validator = Validator::make($request->all(), [
            'name' => 'required|string|max:255',
            'description' => 'required|string',
            'price' => 'required|numeric',
            'stock' => 'required|integer',
        ]);

        if ($validator->fails()) {
            return Redirect::back()->withErrors($validator)->withInput();
        }

        // Create a new product
        $product = $this->productService->createProduct($request->all());

        // Return a success message
        return Redirect::route('admin.products.index')->with('success', 'Product created successfully!');
    }

    /**
     * Display the specified resource.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function show($id)
    {
        // Check if the user has permission to view products
        if (!Gate::allows('view-products')) {
            abort(403);
        }

        // Get the product by ID
        $product = $this->productRepository->find($id);

        // Return the show view with the product
        return View::make('admin.products.show', compact('product'));
    }

    /**
     * Show the form for editing the specified resource.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function edit($id)
    {
        // Check if the user has permission to edit products
        if (!Gate::allows('edit-products')) {
            abort(403);
        }

        // Get the product by ID
        $product = $this->productRepository->find($id);

        // Return the edit form view with the product
        return View::make('admin.products.edit', compact('product'));
    }

    /**
     * Update the specified resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function update(Request $request, $id)
    {
        // Check if the user has permission to edit products
        if (!Gate::allows('edit-products')) {
            abort(403);
        }

        // Validate the request data
        $validator = Validator::make($request->all(), [
            'name' => 'required|string|max:255',
            'description' => 'required|string',
            'price' => 'required|numeric',
            'stock' => 'required|integer',
        ]);

        if ($validator->fails()) {
            return Redirect::back()->withErrors($validator)->withInput();
        }

        // Update the product
        $product = $this->productService->updateProduct($id, $request->all());

        // Return a success message
        return Redirect::route('admin.products.index')->with('success', 'Product updated successfully!');
    }

    /**
     * Remove the specified resource from storage.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function destroy($id)
    {
        // Check if the user has permission to delete products
        if (!Gate::allows('delete-products')) {
            abort(403);
        }

        // Delete the product
        $this->productService->deleteProduct($id);

        // Return a success message
        return Redirect::route('admin.products.index')->with('success', 'Product deleted successfully!');
    }
}
