import os
from _datetime import datetime

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

from thermos.forms import BookmarkForm

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = b'\xda\x0cx\xcf\xd1Qsf\x05,\xddI\xa7\x84}B\xca\x97\xe0Qo\xe7T\xdd'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite::///' + os.path.join(basedir, 'thermos.db')
db = SQLAlchemy(app)

bookmarks = []


def store_bookmark(url, description):
    bookmarks.append(dict(
        url=url,
        user="maurice",
        date=datetime.utcnow(),
        description=description
    ))


def new_bookmarks(num):
    return sorted(bookmarks, key=lambda bm: bm['date'], reverse=True)[:num]


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', new_bookmarks=new_bookmarks(5))


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = BookmarkForm()
    if form.validate_on_submit():
        url = form.url.data
        description = form.description.data
        store_bookmark(url, description)
        flash("Stored '{}'".format(description))
        return redirect(url_for('index'))
    return render_template('add.html', form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)
