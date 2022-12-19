import json
import requests
import os
import time


def weather_start():
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

    # Tarvii vielä lisäksi paikkojen nimet jne jne

    with open('weather.json') as f:
        data = json.load(f)
        for weather in data['data']['weatherStations']:
            for sensorValues in weather['sensorValues']:
                values = {'roadStationId': sensorValues['roadStationId'],
                          'name': sensorValues['name'], 'sensorValue': sensorValues['sensorValue']}
                value_list.append(values)

    for i in value_list:
        print(
            f'{i["roadStationId"]} - {i["name"]} - Value: {i["sensorValue"]}')


if __name__ == '__main__':
    weather_start()
