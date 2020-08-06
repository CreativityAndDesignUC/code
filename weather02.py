import requests, json
from matplotlib import pyplot
  
api_key = 'eb85b0a4df49360254aad7a547a0de9b'

lat = '33.59'
lon = '-10.62'
url = "https://api.openweathermap.org/data/2.5/onecall?lat="+lat+"&lon="+lon+"&appid="+api_key


response = requests.get(url) 
data = response.json()

current_temp = data['current']['temp']
sky = data['current']['weather'][0]['description']

forcast_length = len(data['hourly'])

temperatures = []
for i in range(forcast_length):
    t = data['hourly'][i]['temp']
    temperatures.append(t)
    
mn = min(temperatures)
mx = max(temperatures)  
  
print(temperatures)
pyplot.bar(range(forcast_length), temperatures)
pyplot.ylim([mn-2, mx+2])
pyplot.xlabel('Hours')
pyplot.ylabel('Temperature')
pyplot.show()
