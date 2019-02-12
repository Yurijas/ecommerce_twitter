from app import app
from flask import render_template, url_for, redirect

@app.route('/')
@app.route('/index')
def index():
    products = {
        1001: {
            'title': 'Soap',
            'price': 3.98,
            'desc': 'Very clean soapy soap, descriptive text'
        },
        1002: {
            'title': 'Grapes',
            'price': 4.56,
            'desc': 'A bundle of grapey grapes, yummy'
        },
        1003: {
            'title': 'Pickles',
            'price': 5.67,
            'desc': 'A jar of pickles is pickley'
        },
        1004: {
            'title': 'Juice',
            'price': 2.68,
            'desc': 'Yummy orange juice'
        }
    }
    return render_template('index.html', products=products, title='Home')

@app.route('/posts')
def posts():
    return render_template('posts.html', title='Posts')
