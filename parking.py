import json
import requests
import os
import time


def start():
    q_address = 'https://api.oulunliikenne.fi/proxy/graphql'
    query = 'query GetAllCarParks {carParks {carParkId,name,lat,lon,maxCapacity,spacesAvailable}}'
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
    with open('parking.json', 'w') as f:
        f.write(json.dumps(response.json(), indent=4))

    value_list = []

    with open('parking.json') as f:
        data = json.load(f)
        for carPark in data['data']['carParks']:
            values = {'name': carPark['name'], 'maxCapacity': carPark['maxCapacity'],
                      'spacesAvailable': carPark['spacesAvailable']}
            value_list.append(values)

    for i in value_list:
        print(i)


if __name__ == '__main__':
    start()
