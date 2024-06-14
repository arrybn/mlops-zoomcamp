import predict
from flask import Flask, request, jsonify
import click
import numpy as np

app = Flask('duration-prediction-service')

@app.route('/predict', methods=['POST'])
def predict_endpoint():
    ride = request.get_json()

    X = predict.prepare_features(ride)

    result = {'duration': list(predict.predict(X))}

    return jsonify(result)


@app.cli.command("predict-for-year-month")
@app.route('/predict-for-year-month/<year>/<month>', methods=['POST'])
@click.argument("year", type=int)
@click.argument("month", type=int)
def predict_year_month(year, month):
    url = f'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{year}-{month:02}.parquet'

    app.logger.info(url)
    data_dicts = predict.read_data(url)
    X = predict.prepare_features(data_dicts)

    result = jsonify({'mean_predicted_duration': np.mean(predict.predict(X))})
    print(result.json)

    return result


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)