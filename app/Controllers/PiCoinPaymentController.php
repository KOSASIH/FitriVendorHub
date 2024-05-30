<?php

namespace App\Controllers;

use Illuminate\Http\Request;
use App\Models\PiCoinPayment;

class PiCoinPaymentController extends Controller
{
    public function initiatePayment(Request $request)
    {
        // Generate a new Pi Coin payment address
        $piCoinAddress = 'your_pi_coin_address';

        // Create a new Pi Coin payment record
        $piCoinPayment = PiCoinPayment::create([
            'user_id' => auth()->user()->id,
            'order_id' => $request->input('order_id'),
            'pi_coin_address' => $piCoinAddress,
            'pi_coin_amount' => $request->input('amount'),
        ]);

        // Redirect to Pi Coin payment page
        return redirect()->route('pi_coin.payment', ['pi_coin_address' => $piCoinAddress]);
    }

    public function callback(Request $request)
    {
        // Verify the payment status with Pi Network API
        $apiResponse = json_decode($this->callPiCoinApi('getPaymentStatus', [
            'payment_id' => $request->input('payment_id'),
        ]), true);

        if ($apiResponse['status'] === 'uccess') {
            // Update the payment status in the database
            $piCoinPayment = PiCoinPayment::find($request->input('payment_id'));
            $piCoinPayment->payment_status = 'paid';
            $piCoinPayment->save();

            // Redirect to success page
            return redirect()->route('pi_coin.success');
        } else {
            // Redirect to failure page
            return redirect()->route('pi_coin.failure');
        }
    }

    private function callPiCoinApi($method, $params)
    {
        $apiUrl = config('pi_coin.api_url'). $method;
        $headers = [
            'Authorization' => 'Bearer '. config('pi_coin.api_key'),
            'Content-Type' => 'application/json',
        ];
        $response = json_decode(Http::withHeaders($headers)->post($apiUrl, $params), true);

        return $response;
    }
}
