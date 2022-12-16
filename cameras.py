import json
import requests
import os

q_address = 'https://api.oulunliikenne.fi/proxy/graphql'
query = 'query {cameras {cameraId,name,lat,lon,presets {presetId,presentationName,imageUrl,measuredTime}}}'
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
with open('cameras.json', 'w') as f:
    f.write(json.dumps(response.json(), indent=4))

# Save images

url_list = []

with open('cameras.json') as f:
    data = json.load(f)
    for camera in data['data']['cameras']:
        for preset in camera['presets']:
            url_list.append(preset['imageUrl'])

for url in url_list:
    _, file_path = os.path.split(url)
    if not os.path.exists(file_path):
        response = requests.get(url)

        with open(file_path, 'wb') as f:
            f.write(response.content)
            print(f'Saved {file_path}')
