from flask import render_template, flash, redirect, url_for, abort, request
from flask_login import login_required, login_user

from thermos import app, db, login_manager
from .forms import BookmarkForm, LoginForm
from .models import User, Bookmark


@login_manager.user_loader
def load_user(userid):
    return User.query.get(int(userid))


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', new_bookmarks=Bookmark.newest(5))


@app.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    form = BookmarkForm()
    if form.validate_on_submit():
        url = form.url.data
        description = form.description.data
        bm = Bookmark(user=logged_in_user(), url=url, description=description)
        db.session.add(bm)
        db.session.commit()
        flash("Stored '{}'".format(description))
        return redirect(url_for('index'))
    return render_template('add.html', form=form)


@app.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', user=user)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None:
            login_user(user, form.remember_me.data)
            flash("Logged in successfully as {}.".format(user.username))
            return redirect(request.args.get('next') or url_for('user', username=user.username))
        flash('Incorrect username or password.')
    return render_template("login.html", form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500