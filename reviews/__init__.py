from flask import Blueprint

reviews_blueprint = Blueprint('reviews', __name__)

from. import models, schemas, views, routes
