import sys
sys.path.insert(0, '/var/www/html/flask_demo')
sys.path.append('/usr/local/lib/python2.7/site-packages')
sys.path.append('/usr/lib/python2.7/dist-packages/')
sys.path.append('/usr/lib64/python2.7/dist-packages/')

from flask_hello_world import app as application
