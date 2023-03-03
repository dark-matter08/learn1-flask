from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World</h1>'


@app.route('/<name>')
def print_name(name):
    return 'Hi, Mr. {}'.format(name)


if __name__ == '__main__':
    app.run(debug=True)
