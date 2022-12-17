import json
import requests
import os
import time

# lam = liikenteen automaattinen mittaus


def start():
    q_address = 'https://api.oulunliikenne.fi/proxy/graphql'
    query = 'query {tmsStations {tmsStationId,name,lat,lon,collectionStatus,measuredTime,sensorValues {roadStationId,name,sensorValue,sensorUnit}}}'
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
    with open('lam.json', 'w') as f:
        f.write(json.dumps(response.json(), indent=4))

    value_list = []

    with open('lam.json') as f:
        data = json.load(f)
        for tmsStationId in data['data']['tmsStations']:
            for sensorValues in tmsStationId['sensorValues']:
                values = {'roadStationId': sensorValues['roadStationId'],
                          'name': sensorValues['name'], 'sensorValue': sensorValues['sensorValues']}
                value_list.append(values)


if __name__ == '__main__':
    start()
