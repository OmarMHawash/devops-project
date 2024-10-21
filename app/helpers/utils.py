"""Utility Functions"""
from typing import Final
from datetime import datetime, timedelta
import json
import os
import requests
from app.config import Config

def get_request(url):
    """
    GET request template with timeout\n
    Args:
        `url` (str) the full request url

    Returns:
        `response.json()` if status code is 200 else `None`
    """
    print(f"GET: {url}")
    response = requests.get(url, timeout=Config.REQUEST_TIMEOUT)
    if response.status_code == 200:
        return response.json()
    print(f"Error: {response.status_code}\n {response.text}")
    return None, 500

def get_utc_date(offset_hours=0) -> str:
    """
        returns a string in the format of "YYYY-MM-DDTHH:MM:SS.000Z"\n
        Args:
            `offset_hours` (int) the number of hours to offset from UTC
            default is 0
    """
    strip_length: Final[int] = 3
    extra_char: Final[str] = 'Z'

    utc_now =  datetime.now() + timedelta(hours=offset_hours)
    modified_utc_now = str(utc_now.isoformat())[:-strip_length] + extra_char

    return modified_utc_now

def get_avg_temp(boxes_arr:dict) -> str:
    """
    Returns the average temperature of all given boxes data\n
    Args:
        `boxes_arr` (dict) boxes data\n
    """
    total = 0
    count = 0

    for box in boxes_arr:
        for sensor in box['sensors']:
            if sensor['title'] == 'temperature' and 'lastMeasurement' in sensor:
                total += float(sensor['lastMeasurement']['value'])
                count += 1

    if count > 0:
        temp = total / count
        return round(temp, 2)
    return None

def load_dummy_data(filename:str) -> dict:
    """Sample for loading dummy data"""

    if not os.path.isfile(f'app/static/{filename}.json'):
        print(f"Error: {filename}.json not found")
        return None

    try:
        with open(f'app/static/{filename}.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except ImportError as e:
        print(f"Error: {e}")
        return None

def get_temp_status(temp:float) -> str:
    """Returns the temperature status\n
    Less than 10: Too Cold
    Between 11-36: Good
    More than 37: Too Hot
    """
    if temp < 10:
        return "Too Cold"
    if temp < 36:
        return "Good"
    return "Too Hot"
