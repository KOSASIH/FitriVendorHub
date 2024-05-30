<?php

use App\Http\Controllers\PaymentController;
use Illuminate\Support\Facades\Auth;

require_once __DIR__. '/vendor/autoload.php';

$paymentController = new PaymentController();

if (Auth::check()) {
    $user_id = Auth::id();
    $payment_method = $paymentController->getPaymentMethod($user_id);

    if ($payment_method) {
        $pi_coin_address = $payment_method->pi_coin_address;
    } else {
        $pi_coin_address = null;
    }
} else {
    $pi_coin_address = null;
}

if (isset($_POST['pi_coin_address'])) {
    $pi_coin_address = $_POST['pi_coin_address'];
    $paymentController->createPaymentMethod($user_id, $pi_coin_address);
}

?>

<!DOCTYPE html>
<html>
<head>
    <title>Pi Coin Payment Method</title>
</head>
<body>
    <h1>Pi Coin Payment Method</h1>
    <form method="post">
        <label for="pi_coin_address">Pi Coin Address:</label>
        <input type="text" id="pi_coin_address" name="pi_coin_address" value="<?php echo $pi_coin_address;?>">
        <button type="submit">Save</button>
    </form>

    <?php if ($pi_coin_address):?>
        <p>Your Pi Coin address is: <?php echo $pi_coin_address;?></p>
    <?php endif;?>
</body>
</html>
