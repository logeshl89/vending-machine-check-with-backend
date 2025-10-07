# Simple Deployment Instructions

This guide will help you deploy the Raspberry Pi Status Dashboard as a combined frontend/backend application on Render.

## Prerequisites

1. A Render account (free available at [render.com](https://render.com))
2. Your code repository on GitHub (or another Git provider supported by Render)

## Deployment Steps

### 1. Fork or Push Your Code to GitHub

First, make sure your code is available on GitHub. You can either:
- Fork this repository if it's public
- Create a new repository and push your code

### 2. Create a New Web Service on Render

1. Go to your Render dashboard
2. Click "New+" and select "Web Service"
3. Connect your GitHub account when prompted
4. Select your repository

### 3. Configure Your Web Service

Fill in the following settings:
- **Name**: `raspberry-pi-status-dashboard` (or any name you prefer)
- **Environment**: `Python 3`
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn -w 4 -b 0.0.0.0:$PORT server:app`
- **Instance Type**: Free (for testing) or Standard (for production)

### 4. Deploy

Click "Create Web Service". Render will:
1. Clone your repository
2. Install dependencies
3. Build your application
4. Start your server

## Post-Deployment Steps

### 1. Update Your Raspberry Pi Configuration

After deployment, you'll get a URL for your service (something like `https://your-app-name.onrender.com`). 

Update your Raspberry Pi [heartbeat.py](file:///d%3A/Raspi-status-check/simple_deployment%5Cheapbeat.py) script with this URL:

```python
# Replace with your actual Render domain
SERVER_URL = "https://your-app-name.onrender.com/api/heartbeat"
```

### 2. Test Your Deployment

1. Visit your Render URL in a browser to see the dashboard
2. Start your Raspberry Pi heartbeat script
3. Refresh the dashboard to see your device appear

## Render-Specific Features

### Auto-Deploy
Render can automatically redeploy your application when you push changes to your repository.

### Logs
View your application logs directly in the Render dashboard:
1. Go to your service dashboard
2. Click "Logs" in the sidebar

### Scaling
Render allows you to scale your application:
1. Go to your service dashboard
2. Click "Settings" in the sidebar
3. Modify the "Instance Count" and "Instance Type"

## Troubleshooting

### Application Won't Start
1. Check the logs in your Render dashboard
2. Verify all dependencies are in [requirements.txt](file:///d%3A/Raspi-status-check/simple_deployment%5Crequirements.txt)
3. Ensure your start command is correct

### Devices Not Appearing
1. Verify your Raspberry Pi is sending heartbeats to the correct URL
2. Check that your device IDs are unique
3. Confirm network connectivity from your Pi to Render

### Performance Issues
For a device monitoring application with moderate usage, the free tier should be sufficient.

## Cost Considerations

- **Free Tier**: Includes 750 free hours per month (about 31 days)
- **Sleep Mode**: Free instances sleep after 15 minutes of inactivity

For a device monitoring application with moderate usage, the free tier should be sufficient.