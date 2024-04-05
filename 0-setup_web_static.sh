#!/usr/bin/env bash
# Setup the web servers for the deployment of web_static

# Install nginx if it is not installed
if [ ! -x "$(command -v nginx)" ]
then
        apt-get -y update
        apt-get -y install nginx
fi

# Create new directories
mkdir -p /data/web_static/shared/
mkdir -p "/data/web_static/releases/test/"

# Make a fake content inside the file
template="<html>
        <head>
        </head>
        <body>
                Holberton School
        </body>
</html>"
echo "$template" > "/data/web_static/releases/test/index.html"

# Create a symbolic link
ln -sf "/data/web_static/releases/test/" "/data/web_static/current"

# Change the ownership of the folder called data
chown -R ubuntu:ubuntu /data/

# Varaibles to be used with the sed command
new_location="\n\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}"
server="server_name _"

# append the new location
sed -i "/$server/a \ $new_location" /etc/nginx/sites-available/default

# Restart the nginx server
service nginx restart
