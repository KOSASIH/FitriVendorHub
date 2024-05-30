// tests/PaymentMethodTest.php
<?php

use PHPUnit\Framework\TestCase;
use App\Models\PaymentMethod;

class PaymentMethodTest extends TestCase
{
    public function testCreatePaymentMethod()
    {
        $payment_method = new PaymentMethod();
        $payment_method->pi_coin_address = 'test_address';
        $payment_method->save();

        $this->assertEquals('test_address', $payment_method->pi_coin_address);
    }

    public function testGetPaymentMethod()
    {
        $payment_method = PaymentMethod::where('pi_coin_address', 'test_address')->first();

        $this->assertInstanceOf(PaymentMethod::class, $payment_method);
    }

    public function testUpdatePaymentMethod()
    {
        $payment_method = PaymentMethod::where('pi_coin_address', 'test_address')->first();
        $payment_method->pi_coin_address = 'new_address';
        $payment_method->save();

        $this->assertEquals('new_address', $payment_method->pi_coin_address);
    }

    public function testDeletePaymentMethod()
    {
        $payment_method = PaymentMethod::where('pi_coin_address', 'test_address')->first();
        $payment_method->delete();

        $this->assertNull(PaymentMethod::where('pi_coin_address', 'test_address')->first());
    }
}

// tests/PaymentControllerTest.php
<?php

use PHPUnit\Framework\TestCase;
use App\Http\Controllers\PaymentController;

class PaymentControllerTest extends TestCase
{
    public function testIndex()
    {
        $payment_controller = new PaymentController();
        $response = $payment_controller->index();

        $this->assertEquals('payment/index', $response->getName());
    }

    public function testCreate()
    {
        $payment_controller = new PaymentController();
        $request = new Illuminate\Http\Request();
        $request->input('pi_coin_address', 'test_address');
        $response = $payment_controller->create($request);

        $this->assertEquals('payment/index', $response->getName());
    }

    public function testEdit()
    {
        $payment_controller = new PaymentController();
        $payment_method = PaymentMethod::where('pi_coin_address', 'test_address')->first();
        $response = $payment_controller->edit($payment_method);

        $this->assertEquals('payment/edit', $response->getName());
    }

    public function testUpdate()
    {
        $payment_controller = new PaymentController();
        $payment_method = PaymentMethod::where('pi_coin_address', 'test_address')->first();
        $request = new Illuminate\Http\Request();
        $request->input('pi_coin_address', 'new_address');
        $response = $payment_controller->update($payment_method, $request);

        $this->assertEquals('payment/index', $response->getName());
    }

    public function testDestroy()
    {
        $payment_controller = new PaymentController();
        $payment_method = PaymentMethod::where('pi_coin_address', 'test_address')->first();
        $response = $payment_controller->destroy($payment_method);

        $this->assertEquals('payment/index', $response->getName());
    }
}
