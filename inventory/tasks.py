from celery import Celery
from app import db
from models import Product, InventoryItem, Warehouse
from schemas import ProductSchema, InventoryItemSchema, WarehouseSchema

celery = Celery(__name__)

@celery.task
def update_inventory(product_id, quantity):
    # update inventory quantity
    product = Product.query.get(product_id)
    if product is None:
        return jsonify({'error': 'Product not found'}), 404
    product.quantity += quantity
    db.session.commit()
    return jsonify(ProductSchema().dump(product))

@celery.task
def restock_warehouse(warehouse_id, product_id, quantity):
    # restock warehouse with product
    warehouse = Warehouse.query.get(warehouse_id)
    if warehouse is None:
        return jsonify({'error': 'Warehouse not found'}), 404
    product = Product.query.get(product_id)
    if product is None:
        return jsonify({'error': 'Product not found'}), 404
    inventory_item = InventoryItem(warehouse_id=warehouse_id, product_id=product_id, quantity=quantity)
    db.session.add(inventory_item)
    db.session.commit()
    return jsonify(InventoryItemSchema().dump(inventory_item))
