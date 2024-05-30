<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class PiCoinPayment extends Model
{
    protected $fillable = [
        'user_id',
        'order_id',
        'pi_coin_address',
        'pi_coin_amount',
        'payment_status',
    ];
}
