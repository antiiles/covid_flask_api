from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
import pandas as pd

app = Flask(__name__)

#load data from csv into memory
total_tests = pd.read_csv(
    "./data/downsampled_data.csv"
    ).set_index('year_week')

@app.errorhandler(404)
def pageNotFound(e):
    return "<h1> Error 404 <h1>", 404

@app.errorhandler(400)
def badRequest(e):
    return "<h1> Bad request <h1>", 400

#landing page
@app.route("/")
def home():
    return "Hello there! General Kenobi...", 200

# api endpoint for receiving testing data with some typical error checking
@app.route('/country_tests_done', methods=['GET'])                                                                                                    
def all_tests():                                                                                                                              
    data = request.get_json()
    
    if len(data.keys())>1:
        return badRequest(400)
    
    for key in data:
        if key != 'country':
            return pageNotFound(404)

    response_json = total_tests.tests_done.loc[(total_tests.country_code) == data.get("country")]
    return response_json.to_json()


if __name__ == '__main__':
    app.run()