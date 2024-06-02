<!-- Order Show View -->

@extends('layouts.app')

@section('content')
    <div class="container-fluid">
        <div class="row">
            <div class="col-md-12">
                <h1>Order {{ $order->id }}</h1>
            </div>
        </div>

        <div class="row">
            <div class="col-md-6">
                <h2>Order Details</h2>
                <p>Customer Name: {{ $order->customer->name }}</p>
                <p>Order Date: {{ $order->created_at }}</p>
                <p>Total: {{ $order->total }}</p>
                <p>Status: {{ $order->status->name }}</p>
            </div>

            <div class="col-md-6">
                <h2>Order Items</h2>
                <table class="table table-striped">
                    <thead>
                        <tr>
                            <th>Item ID</th>
                            <th>Product Name</th>
                            <th>Quantity</th>
                            <th>Price</th>
                        </tr>
                    </thead>
                    <tbody>
                        @foreach($order->items as $item)
                            <tr>
                                <td>{{ $item->id }}</td>
                                <td>{{ $item->product->name }}</td>
                                <td>{{ $item->quantity }}</td>
                                <td>{{ $item->price }}</td>
                            </tr>
                        @endforeach
                    </tbody>
                </table>
            </div>
        </div>
    </div>
@endsection
