from flask import Blueprint, jsonify, request
from.models import Customer, SalesTransaction
from.schemas import CustomerSchema, SalesTransactionSchema

api = Blueprint('api', __name__)

@api.route('/customers', methods=['GET'])
def get_customers():
    customers = Customer.query.all()
    return jsonify([CustomerSchema().dump(customer) for customer in customers])

@api.route('/customers/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    customer = Customer.query.get(customer_id)
    if not customer:
        return jsonify({'error': 'Customer not found'}), 404
    return jsonify(CustomerSchema().dump(customer))

@api.route('/sales_transactions', methods=['GET'])
def get_sales_transactions():
    sales_transactions = SalesTransaction.query.all()
    return jsonify([SalesTransactionSchema().dump(sales_transaction) for sales_transaction in sales_transactions])

@api.route('/sales_transactions/<int:transaction_id>', methods=['GET'])
def get_sales_transaction(transaction_id):
    sales_transaction = SalesTransaction.query.get(transaction_id)
    if not sales_transaction:
        return jsonify({'error': 'Sales transaction not found'}), 404
    return jsonify(SalesTransactionSchema().dump(sales_transaction))

@api.route('/customers/<int:customer_id>/add_points', methods=['POST'])
def add_points(customer_id):
    customer = Customer.query.get(customer_id)
    if not customer:
        return jsonify({'error': 'Customer not found'}), 404
    points_to_add = request.json['points']
    customer.loyalty_points += points_to_add
    db.session.commit()
    return jsonify(CustomerSchema().dump(customer))

@api.route('/customers/<int:customer_id>/invite_guest', methods=['POST'])
def invite_guest(customer_id):
    customer = Customer.query.get(customer_id)
    if not customer:
        return jsonify({'error': 'Customer not found'}), 404
    if customer.loyalty_points >= 1000:
        # implement invite guest logic here
        pass
    return jsonify(CustomerSchema().dump(customer))
