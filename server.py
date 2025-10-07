from flask import Flask, request, jsonify
from flask_cors import CORS
import time
import os

app = Flask(__name__, static_folder='static')
CORS(app)  # Enable CORS for all routes

# In-memory database (device_id -> info)
devices = {}

def get_device_ip(data):
    return data.get("ip", "unknown") if data else "unknown"

def get_device_id(data):
    return data["device_id"] if data else "unknown"

@app.route("/api/heartbeat", methods=["POST"])
def heartbeat():
    data = request.json
    
    # Handle case where data is None
    if data is None:
        return jsonify({"error": "No JSON data received"}), 400
    
    device_id = get_device_id(data)
    devices[device_id] = {
        "ip": get_device_ip(data),
        "last_seen": time.time()
    }
    print(f"Received from {device_id}")
    return jsonify({"status": "ok"}), 200

@app.route("/api/devices", methods=["GET"])
def get_devices():
    now = time.time()
    result = []
    for device_id, info in devices.items():
        delta = now - info["last_seen"]
        status = "online" if delta < 60 else "offline"
        result.append({
            "device_id": device_id,
            "ip": info["ip"],
            "last_seen": int(info["last_seen"]),
            "status": status
        })
    return jsonify(result)

# Serve the main page
@app.route("/")
def index():
    return app.send_static_file('index.html')

# Health check endpoint for Render
@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    # Get port from environment variable or default to 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=port, debug=True)