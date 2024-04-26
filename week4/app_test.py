# Import the necessary modules
from flask import Flask, render_template, request, session
from yelp import find_coffee
# Create a new Flask application instance
app = Flask(__name__)
app.secret_key='super secret key'

# Define a route for the root URL ("/") that returns "Hello World"
@app.route('/home', methods=['GET'])
def showCoffeeShops():
    if request.method == 'GET' and 'city' in request.args and request.args.get('city') is not None: 
        session['city'] = request.args.get('city')
    if 'city' in session:
        return render_template('home.html', coffeeShops=find_coffee(city=session['city']))
    return render_template('home.html', coffeeShops=find_coffee())
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if ('city' in session):
            session.pop('city')
    return render_template('login.html')
# Run the application if this script is being run directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug='True', port=5000)
