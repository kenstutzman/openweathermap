# OpenWeatherMap.org python decode
# JSON Formatted object is as follows:
# {'coord': {'lon': -105.0844, 'lat': 40.5853}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'base': 'stations', 'main': {'temp': 7.74, 'feels_like': -2.07, 'temp_min': 3.2, 'temp_max': 10.99, 'pressure': 1011, 'humidity': 66}, 'visibility': 10000, 'wind': {'speed': 6.15, 'deg': 141}, 'clouds': {'all': 1}, 'dt': 1613416832, 'sys': {'type': 1, 'id': 4120, 'country': 'US', 'sunrise': 1613397230, 'sunset': 1613435720}, 'timezone': -25200, 'id': 5577147, 'name': 'Fort Collins', 'cod': 200}

# importing requests and json
import requests, json
# base URL
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
#CITY = "Goddard,KS,US"
CITY = "Windsor,CO,US"
UNITS = "imperial"
API_KEY = ""
# upadting the URL
URL = BASE_URL + "q=" + CITY + "&units=" + UNITS + "&appid=" + API_KEY
# HTTP request
response = requests.get(URL)
# checking the status code of the request
if response.status_code == 200:
   # getting data in the json format
   data = response.json()
   print(data)
   # getting the main dict block
   main = data['main']
   # getting temperature
   temperature = main['temp']
   # getting the humidity
   humidity = main['humidity']
   # getting the pressure
   pressure = main['pressure']
   # wind speed
   wind = data['wind']
   windspeed = wind['speed']
   winddeg = wind['deg']

   # weather report
   report = data['weather']
   print(f"{CITY:-^30}")
   print(f"Temperature: {temperature}F")
   print(f"Humidity: {humidity}")
   print(f"Pressure: {pressure}")
   print(f"Wind Speed: {windspeed}")
   print(f"Wind Degrees: {winddeg}")
   if winddeg < 45 or winddeg >= 315:
     print("north")
   if winddeg >= 45 and winddeg < 135:
     print("east")
   if winddeg >= 135 and winddeg < 225:
     print("south")
   if winddeg >= 225 and winddeg < 315:
     print("west")
   print(f"Weather Report: {report[0]['description']}")
else:
   # showing the error message
   print("Error in the HTTP request")