FROM agrigorev/zoomcamp-model:mlops-2024-3.10.13-slim

RUN pip install -U pip
RUN pip install pipenv

WORKDIR /app

COPY ["web-service/Pipfile", "web-service/Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["flask_app.py", "predict.py", "./"]

RUN mkdir -p web-service

RUN ln -sf /app/model.bin /app/web-service/lin_reg.bin

EXPOSE 9696

ENTRYPOINT [ "gunicorn", "--bind=0.0.0.0:9696", "flask_app:app" ]

