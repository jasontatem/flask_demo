#!/bin/bash

# Update package repos

/usr/bin/yum -y update

# Install pip

/usr/bin/yum install -y epel-release
/usr/bin/yum install -y python-pip

# Install Flask

/usr/bin/pip install flask

# Install/start Apache, enable start on OS startup

/usr/bin/yum install -y httpd
/usr/bin/yum install -y mod_wsgi
/usr/bin/systemctl start httpd
/usr/bin/systemctl enable httpd

# Allow port 80 traffic through OS firewall

/usr/bin/firewall-cmd --permanent --add-port=80/tcp
/usr/bin/firewall-cmd --reload

# Install git

/usr/bin/yum install -y git

# Install Flask demo app

cd /var/www/html
/usr/bin/git clone https://github.com/jasontatem/flask_demo

# Add WSGI configuration to Apache

/bin/cat /var/www/html/flask_demo/etc/apache_wsgi_module_config > /etc/httpd/conf.modules.d/10-wsgi.conf
/bin/cat /var/www/html/flask_demo/etc/apache_wsgi_config >> /etc/httpd/conf/httpd.conf

# Restart Apache

/usr/bin/systemctl restart httpd
