Route::get('pi-coin/payment/{pi_coin_address}', 'PiCoinPaymentController@initiatePayment')->name('pi_coin.payment');
Route::post('pi-coin/callback', 'PiCoinPaymentController@callback')->name('pi_coin.callback');
Route::get('pi-coin/success', function () {
    return 'Payment successful!';
})->name('pi_coin.success');
Route::get('pi-coin/failure', function () {
    return 'Payment failed!';
})->name('pi_coin.failure');
