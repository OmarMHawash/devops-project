"""API Routes & Functions"""
from flask import Blueprint, jsonify
from app.config import Config, OpenSense
from app.helpers import utils

main = Blueprint('main', __name__)
api = Blueprint('api', __name__)

@main.route('/', methods=['GET'])
def index():
    """Health Check"""
    return jsonify({"Status": "OK"}), 200

@main.route('/version', methods=['GET'])
def version():
    """Version Check"""
    if Config.APP_VERSION:
        return jsonify({"Version": Config.APP_VERSION}), 200
    return jsonify({"Error": "Version not set"}), 500

@api.route('/temperature', methods=['GET'])
def temperature() -> dict:
    """
    Temperature GET endpoint\n
    Return current average temperature based on all senseBox data.
    Ensure that the data is no older 1 hour.\n
    all_boxes_params: `base_url`?date=:date&phenomenon=:phenomenon&format=:format
    """

    if OpenSense.API_URL is None or OpenSense.GET_BOXES_PREFIX is None:
        return jsonify({"Error": "OpenSense API or GET_BOXES_PREFIX not set"}), 500

    date_str = utils.get_utc_date(offset_hours=OpenSense.BOXES_OFFSET_HOURS)

    base_url = f"{OpenSense.API_URL}{OpenSense.GET_BOXES_PREFIX}"
    url_params = f"?date={date_str}&phenomenon=temperature"

    boxes_data = utils.get_request(f"{base_url}{url_params}")
    avg_temp = utils.get_avg_temp(boxes_data)

    if avg_temp is None:
        return jsonify({"Error": "Temperature data not found"}), 500
    return jsonify({"Average temperature": avg_temp}), 200
