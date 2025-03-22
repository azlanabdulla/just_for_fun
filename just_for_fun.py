from flask import Flask, request, render_template, redirect, url_for
import logging
from datetime import datetime

app = Flask(__name__)

# Configure logging to a file
logging.basicConfig(
    filename='visitor.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

@app.route('/')
def index():
    # Gather visitor data
    visitor_data = {
        'ip_address': request.remote_addr,
        'user_agent': request.headers.get('User-Agent'),
        'referrer': request.referrer,
        'cookies': request.cookies,
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'visited_url': request.url
    }
    
    # Log the visitor data
    log_message = (
        f"IP: {visitor_data['ip_address']} | "
        f"User-Agent: {visitor_data['user_agent']} | "
        f"Referrer: {visitor_data['referrer']} | "
        f"Cookies: {visitor_data['cookies']} | "
        f"Visited URL: {visitor_data['visited_url']}"
    )
    app.logger.info(log_message)
    
    # Render your index.html template (make sure it's in your templates folder)
    return render_template('index.html')

# You can add more routes if needed that also log visitor data
@app.route('/contact')
def contact():
    # Log visit to the contact page as well
    log_message = f"IP: {request.remote_addr} visited {request.url}"
    app.logger.info(log_message)
    return render_template('contact.html')

if __name__ == '__main__':
    # Make sure to run the app in production using a proper WSGI server
    app.run(host='0.0.0.0', port=80, debug=True)
