from flask_restplus import Api
from flask import Blueprint
from ..controller.predict_disease import ns as fb_data

bp = Blueprint('Classification Algorithm', __name__, url_prefix='/api')

api = Api(bp, catch_all_404s=True)

api.add_namespace(fb_data)
