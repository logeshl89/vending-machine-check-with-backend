import time
import requests
import socket
import logging
import os
from datetime import datetime

# Get the home directory of the current user
home_dir = os.path.expanduser("~")
log_file_path = os.path.join(home_dir, "heartbeat.log")

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file_path),
        logging.StreamHandler()
    ]
)

# Replace with your actual Render app domain (e.g., https://your-app-name.onrender.com)
SERVER_URL = "https://YOUR-RENDER-APP-NAME.onrender.com/api/heartbeat"
# Replace with a unique identifier for this Pi
DEVICE_ID = "pi-001"

def get_ip():
    try:
        # Try to get the IP address
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception as e:
        logging.warning(f"Could not determine IP address: {e}")
        return "unknown"

def send_heartbeat():
    try:
        ip = get_ip()
        payload = {
            "device_id": DEVICE_ID,
            "ip": ip,
            "timestamp": time.time()
        }
        
        response = requests.post(SERVER_URL, json=payload, timeout=10)
        
        if response.status_code == 200:
            logging.info(f"Heartbeat sent successfully. IP: {ip}")
            return True
        else:
            logging.error(f"Server responded with status code: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        logging.error("Failed to connect to server. Check your internet connection and server URL.")
        return False
    except requests.exceptions.Timeout:
        logging.error("Request timed out.")
        return False
    except Exception as e:
        logging.error(f"Unexpected error sending heartbeat: {e}")
        return False

def main():
    logging.info(f"Starting heartbeat script for device: {DEVICE_ID}")
    logging.info(f"Server URL: {SERVER_URL}")
    logging.info(f"Log file location: {log_file_path}")
    
    while True:
        try:
            success = send_heartbeat()
            if not success:
                logging.warning("Failed to send heartbeat, will retry in 30 seconds")
            
            # Wait 30 seconds before sending the next heartbeat
            time.sleep(30)
        except KeyboardInterrupt:
            logging.info("Heartbeat script stopped by user")
            break
        except Exception as e:
            logging.error(f"Unexpected error in main loop: {e}")
            time.sleep(30)  # Wait before retrying

if __name__ == "__main__":
    main()