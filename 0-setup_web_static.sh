#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static
sudo apt-get -y update
# Install Nginx
sudo apt-get -y install nginx
# Allow Port 80
sudo ufw allow 'Nginx HTTP'
# Creating folders
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
# Creating a HTML file
echo "<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
    <p>Nginx server test</p>
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html
# Creating a symblic link
sudo ln -sfn /data/web_static/releases/test/ /data/web_static/current
# Giving Ownership to ubuntu
sudo chown -R ubuntu:ubuntu /data/
# Nginx configuration
sudo sed -i '/listen 80 default_server/a location /hbnb_static/ {alias /data/web_static/current/;}' /etc/nginx/sites-available/default
# Restart
sudo service nginx restart
