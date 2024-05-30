from flask import Blueprint

recommendations_blueprint = Blueprint('recommendations', __name__)

from. import models, schemas, tasks, routes
