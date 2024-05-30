<?php

namespace App\Http\Controllers;

use App\Models\PaymentMethods\PaymentMethod;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\Redirect;
use Illuminate\Support\Facades\Session;

class PaymentController extends Controller
{
    public function index()
    {
        $paymentMethods = PaymentMethod::where('user_id', Auth::id())->get();

        return view('payment.index', compact('paymentMethods'));
    }

    public function create(Request $request)
    {
        $paymentMethod = PaymentMethod::create([
            'user_id' => Auth::id(),
            'type' => $request->input('type'),
        ]);

        Session::flash('success', 'Payment method created successfully.');

        return Redirect::route('payment.index');
    }

    public function edit(PaymentMethod $paymentMethod)
    {
        if ($paymentMethod->user_id !== Auth::id()) {
            abort(403);
        }

        return view('payment.edit', compact('paymentMethod'));
    }

    public function update(Request $request, PaymentMethod $paymentMethod)
    {
        if ($paymentMethod->user_id !== Auth::id()) {
            abort(403);
        }

        $paymentMethod->validatePaymentMethod($request);
        $paymentMethod->fill($request->all());
        $paymentMethod->save();

        Session::flash('success', 'Payment method updated successfully.');

        return Redirect::route('payment.index');
    }

    public function destroy(PaymentMethod $paymentMethod)
    {
        if ($paymentMethod->user_id !== Auth::id()) {
            abort(403);
        }

        $paymentMethod->delete();

        Session::flash('success', 'Payment method deleted successfully.');

        return Redirect::route('payment.index');
    }

    public function process(Request $request, PaymentMethod $paymentMethod)
    {
        if ($paymentMethod->user_id !== Auth::id()) {
            abort(403);
        }

        try {
            $paymentResponse = $paymentMethod->processPayment($request);

            Session::flash('success', 'Payment processed successfully.');

            return Redirect::route('payment.index');
        } catch (\Exception $e) {
            Session::flash('error', 'Payment processing failed: ' . $e->getMessage());

            return Redirect::route('payment.index');
        }
    }
}
