import requests
res = requests.get('https://wttr.in/{}'.format(input('input the city name:-\n')))
print(res.text)
