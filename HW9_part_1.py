import requests

responce_hulk = requests.get('https://superheroapi.com/api.php/2619421814940190/search/hulk')

#print(responce_hulk.json()['results'][0]['powerstats']['intelligence'])

responce_ca = requests.get('https://superheroapi.com/api.php/2619421814940190/149')

#print(responce_ca.json()['powerstats']['intelligence'])

responce_thanos = requests.get('https://superheroapi.com/api.php/2619421814940190/search/thanos')

#print(responce_thanos.json()['results'][0]['powerstats']['intelligence'])

#hulk_intelligence = responce_hulk.json()['results'][0]['powerstats']['intelligence']
#ca_intelligence = responce_ca.json()['powerstats']['intelligence']
#thanos = responce_thanos.json()['results'][0]['powerstats']['intelligence']

#hulk_dict = {}
#hulk_dict[responce_hulk.json()['results-for']] = responce_hulk.json()['results'][0]['powerstats']['intelligence']
#ca_dict = {}
#ca_dict[responce_ca.json()['name']] = responce_ca.json()['powerstats']['intelligence']
#thanos_dict = {}
#thanos_dict[responce_thanos.json()['results-for']] = responce_thanos.json()['results'][0]['powerstats']['intelligence']

super_dict = {}
super_dict[responce_hulk.json()['results-for']] = responce_hulk.json()['results'][0]['powerstats']['intelligence']
super_dict[responce_ca.json()['name']] = responce_ca.json()['powerstats']['intelligence']
super_dict[responce_thanos.json()['results-for']] = responce_thanos.json()['results'][0]['powerstats']['intelligence']
#print(super_dict)
#super_hero = max(super_dict, key = lambda k: super_dict[k])
#print(f'{super_hero} {super_dict[super_hero]}')

print(f'Самый умный супер герой - {max(super_dict)} с интеллектом {max(super_dict.values())}')

