'''if not os.path.exists(file) or os.path.getsize(file) == int(url.headers['Content-Length']):
    response = requests.get(url)
    with open(file, 'wb') as f:
        f.write(response.content)
        print(f'Saved {file}')'''

'''import os

folder_path = "folder"

files = os.listdir(folder_path)
files.sort(key=lambda x: os.path.getmtime(os.path.join(folder_path, x)))
last_file_path = os.path.join(folder_path, files[-1])
last_file_size = os.path.getsize(last_file_path)
if last_file_size != int(url.headers['Content-Length'])):'''