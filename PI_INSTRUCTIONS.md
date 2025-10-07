# Raspberry Pi Setup Instructions

This document provides instructions for setting up your Raspberry Pi to send heartbeat signals to your Render-deployed status dashboard.

## Setup Steps

1. Install required packages:
   ```bash
   sudo apt update
   sudo apt install python3-pip -y
   ```

2. Create a virtual environment (recommended):
   ```bash
   python3 -m venv heartbeat_env
   ```

3. Activate the virtual environment:
   ```bash
   source heartbeat_env/bin/activate
   ```

4. Install required Python packages:
   ```bash
   pip install requests
   ```

5. Copy the [heartbeat.py](file:///d%3A/Raspi-status-check/simple_deployment%5Cheapbeat.py) script to your Raspberry Pi:
   - You can download it directly from your Render app or copy it manually

6. Edit the [heartbeat.py](file:///d%3A/Raspi-status-check/simple_deployment%5Cheapbeat.py) script to configure your Render app URL:
   ```python
   # Replace with your actual Render app domain
   SERVER_URL = "https://YOUR-RENDER-APP-NAME.onrender.com/api/heartbeat"
   # Replace with a unique identifier for this Pi
   DEVICE_ID = "pi-001"  # e.g., "vending-machine-01"
   ```

7. Test the script manually:
   ```bash
   python3 heartbeat.py
   ```

8. Make the script run automatically on boot:
   - Edit crontab: `crontab -e`
   - Add this line: `@reboot /home/pi/heartbeat_env/bin/python /home/pi/heartbeat.py &`

## Monitoring

To check if the script is running:
```bash
ps aux | grep heartbeat.py
```

To view the logs:
```bash
tail -f ~/heartbeat.log
```

## Troubleshooting

1. **Device not appearing in dashboard**:
   - Check the log file: `tail -f ~/heartbeat.log`
   - Verify your Render app URL is correct
   - Ensure your Pi has internet access

2. **Connection errors**:
   - Verify your Render app is running
   - Check that you've replaced "YOUR-RENDER-APP-NAME" with your actual app name
   - Ensure there are no typos in the URL

3. **Script not starting on boot**:
   - Check that the path in crontab is correct
   - Verify the virtual environment path is correct
   - Check cron logs: `grep CRON /var/log/syslog`