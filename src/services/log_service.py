from pymongo import MongoClient
from src.config import MONGO_URI
from datetime import datetime

client = MongoClient(MONGO_URI)
db = client["inventory"]
logs = db["activity_logs"]

def log_activity(user_id, action):
    logs.insert_one({
        "user_id": user_id,
        "action": action,
        "timestamp": datetime.utcnow()
    })