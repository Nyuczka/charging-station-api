from flask import Flask, request
import requests

app = Flask(__name__)
login_url = "http://localhost:8080/login"
api_url = 'http://localhost:8080/api/charging-events'


@app.route('/login', methods=['POST'])
def login():
    request_data = request.get_json()
    response = requests.post(url=login_url, json=request_data)
    return response.json()


@app.route('/api/station', methods=['GET'])
def get_events_for_station_with_limit():
    station_name = request.args.get('stationName')
    limit = request.args.get('limit')
    session = requests.session()
    response = session.get(url=api_url, params={'stationName': station_name,
                                                'limit': limit}, headers=request.headers)

    return response.json()


@app.route('/api/<string:user_id>', methods=['GET'])
def get_events_for_user_and_limit(user_id):
    min_energy = request.args.get('minEnergy')
    max_energy = request.args.get('maxEnergy')
    session = requests.session()
    response = session.get(url=api_url + '/' + user_id, params={'minEnergy': min_energy,
                                                                'maxEnergy': max_energy}, headers=request.headers)
    return response.json()


@app.route('/api/avg/energy/user', methods=['GET'])
def get_avg_energy_for_user():
    session = requests.session()
    response = session.get(url=api_url + '/average-energy-per-user', headers=request.headers)
    return response.json()


@app.route('/api/avg-energy', methods=['GET'])
def get_average_energy():
    session = requests.session()
    response = session.get(url=api_url + '/average-energy', headers=request.headers)
    return response.json()


@app.route('/api/max-energy', methods=['GET'])
def get_users_with_max_energy():
    start_date = request.args.get('startDate')
    end_date = request.args.get('endDate')
    session = requests.session()
    response = session.get(url=api_url + '/max-energy', params={'startDate': start_date,
                                                                'endDate': end_date}, headers=request.headers)
    return response.json()


@app.route('/add-entry', methods=['POST'])
def add_entry():
    data = request.get_json()
    session = requests.session()
    response = session.post(url=api_url + '/add-entry', json=data, headers=request.headers)

    return response.status_code


if __name__ == '__main__':
    app.run()
