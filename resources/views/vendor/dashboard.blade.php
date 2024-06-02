<!-- Vendor Dashboard View -->

@extends('layouts.app')

@section('content')
    <div class="container-fluid">
        <div class="row">
            <div class="col-md-12">
                <h1>Vendor Dashboard</h1>
            </div>
        </div>

        <div class="row">
            <div class="col-md-4">
                <div class="card">
                    <div class="card-header">Sales Performance</div>
                    <div class="card-body">
                        <h5>Total Sales: {{ $vendor->sales->sum('amount') }}</h5>
                        <h5>Average Order Value: {{ $vendor->sales->avg('amount') }}</h5>
                        <h5>Sales Growth: {{ $vendor->sales->growthRate() }}%</h5>
                    </div>
                </div>
            </div>

            <div class="col-md-4">
                <div class="card">
                    <div class="card-header">Order Performance</div>
                    <div class="card-body">
                        <h5>Total Orders: {{ $vendor->orders->count() }}</h5>
                        <h5>Average Order Fulfillment Time: {{ $vendor->orders->avg('fulfillment_time') }} days</h5>
                        <h5>Order Cancellation Rate: {{ $vendor->orders->cancellationRate() }}%</h5>
                    </div>
                </div>
            </div>

            <div class="col-md-4">
                <div class="card">
                    <div class="card-header">Product Performance</div>
                    <div class="card-body">
                        <h5>Top Selling Product: {{ $vendor->topSellingProduct->name }}</h5>
                        <h5>Product Return Rate: {{ $vendor->products->returnRate() }}%</h5>
                        <h5>Average Product Rating: {{ $vendor->products->avg('rating') }}/5</h5>
                    </div>
                </div>
            </div>
        </div>

        <div class="row">
            <div class="col-md-12">
                <h2>Recent Orders</h2>
                <table class="table table-striped">
                    <thead>
                        <tr>
                            <th>Order ID</th>
                            <th>Customer Name</th>
                            <th>Order Date</th>
                            <th>Total</th>
                            <th>Status</th>
                        </tr>
                    </thead>
                    <tbody>
                        @foreach($vendor->orders->take(10) as $order)
                            <tr>
                                <td>{{ $order->id }}</td>
                                <td>{{ $order->customer->name }}</td>
                                <td>{{ $order->created_at }}</td>
                                <td>{{ $order->total }}</td>
                                <td>{{ $order->status->name }}</td>
                            </tr>
                        @endforeach
                    </tbody>
                </table>
            </div>
        </div>
    </div>
@endsection
