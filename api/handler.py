from flask import Flask, request, Response
from rossmann import Rossmann
import pickle
import pandas as pd

# loading model - pipeline
model = pickle.load(open(
    '/Users/Lidiane/Documents/projects_portfolio/rossmann/models/pipe.pkl', 'rb'))

# initialize app
app = Flask(__name__)


@app.route('/rossmann/predict', methods=['POST'])
def rossmann_predict():
    test_json = request.get_json()

    if test_json:
        if isinstance(test_json, dict):
            test_raw = pd.DataFrame(test_json, index=[0])
        else:
            test_raw = pd.DataFrame(test_json, columns=test_json[0].keys())

        # instantiate rossmann
        initial_pipeline = Rossmann()

        # data cleaning
        data1 = initial_pipeline.data_cleaning(test_raw)

        # feature eng
        data2 = initial_pipeline.feature_engineering(data1)

        # data prep
        data3 = initial_pipeline.data_prep(data2)

        # prediction
        data_response = initial_pipeline.get_prediction(model, test_raw, data3)

        # create response json
        raw_data = {'raw_data': test_json}
        data_response.update(raw_data)

        return data_response

    else:
        return Response('{}', status=200, mimetype='application/json')


if __name__ == '__main__':
    app.run('0.0.0.0')