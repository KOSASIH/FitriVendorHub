import os
import requests
from dotenv import load_dotenv
from pi_network import PiNetworkClient

class PaymentMethod:
    def __init__(self, user_id):
        self.user_id = user_id
        self.pi_coin_address = None
        self.load_env_variables()

    def load_env_variables(self):
        load_dotenv()
        self.pi_network_api_key = os.getenv('PI_NETWORK_API_KEY')

    def create(self, pi_coin_address):
        self.pi_coin_address = pi_coin_address
        self.save()

    def save(self):
        # Save the payment method to the database
        pass

    def validate(self, request):
        # Validate the payment method data
        pass

    def process_payment(self, request):
        pi_network_client = PiNetworkClient(self.pi_network_api_key)
        payment_response = pi_network_client.create_payment(
            amount=request.input('amount'),
            currency='PI',
            address=self.pi_coin_address,
        )

        if payment_response.successful():
            self.payment_token = payment_response.payment_token
            self.save()
            return True

        return False

class PaymentController:
    def __init__(self):
        self.payment_method = PaymentMethod(Auth.get_user_id())

    def index(self, request):
        payment_methods = PaymentMethod.objects.filter(user_id=self.payment_method.user_id)
        return render(request, 'payment/index.html', {'payment_methods': payment_methods})

    def create(self, request):
        self.payment_method.create(request.input('pi_coin_address'))
        return redirect('payment_index')

    def edit(self, request, payment_method_id):
        payment_method = PaymentMethod.objects.get(id=payment_method_id)
        return render(request, 'payment/edit.html', {'payment_method': payment_method})

    def update(self, request, payment_method_id):
        payment_method = PaymentMethod.objects.get(id=payment_method_id)
        payment_method.validate(request)
        payment_method.save()
        return redirect('payment_index')

    def destroy(self, payment_method_id):
        payment_method = PaymentMethod.objects.get(id=payment_method_id)
        payment_method.delete()
        return redirect('payment_index')

    def process(self, request, payment_method_id):
        payment_method = PaymentMethod.objects.get(id=payment_method_id)
        if payment_method.process_payment(request):
            return redirect('payment_index')
        else:
            # Handle payment processing failure
            pass
