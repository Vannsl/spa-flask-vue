from flask import Flask, render_template, jsonify
from random import *
from flask_cors import CORS
import requests

app = Flask(__name__,
            static_folder = "./frontend/dist/static",
            template_folder = "./frontend/dist")
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

FAQ = {
    'faq1': {
        'id': 1,
        'title': 'How can I track my orders & payment?',
        'message': 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.',
    },
    'faq2': {
        'id': 2,
        'title': 'How do you ship your orders',
        'message': 'At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.',
    },
    'faq3': {
        'id': 3,
        'title': 'How can I change my shipment address?',
        'message': 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.',
    },
}

@app.route('/api/faq')
def faq():
    response = FAQ
    return jsonify(response)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if app.debug:
        return requests.get('http://localhost:8080/{}'.format(path)).text
    return render_template("index.html")
