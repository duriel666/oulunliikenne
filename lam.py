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

    '''url_list = []

    with open('cameras.json') as f:
        data = json.load(f)
        for camera in data['data']['cameras']:
            for preset in camera['presets']:
                url_list.append(preset['imageUrl'])'''


if __name__ == '__main__':
    start()
