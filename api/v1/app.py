#!/usr/bin/python3
"""Creating a flask app
"""
from models import storage
from flask import Flask, jsonify
from api.v1.views import app_views
from os import getenv
from flask_cors import CORS


app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources=({r"/*": {"origins": "0.0.0.0"}}))


@app.errorhandler(404)
def page_not_found(e):
    not_found = {"error": "Not found"}
    return jsonify(not_found), 404


@app.teardown_appcontext
def teardown_db(self):
    storage.close()


if __name__ == '__main__':
    if getenv('HBNB_API_HOST') and getenv('HBNB_API_PORT'):
        app.run(
               host=getenv('HBNB_API_HOST'),
               port=getenv('HBNB_API_PORT'),
               threaded=True,
               debug=True)
    else:
        app.run(
               host='0.0.0.0',
               port='5000',
               threaded=True,
               debug=True)
