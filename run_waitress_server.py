#import System-specific parameters and  OS module in Python provides a way of using operating system dependent functionality.
import sys, os  
# Waitress is a pure-python WSGI server
from waitress import serve 
# Providing path for app.py module 
sys.path.insert(0, './app')
# From app module import APP flask variable
from app import APP

# This wil serve the application
serve(APP,host="0.0.0.0",port=os.environ["PORT"])  
#serve(APP,host="localhost",port="5000")  
#APP.run(debug=True)