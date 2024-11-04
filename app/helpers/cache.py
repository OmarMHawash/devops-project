"""Valkey"""
import json
import valkey
from app.config import Valkey as ValkeyConfig, Config

val = valkey.Valkey(host=ValkeyConfig.HOST, port=ValkeyConfig.PORT, db=ValkeyConfig.DB)

def set_cache(key, value):
    """Set cache"""
    try:
        json_dump = json.dumps(value)
        val.set(key, json_dump, ex=ValkeyConfig.EXP)
        print(val.ttl(key))
    except IOError as e:
        print(e)
        return False
    return True

def get_cache(key):
    """Get cache"""
    try:
        data = val.get(key)
        if data is None and Config.DEBUG_MODE:
            print("Cache miss")
        return data
    except KeyError as e:
        print(e)
        return None
