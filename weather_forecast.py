import requests
url = 'https://wttr.in/{}'.format(input('input the city name:-\n'))
res = requests.get(url)
print(res.text)
