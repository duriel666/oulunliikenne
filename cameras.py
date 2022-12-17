import json
import requests
import os
import time


total_images = 0
total_size = 0
run_time = time.time()


def start():
    global total_images
    global total_size
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

    url_list = []

    with open('cameras.json') as f:
        data = json.load(f)
        for camera in data['data']['cameras']:
            for preset in camera['presets']:
                url_list.append(preset['imageUrl'])

    subfolder = 'images'
    if not os.path.exists(subfolder):
        os.mkdir(subfolder)

    run = True

    while run:
        saved = 0
        start_time = time.time()

        for url in url_list:
            _, file = os.path.split(url)
            response = requests.get(url)
            current_time = time.strftime('%Y%m%d%H%M%S', time.localtime())
            name = file.split('.')[0]+'_'+current_time+'.'+file.split('.')[1]

            folder = subfolder+'/'+file.split('.')[0]

            if not os.path.exists(folder):
                os.mkdir(folder)

            file_path = os.path.join(folder, name)

            files = os.listdir(folder)
            files.sort(key=lambda x: os.path.getmtime(os.path.join(folder, x)))
            if len(files) > 0:
                last_file_path = os.path.join(folder, files[-1])
                last_file_size = os.path.getsize(last_file_path)
                if len(files) > 1:
                    last_file2_path = os.path.join(folder, files[-2])
                    last_file2_size = os.path.getsize(last_file2_path)
                else:
                    last_file2_size = 0
            else:
                last_file_size = 0
                last_file2_size = 0

            try:
                file_size = int(response.headers['Content-Length'])
                if last_file_size != file_size and last_file2_size != file_size:
                    with open(file_path, 'wb') as f:
                        f.write(response.content)
                        saved += 1
                        total_images += 1
                        total_size += file_size
                        print(
                            f'Saved \"{file_path}\" {file_size/1024:.0f} kb - {len(files)+1} files in folder \"{folder}\"')
                else:
                    print(
                        f'File \"{file_path}\" already downloaded - {len(files)} files in folder \"{folder}\"')
            except:
                pass

        print(f'\tSaved {saved} files in {time.time()-start_time:.2f} seconds')
        print(
            f'Total images downloaded this session {total_images} - {total_size/1024/1024:.2f} Mb')
        print(
            f'Total running time this session {time.time()-run_time:.2f} seconds')
        # tarkista tiedostojen määrä hakemistoista
        countdown(120)


def countdown(num):
    for i in range(num):
        print(f'\tWaiting {num-i-1} seconds     ', end='\r')
        time.sleep(1)
    print('\n\tContinuing...     ')


if __name__ == '__main__':
    start()
