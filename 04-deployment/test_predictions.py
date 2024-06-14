import predict
import numpy as np

year = 2023
month = 3

data_dicts = predict.read_data(f'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{year}-{month:02}.parquet')

# ride = {'PULocationID': '10', 'DOLocationID': '50', 'trip_distance': 40}

X = predict.prepare_features(data_dicts)

print(np.mean(predict.predict(X)))