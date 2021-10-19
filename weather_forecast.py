import requests
print(requests.get('https://wttr.in/{}'.format(input('input the city name:-\n'))).text)
