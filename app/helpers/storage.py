"""Storage Helper Functions"""
from datetime import datetime
import json
from minio import Minio
from app.config import MinIO
from app.helpers import utils

def get_minio_client():
    """Returns MinIO client instance"""
    return Minio(
        MinIO.ENDPOINT,
        access_key=MinIO.ACCESS_KEY,
        secret_key=MinIO.SECRET_KEY,
        secure=MinIO.SECURE
    )

def store_sensor_data():
    """
    Store current sensor data to MinIO
    for now it uses dummy data
    """
    try:
        # Get boxes data
        # date_str = utils.get_utc_date(offset_hours=-1)
        boxes_data = utils.load_dummy_data("boxes_sample")
        if not boxes_data:
            return False, "No data available"

        # Create MinIO client
        client = get_minio_client()

        # Create bucket if it doesn't exist
        if not client.bucket_exists(MinIO.BUCKET_NAME):
            client.make_bucket(MinIO.BUCKET_NAME)

        # Generate filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"sensor_data_{timestamp}.json"

        # Convert data to JSON string
        json_data = json.dumps(boxes_data).encode('utf-8')

        # Upload to MinIO
        client.put_object(
            MinIO.BUCKET_NAME,
            filename,
            data=json_data,
            length=len(json_data),
            content_type='application/json'
        )

        return True, f"Data stored successfully as {filename}"

    except ValueError as e:
        return False, f"Error storing data: {str(e)}"
