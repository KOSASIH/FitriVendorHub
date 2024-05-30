from flask import Blueprint

inventory_blueprint = Blueprint('inventory', __name__)

from. import models, schemas, tasks, routes
