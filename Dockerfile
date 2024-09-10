FROM tensorflow/tensorflow:2.17.0
WORKDIR /prod

COPY requirements.txt /prod
RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y python3-opencv

COPY ai_weeder_package ai_weeder_package

COPY models models
COPY setup.py setup.py
COPY README.md README.md

CMD uvicorn ai_weeder_package.api.api:app --host 0.0.0.0 --port $PORT
