#!/usr/bin/env python3
# Import the necessary modules
from flask import Flask, render_template, request, session
from forms import LoginForm
from yelp import find_coffee
from flask_login import login_user, logout_user, login_required 
from models import db, login_manager, UserModel

# Create a new Flask application instance
app = Flask(__name__)
app.secret_key='super secret key'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./login.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
login_manager.init_app(app)

#add user routine

# create database with a test user

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
    form=LoginForm()
    if request.method == 'POST':
        if ('city' in session):
            session.pop('city')
    return render_template('login.html',form=form)
@app.route("/logout")# added
@login_required
def logout():
    session.pop('city',None)
    return redirect(url_for('login'))#added
# Run the application if this script is being run directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug='True', port=5000)
