from flask import Blueprint, jsonify, request
from app.utils.error_handler import add_api_error_responses

service_bp = Blueprint("service", __name__)


@service_bp.route('/health',
                  methods=['GET'],
                  strict_slashes=False)
@add_api_error_responses
def health():
    return jsonify(''), 200


@service_bp.route('/',
                  methods=['GET'],
                  strict_slashes=False)
@add_api_error_responses
def base():
    return jsonify(''), 200
