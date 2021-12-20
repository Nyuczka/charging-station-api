FROM python:3.9.1
ADD . /charging-station-api
WORKDIR /charging-station-api
RUN pip install -r requirements.txt
ENTRYPOINT python ./charging-station-api/app.py