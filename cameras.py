import json
import requests
import os
import time

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


def countdown(num):
    for i in range(num):
        print(f'\tWaiting {num-i} seconds', end='\r')
        time.sleep(1)
    print('\tContinuing...')

# Save images


url_list = []

with open('cameras.json') as f:
    data = json.load(f)
    for camera in data['data']['cameras']:
        for preset in camera['presets']:
            url_list.append(preset['imageUrl'])

if not os.path.exists('images'):
    for url in url_list:
        _, file = os.path.split(url)
        response = requests.get(url)
        current_time = time.strftime('%Y%m%d%H%M%S', time.localtime())
        name = file.split('.')[0]+'_'+current_time+'.'+file.split('.')[1]
        folder = 'images/'+file.split('.')[0]

        if not os.path.exists(folder):
            os.mkdir(folder)

        file_path = os.path.join(folder, name)
        with open(file_path, 'wb') as f:
            f.write(response.content)
            print(f'Saved {file_path}')

countdown(10)

run = True
while run:
    for url in url_list:
        _, file = os.path.split(url)
        response = requests.get(url)
        current_time = time.strftime('%Y%m%d%H%M%S', time.localtime())
        name = file.split('.')[0]+'_'+current_time+'.'+file.split('.')[1]
        folder = 'images/'+file.split('.')[0]

        if not os.path.exists(folder):
            os.mkdir(folder)

        file_path = os.path.join(folder, name)

        files = os.listdir(folder)
        files.sort(key=lambda x: os.path.getmtime(os.path.join(folder, x)))
        last_file_path = os.path.join(folder, files[-1])
        last_file_size = os.path.getsize(last_file_path)

        try:
            if not last_file_size == int(response.headers['Content-Length']):
                with open(file_path, 'wb') as f:
                    f.write(response.content)
                    print(f'Saved {file_path}')
            else:
                print(f'File {file_path} already downloaded')
        except:
            pass

    countdown(10)
