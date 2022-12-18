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
        for tmsStation in data['data']['tmsStations']:
            for sensorValues in tmsStation['sensorValues']:
                values = {'roadStationId': sensorValues['roadStationId'],
                          'name': sensorValues['name'], 'sensorValue': sensorValues['sensorValue']}
                value_list.append(values)
    '''{
    "data": {
        "tmsStations": [
            {
                "tmsStationId": "21201",
                "name": "vt4_Oulu_Inti\u00f6_LML",
                "lat": 65.020043,
                "lon": 25.508104,
                "collectionStatus": "GATHERING",
                "measuredTime": "2022-12-18T02:14:53Z",
                "sensorValues": [
                    {
                        "roadStationId": 21201,
                        "name": "KESKINOPEUS_60MIN_KIINTEA_SUUNTA1",
                        "sensorValue": 100,
                        "sensorUnit": "km/h"
                    },'''
    for i in value_list:
        print(i)


if __name__ == '__main__':
    start()
