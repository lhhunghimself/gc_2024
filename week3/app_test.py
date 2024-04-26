# Import the necessary modules
from flask import Flask, render_template
from yelp import find_coffee
# Create a new Flask application instance
app = Flask(__name__)
# Define a route for the root URL ("/") that returns "Hello World"
@app.route('/home')
def showCoffeeShops():
    return render_template('home.html', coffeeShops=find_coffee())
@app.route('/login')
def login():
    return render_template('login.html')
# Run the application if this script is being run directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
