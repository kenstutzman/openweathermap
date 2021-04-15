# OpenWeatherMap.org python decode
# JSON Formatted object is as follows:
# {'coord': {'lon': -105.0844, 'lat': 40.5853}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'base': 'stations', 'main': {'temp': 7.74, 'feels_like': -2.07, 'temp_min': 3.2, 'temp_max': 10.99, 'pressure': 1011, 'humidity': 66}, 'visibility': 10000, 'wind': {'speed': 6.15, 'deg': 141}, 'clouds': {'all': 1}, 'dt': 1613416832, 'sys': {'type': 1, 'id': 4120, 'country': 'US', 'sunrise': 1613397230, 'sunset': 1613435720}, 'timezone': -25200, 'id': 5577147, 'name': 'Fort Collins', 'cod': 200}

# importing requests and json
import requests, json
import time
import fourletterphat
from subprocess import Popen, PIPE
import datetime

# base URL
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
#CITY = "Goddard,KS,US"
#CITY = "Windsor,CO,US"
CITY = "Fort&20Collins,CO,US"
UNITS = "imperial"
# upadting the URL
URL = BASE_URL + "q=" + CITY + "&units=" + UNITS + "&appid=" + API_KEY

def main():
    temperature = 0
    winspeed = 0
    windir = " "
    lastmin = 99
    while True:
        now = datetime.datetime.now()
        if now.minute != lastmin :  # if new minute
            lastmin = now.minute
            print(now.minute,lastmin)
            response = requests.get(URL)  #ask for weather from openweathermap 
            if response.status_code == 200:
                data = response.json()
                # print(data) 
                main = data['main']
                temperature = main['temp']
                humidity = main['humidity']
                pressure = main['pressure']
                wind = data['wind']
                windspeed = wind['speed']
                winddeg = wind['deg']
       
                report = data['weather']
                print(f"{CITY:-^30}")
                print(f"Temperature: {temperature}F")
                print(f"Humidity: {humidity}")
                print(f"Pressure: {pressure}")
                print(f"Wind Speed: {windspeed}")
                print(f"Wind Degrees: {winddeg}")
                if winddeg < 45 or winddeg >= 315:
                    print("north")
                    windir = "N"
                if winddeg >= 45 and winddeg < 135:
                    print("east")
                    windir = "E"
                if winddeg >= 135 and winddeg < 225:
                    print("south")
                    windir = "S"
                if winddeg >= 225 and winddeg < 315:
                    print("west")
                    windir = "W"
                print(f"Weather Report: {report[0]['description']}")
            else:
                print("Error in the HTTP request")
          
        fourletterphat.clear()
        tempstring = "{:.0f}F".format(temperature)
        print(now.second,tempstring)
        fourletterphat.print_str(tempstring)
        #fourletterphat.set_decimal(1, 1)
        fourletterphat.show()
 
        time.sleep(4)
            
        fourletterphat.clear()
        tempstring = "{:.0f}{}".format(windspeed,windir)
        print(now.second,tempstring)
        fourletterphat.print_str(tempstring)
        fourletterphat.show()
            
        time.sleep(4)

if __name__ == "__main__":
    main()
