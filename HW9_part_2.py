import requests

auth = {'Authorization': 'OAuth (мой токен)'}

new_file1 = 'hw9.txt'
with open(new_file1, encoding='utf8') as f:
    file = f.read()
#print(file)

bucket = requests.get('https://cloud-api.yandex.net:443/v1/disk/resources/upload?path=/{file}', headers=auth)
print(bucket.json())

href = bucket.json()['href']

print(href)

push_file = requests.put(href, data=file)

print(push_file.text)