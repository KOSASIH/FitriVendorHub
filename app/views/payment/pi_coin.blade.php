@extends('layouts.app')

@section('content')
    <h1>Pi Coin Payment</h1>
    <p>Please send {{ $piCoinAmount }} Pi Coin to {{ $piCoinAddress }}.</p>
    <p>Once the payment is confirmed, you will be redirected to the success page.</p>
@endsection
