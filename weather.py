import json
import requests
import os
import time


def start():
    q_address = 'https://api.oulunliikenne.fi/proxy/graphql'
    query = 'query GetAllWeatherStations {weatherStations {weatherStationId,name,lat,lon,collectionStatus,measuredTime,sensorValues {roadStationId,name,sensorValue,sensorUnit}}}'
    variables = {}

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    body = {
        'query': query,
        'variables': variables
    }

    response = requests.post(q_address, json=body, headers=headers)
    with open('weather.json', 'w') as f:
        f.write(json.dumps(response.json(), indent=4))

    value_list = []

    with open('weather.json') as f:
        data = json.load(f)
        for weather in data['data']['weatherStations']:
            for sensorValues in weather['sensorValues']:
                values = {'roadStationId': sensorValues['roadStationId'],
                          'name': sensorValues['name'], 'sensorValue': sensorValues['sensorValue']}
                value_list.append(values)
    '''{
    "data": {
        "weatherStations": [
            {
                "weatherStationId": "15010",
                "name": "TEST_st833_Oulu_Vesala_Lumi",
                "lat": 65.031926,
                "lon": 26.058409,
                "collectionStatus": "GATHERING",
                "measuredTime": "2022-12-18T02:57:00Z",
                "sensorValues": [
                    {
                        "roadStationId": 15010,
                        "name": "SADE",
                        "sensorValue": 0,
                        "sensorUnit": "///"
                    },'''

    for i in value_list:
        print(i)


if __name__ == '__main__':
    start()
