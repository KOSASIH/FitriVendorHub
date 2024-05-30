<?php

return [
    'api_url' => 'https://api.pi.network/v1/', // Pi Network API URL
    'api_key' => env('PI_COIN_API_KEY'), // Your Pi Coin API Key
    'api_secret' => env('PI_COIN_API_SECRET'), // Your Pi Coin API Secret
    'callback_url' => route('pi_coin.callback'), // Callback URL for Pi Coin payment
];
