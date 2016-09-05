from flask import Flask  # The Flask object we'll use to create an application
from flask import render_template  # We'll use this for rendering Jinja templates so we're not embedding HTML in code
from flask import request  # Allows us to get info on HTTP requests we're receiving
import socket  # Using this to get IP and hostname info
import time  # Using this to get time info


# Create a Flask application object named app

app = Flask(__name__)


# Define a URL handler on the app object, this one looks for requests for the root URL of '/'

@app.route('/')
def hello_world():

    # Gather the information we want to show on the page

    hostname = socket.gethostname()  # Get our hostname
    ip_address = socket.gethostbyname(hostname)  # From the hostname, find our IP
    remote_ip = request.remote_addr  # Requester's IP address
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')  # Get the current time in a human friendly format
    header_keys = sorted(request.headers.keys())  # Won't let you iterate over the headers directly, so grab the keys and sort them

    # Stuff it all in a dict for easy passing to the template

    page_data = {
        'header_keys': header_keys,
        'header_data': request.headers,
        'hostname': hostname,
        'ip_address': ip_address,
        'remote_ip': remote_ip,
        'timestamp': timestamp
    }

    # Use render_template to produce HTML from the template file and page data, return that to the user

    return render_template('hello_world.html', data=page_data)


if __name__ == '__main__':

    # If we're launched directly, run Flask's built-in single-threaded web server and listen on port 12345

    app.run(host='0.0.0.0', port='12345')
