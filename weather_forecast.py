import requests
city = input('input the city name:-\n')
url = 'https://wttr.in/{}'.format(city)
res = requests.get(url)
print(res.text)
