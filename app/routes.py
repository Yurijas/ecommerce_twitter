from app import app
from flask import render_template, url_for, redirect
from app.forms import TitleForm, PostForm


# create posts global variable, only for placement before implementing database
# once databese is created, get rid of this variable
tweets = [
    {
        'post_id': 0,
        'tweet': 'Just threw the ring into volcano!',
        'date_posted': 'February 14th, 2019'
    }
]

@app.route('/')
@app.route('/index')
@app.route('/index/<header>', methods=['GET'])##
def index(header=''):
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
    return render_template('index.html', header=header, products=products, title='Home')

@app.route('/posts', methods=['GET', 'POST'])
def posts():
    form = PostForm()

    # when form is submitted appends to post lists, re-render posts page
    if form.validate_on_submit():
        tweet = form.tweet.data
        tweets.append({
            'post_id': len(tweets),
            'tweet': tweet,
            'date_posted': 'February 14th, 2019'
        })

    return render_template('posts.html', title='Posts', form=form, tweets=tweets)

@app.route('/title', methods=['GET', 'POST'])
def title():
    form = TitleForm()

    # when form is submitted, rediret to home page, and pass itle to change what the h1 tag says
    if form.validate_on_submit():
        header = form.title.data
        return redirect(url_for('index', header=header))

    return render_template('title.html', title='Title', form=form )
