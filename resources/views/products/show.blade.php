<!-- Product Show View -->

@extends('layouts.app')

@section('content')
    <div class="container-fluid">
        <div class="row">
            <div class="col-md-12">
                <h1>{{ $product->name }}</h1>
            </div>
        </div>

        <div class="row">
            <div class="col-md-6">
                <img src="{{ $product->image }}" alt="{{ $product->name }}" class="img-fluid">
            </div>

            <div class="col-md-6">
                <h2>Product Details</h2>
                <p>{{ $product->description }}</p>
                <p>Price: {{ $product->price }}</p>
                <p>Rating: {{ $product->rating }}/5</p>
            </div>
        </div>

        <div class="row">
            <div class="col-md-12">
                <h2>Product Variations</h2>
                <table class="table table-striped">
                    <thead>
                        <tr>
                            <th>Variation ID</th>
                            <th>Name</th>
                            <th>Price</th>
                            <th>Stock</th>
                        </tr>
                    </thead>
                    <tbody>
                        @foreach($product->variations as $variation)
                            <tr>
                                <td>{{ $variation->id }}</td>
                                <td>{{ $variation->name }}</td>
                                <td>{{ $variation->price }}</td>
                                <td>{{ $variation->stock }}</td>
                            </tr>
                        @endforeach
                    </tbody>
                </table>
            </div>
        </div>

        <div class="row">
            <div class="col-md-12">
                <h2>Product Reviews</h2>
                <table class="table table-striped">
                    <thead>
                        <tr>
                            <th>Review ID</th>
                            <th>Customer Name</th>
                            <th>Rating</th>
                            <th>Review</th>
                        </tr>
                    </thead>
                    <tbody>
                        @foreach($product->reviews as $review)
                            <tr>
                                <td>{{ $review->id }}</td>
                                <td>{{ $review->customer->name }}</td>
                                <td>{{ $review->rating }}/5</td>
                                <td>{{ $review->review }}</td>
                            </tr>
                        @endforeach
                    </tbody>
                </table>
            </div>
        </div>
    </div>
@endsection
