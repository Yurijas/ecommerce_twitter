from app import app, db
from flask import render_template, url_for, redirect, flash
from app.forms import TitleForm, PostForm, LoginForm, RegisterForm
from app.models import Post, User
from flask_login import current_user, login_user, logout_user, login_required


@app.route('/')
@app.route('/index')
@app.route('/index/<header>', methods=['GET'])
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
        post = Post(tweet=tweet)

        # add post variable to database stage, then commit
        db.session.add(post)
        db.session.commit()

        return redirect(url_for('posts'))

    tweets = Post.query.all()

    return render_template('posts.html', title='Posts', form=form, tweets=tweets)

@app.route('/title', methods=['GET', 'POST'])
def title():
    form = TitleForm()

    # when form is submitted, rediret to home page, and pass itle to change what the h1 tag says
    if form.validate_on_submit():
        header = form.title.data
        return redirect(url_for('index', header=header))

    return render_template('title.html', title='Title', form=form )

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    #
    if current_user.is_authenticated:
        flash('You are already logged in!')
        return redirect(url_for('index'))

    form = RegisterForm()

    if form.validate_on_submit():
        user = User(
            first_name = form.first_name.data,
            last_name = form.last_name.data,
            username = form.username.data,
            email = form.email.data,
            url = form.url.data,
            age = int(form.age.data),
            bio = form.bio.data,
        )

        # set the password hash
        user.set_password(form.password.data)

        # add to stage and commit to db, then flash and return
        db.session.add(user)
        db.session.commit()
        flash('Congratulation, you are now registered!')
        return redirect(url_for('login'))

    return render_template('register.html', title='Register', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
