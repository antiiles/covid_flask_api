from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
import pandas as pd
# import ast

app = Flask(__name__)
app.config["Debug"] =True

total_tests = pd.read_csv(
    "C:/Users/anko/Documents/git_staging/flask/flask_app/data/downsampled_data.csv"
    ).set_index('year_week')

@app.errorhandler(404)
def pageNotFound(e):
    return "<h1> Error 404 <h1>", 404

@app.errorhandler(400)
def badRequest(e):
    return "<h1> Bad request <h1>", 400

@app.route("/")
def home():
    return "Hello there! General Kenobi...", 200

# @app.route("/country_tests_done", methods=["GET"])
# def get_all_data():
#     data = pd.read_csv("C:/Users/anko/Documents/git_staging/flask/flask_app/data/downsampled_data.csv")
#     data = data.to_dict()
#     return {'data': data}, 200

# @app.route('/json/<uuid>', methods=['GET', 'POST'])
# def add_message(uuid):
#     content = request.json
#     print(content['mytext'])
#     return jsonify({"uuid":uuid})

#  curl -X GET -H 'Content-Type: application/json' http://127.0.0.1:5000/country_tests_done -d '{"country": "DK","country":"DK"}'

@app.route('/country_tests_done', methods=['GET'])                                                                                                    
def all_tests():                                                                                                                              
    data = request.get_json()

    print(len(data.keys()))
    # print(type(data))
    # print(data.get("country"))
    # for (k,v) in data.items():
    #     print(k,v)
    
    if len(data.keys())>1:
        return badRequest(400)
    
    for key in data:
        if key != 'country':
            return pageNotFound(404)

    response_json = total_tests.tests_done.loc[(total_tests.country_code) == data.get("country")]

    return response_json.to_json()


if __name__ == '__main__':
    app.run()