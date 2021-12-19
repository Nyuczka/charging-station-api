from flask import Flask, request
import requests

app = Flask(__name__)
url = "http://localhost:8080/api/charging-events"


@app.route('/api/station', methods=['GET'])
def get_events_for_station_with_limit():
    station_name = request.args.get('stationName')
    limit = request.args.get('limit')
    session = requests.session()
    response = session.get(url=url, auth=('user', 'password'), params={'stationName': station_name,
                                                                       'limit': limit})

    return response.json()


@app.route('/api/<string:user_id>', methods=['GET'])
def get_events_for_user_and_limit(user_id):
    min_energy = request.args.get('minEnergy')
    max_energy = request.args.get('maxEnergy')
    session = requests.session()
    response = session.get(url=url + '/' + user_id, auth=('user', 'password'), params={'minEnergy': min_energy,
                                                                                       'maxEnergy': max_energy})
    return response.json()


@app.route('/api/avg/energy/user', methods=['GET'])
def get_avg_energy_for_user():
    session = requests.session()
    response = session.get(url=url + '/average-energy-per-user', auth=('user', 'password'))
    return response.json()


@app.route('/api/avg-energy', methods=['GET'])
def get_average_energy():
    session = requests.session()
    response = session.get(url=url+'/average-energy', auth=('user', 'password'))
    return response.json()


@app.route('/api/max-energy', methods=['GET'])
def get_users_with_max_energy():
    start_date = request.args.get('startDate')
    end_date = request.args.get('endDate')
    session = requests.session()
    response = session.get(url=url + '/max-energy', auth=('user', 'password'), params={'startDate': start_date,
                                                                                       'endDate': end_date})
    return response.json()


@app.route('/add-entry', methods=['POST'])
def add_entry():
    data = request.get_json()
    session = requests.session()
    response = session.post(url=url + '/add-entry', auth=('user', 'password'), data=data)

    return response.status_code


if __name__ == '__main__':
    app.run()
