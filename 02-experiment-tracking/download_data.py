from time import strptime
import urllib.request
from pathlib import Path
import os

if __name__ == '__main__':
    data_folder = 'data'
    url_template = 'https://d37ci6vzurychx.cloudfront.net/trip-data/{0}_tripdata_{1}-{2}.parquet'

    taxi_type = 'green'
    year = 2023
    months = ['Jan', 'Feb', 'Mar']

    os.makedirs(data_folder, exist_ok=True)

    for m in months:
        month = f"{strptime(m,'%b').tm_mon:02}"
        url = url_template.format(taxi_type, year, month)

        urllib.request.urlretrieve(url, Path(data_folder) / url.split('/')[-1])


