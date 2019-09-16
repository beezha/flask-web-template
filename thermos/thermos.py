from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="Sample title", user="Maurice Ilagan")


@app.route('/add')
def add():
    return render_template('add.html')


if __name__ == '__main__':
    app.run(debug=True)
