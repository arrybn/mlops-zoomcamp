import pickle
import pandas as pd

with open('web-service/lin_reg.bin', 'rb') as f_in:
    dv, model = pickle.load(f_in)

categorical = ['PULocationID', 'DOLocationID']
numerical = ['trip_distance']


def prepare_features(dicts, features_transform=dv):
    X = features_transform.transform(dicts)

    return X


def read_data(file_uri, categorical_f_names=categorical, numerical_f_names=numerical):
    df = pd.read_parquet(file_uri)

    df[categorical_f_names] = df[categorical_f_names].fillna(-1).astype('int').astype('str')
    
    dicts = df[categorical + numerical_f_names].to_dict(orient='records')
    
    return dicts


def predict(X, model=model):
    y_pred = model.predict(X)

    return y_pred