# Covid Flask API
Simple Flask API for returning covid testing data for each month by country

Deployed onto https://covid-monthly-flask-api.herokuapp.com/
with available endpoint: `/country_tests_done`

Receives a json request of the form : `'{"country":"RO"}'` for following countries: 'DE', 'DK', 'RO', 'ES'  and 'SE'

### Using curl on heroku:
`curl -X GET -H 'Content-Type: application/json' https://covid-monthly-flask-api.herokuapp.com/country_tests_done -d '{"country": "DK"}'`


## Installation with conda for running locally:

clone git repository: 

1. open terminal
2. clone repo: `git clone https://github.com/antiiles/covid_flask_api.git`
3. set up venv with pyton 3.6 : `conda create -n flask python=3.6`
4. install packages: `pip install flask flask_restful pandas gunicorn`
5. navigate to cloned folder and run `python wsgi.py`

### Query local flask app:
`curl -X GET -H 'Content-Type: application/json' http://127.0.0.1:5000/country_tests_done -d '{"country": "DK"}'`
