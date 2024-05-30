import os
import json
from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from flask_cors import CORS
from flask_apscheduler import APScheduler
from celery import Celery
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config["SECRET_KEY"] = "super_secret_key_here"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://user:password@host:port/dbname"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = "jwt_secret_key_here"
app.config["JWT_TOKEN_LOCATION"] = ["headers"]
app.config["JWT_HEADER_NAME"] = "Authorization"
app.config["JWT_HEADER_TYPE"] = "Bearer"

db = SQLAlchemy(app)
ma = Marshmallow(app)
jwt = JWTManager(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
scheduler = APScheduler()
celery = Celery(app.name, broker="amqp://guest:guest@localhost")

# Define models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

class Vendor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship("User", backref="vendors")

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    vendor_id = db.Column(db.Integer, db.ForeignKey("vendor.id"))
    vendor = db.relationship("Vendor", backref="products")

# Define schemas
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True

class VendorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Vendor
        load_instance = True

class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        load_instance = True

# Define admin views
class UserAdminView(ModelView):
    column_list = ["username", "email"]

class VendorAdminView(ModelView):
    column_list = ["name", "description"]

class ProductAdminView(ModelView):
    column_list = ["name", "description", "price"]

admin = Admin(app, name="FitriVendorHub", template_mode="bootstrap3")
admin.add_view(UserAdminView(User, db.session))
admin.add_view(VendorAdminView(Vendor, db.session))
admin.add_view(ProductAdminView(Product, db.session))

# Define routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            access_token = create_access_token(identity=username)
            return jsonify({"access_token": access_token})
        return jsonify({"error": "Invalid credentials"}), 401
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/api/vendors", methods=["GET"])
@jwt_required
def get_vendors():
    vendors = Vendor.query.all()
    return jsonify(VendorSchema(many=True).dump(vendors))

@app.route("/api/products", methods=["GET"])
@jwt_required
def get_products():
    products = Product.query.all()
    return jsonify(ProductSchema(many=True).dump(products))

@app.route("/api/vendor/<int:vendor_id>/products", methods=["GET"])
@jwt_required
def get_vendor_products(vendor_id):
    vendor = Vendor.query.get(vendor_id)
    if vendor:
products = vendor.products
        return jsonify(ProductSchema(many=True).dump(products))
    return jsonify({"error": "Vendor not found"}), 404

@app.route("/api/vendor", methods=["POST"])
@jwt_required
def create_vendor():
    name = request.json["name"]
    description = request.json["description"]
    user_id = request.json["user_id"]
    user = User.query.get(user_id)
    if user:
        vendor = Vendor(name=name, description=description, user=user)
        db.session.add(vendor)
        db.session.commit()
        return jsonify(VendorSchema().dump(vendor)), 201
    return jsonify({"error": "User not found"}), 404

@app.route("/api/product", methods=["POST"])
@jwt_required
def create_product():
    name = request.json["name"]
    description = request.json["description"]
    price = request.json["price"]
    vendor_id = request.json["vendor_id"]
    vendor = Vendor.query.get(vendor_id)
    if vendor:
        product = Product(name=name, description=description, price=price, vendor=vendor)
        db.session.add(product)
        db.session.commit()
        return jsonify(ProductSchema().dump(product)), 201
    return jsonify({"error": "Vendor not found"}), 404

@app.route("/api/vendor/<int:vendor_id>", methods=["PUT"])
@jwt_required
def update_vendor(vendor_id):
    vendor = Vendor.query.get(vendor_id)
    if vendor:
        vendor.name = request.json["name"]
        vendor.description = request.json["description"]
        db.session.commit()
        return jsonify(VendorSchema().dump(vendor))
    return jsonify({"error": "Vendor not found"}), 404

@app.route("/api/product/<int:product_id>", methods=["PUT"])
@jwt_required
def update_product(product_id):
    product = Product.query.get(product_id)
    if product:
        product.name = request.json["name"]
        product.description = request.json["description"]
        product.price = request.json["price"]
        db.session.commit()
        return jsonify(ProductSchema().dump(product))
    return jsonify({"error": "Product not found"}), 404

@app.route("/api/vendor/<int:vendor_id>", methods=["DELETE"])
@jwt_required
def delete_vendor(vendor_id):
    vendor = Vendor.query.get(vendor_id)
    if vendor:
        db.session.delete(vendor)
        db.session.commit()
        return jsonify({"message": "Vendor deleted"})
    return jsonify({"error": "Vendor not found"}), 404

@app.route("/api/product/<int:product_id>", methods=["DELETE"])
@jwt_required
def delete_product(product_id):
    product = Product.query.get(product_id)
    if product:
        db.session.delete(product)
        db.session.commit()
        return jsonify({"message": "Product deleted"})
    return jsonify({"error": "Product not found"}), 404

# Define background tasks
@scheduler.task
def send_email_task():
    # Implement email sending logic here
    pass

# Define Celery tasks
@celery.task
def process_data_task(data):
    # Implement data processing logic here
    pass

# Initialize scheduler and Celery
scheduler.init_app(app)
scheduler.start()
celery.conf.update(app.config)

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
