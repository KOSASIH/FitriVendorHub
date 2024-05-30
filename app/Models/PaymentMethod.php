<?php

namespace App\Models\PaymentMethods;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Support\Facades\Http;
use Illuminate\Support\Facades\Log;
use Illuminate\Support\Str;
use Illuminate\Validation\Rule;
use Laravel\Cashier\PaymentMethod as CashierPaymentMethod;
use PiNetwork\SDK\Client as PiNetworkClient;
use Symfony\Component\HttpFoundation\Request;

abstract class PaymentMethod extends Model
{
    use CashierPaymentMethod;

    const TYPE_PI_COIN = 'pi_coin';
    const TYPE_CREDIT_CARD = 'credit_card';
    const TYPE_PAYPAL = 'paypal';

    protected $fillable = [
        'user_id',
        'type',
        'pi_coin_address',
        'credit_card_number',
        'credit_card_expiration',
        'paypal_email',
        'payment_token',
    ];

    protected $casts = [
        'payment_token' => 'encrypted',
    ];

    protected $hidden = [
        'credit_card_number',
        'credit_card_expiration',
        'paypal_email',
    ];

    public function user()
    {
        return $this->belongsTo(User::class);
    }

    public function payments()
    {
        return $this->hasMany(Payment::class);
    }

    public function getPaymentMethodTypeAttribute()
    {
        return Str::studly($this->type);
    }

    public function getPaymentMethodLabelAttribute()
    {
        return ucfirst($this->type);
    }

    public function getPaymentMethodIconAttribute()
    {
        return match ($this->type) {
            self::TYPE_PI_COIN => 'fab fa-pi',
            self::TYPE_CREDIT_CARD => 'fas fa-credit-card',
            self::TYPE_PAYPAL => 'fab fa-paypal',
            default => 'fas fa-question',
        };
    }

    public function getPaymentMethodDescriptionAttribute()
    {
        return match ($this->type) {
            self::TYPE_PI_COIN => 'Pay with Pi Coin, the decentralized cryptocurrency.',
            self::TYPE_CREDIT_CARD => 'Pay with your credit card, securely and conveniently.',
            self::TYPE_PAYPAL => 'Pay with PayPal, the trusted online payment service.',
            default => 'Unknown payment method.',
        };
    }

    public function validatePaymentMethod(Request $request)
    {
        $rules = [
            'type' => ['required', Rule::in([self::TYPE_PI_COIN, self::TYPE_CREDIT_CARD, self::TYPE_PAYPAL])],
        ];

        switch ($this->type) {
            case self::TYPE_PI_COIN:
                $rules['pi_coin_address'] = ['required', 'tring', 'ax:255'];
                break;
            case self::TYPE_CREDIT_CARD:
                $rules['credit_card_number'] = ['required', 'tring', 'ax:255'];
                $rules['credit_card_expiration'] = ['required', 'date_format:Y-m'];
                break;
            case self::TYPE_PAYPAL:
                $rules['paypal_email'] = ['required', 'email', 'ax:255'];
                break;
        }

        $request->validate($rules);
    }

    public function processPayment(Request $request)
    {
        switch ($this->type) {
            case self::TYPE_PI_COIN:
                return $this->processPiCoinPayment($request);
            case self::TYPE_CREDIT_CARD:
                return $this->processCreditCardPayment($request);
            case self::TYPE_PAYPAL:
                return $this->processPayPalPayment($request);
            default:
                throw new \Exception('Unknown payment method.');
        }
    }

    private function processPiCoinPayment(Request $request)
    {
        $piNetworkClient = new PiNetworkClient();
        $paymentResponse = $piNetworkClient->createPayment([
            'amount' => $request->input('amount'),
            'currency' => 'PI',
            'address' => $this->pi_coin_address,
        ]);

        if ($paymentResponse->successful()) {
            // Update payment status and token
            $this->payment_token = $paymentResponse->payment_token;
            $this->save();

            return redirect()->route('payment.success');
        } else {
            Log::error('Pi Coin payment failed:', [$paymentResponse->error_message]);
            return redirect()->route('payment.failure');
        }
    }

    private function processCreditCardPayment(Request $request)
    {
        // Implement credit card payment processing using a payment gateway like Stripe
    }

    private function processPayPalPayment(Request $request)
    {
        // Implement PayPal payment processing using the PayPal API
    }
}
