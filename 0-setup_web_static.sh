#!/usr/bin/env bash
# A script that sets up your web servers for the deployment of web_static.

# Install Nginx if it not already installed
sudo apt-get -y update
sudo apt-get install -y nginx

# Create necessary folders if they don't exist
sudo mkdir -p /data/web_static/{releases/test,shared}

# Create a fake HTML file for testing
echo "<html><head></head><body>Test Item</body></html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create or recreate symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Set ownership to ubuntu user and group recursively
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
config_block="
location /hbnb_static {
	alias /data/web_static/current/;
	index index.html;
}"

# Add or update the config block in Nginx
sudo sed -i "/server {/a $config_block" /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart
