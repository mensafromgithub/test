from flask import Flask, render_template, redirect, jsonify
from flask import make_response


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(400)
def bad_request(_):
    return make_response(jsonify({'error': 'Bad Request'}), 400)


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html", title='test')


def main():
    app.run(port=5000, host='127.0.0.1')
