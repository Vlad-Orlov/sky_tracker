import astroplan
from astropy.time import Time
from pytz import timezone
import requests, json
from astropy.coordinates import SkyCoord, EarthLocation
from astroplan import Observer, FixedTarget
import astropy.units as u
from astropy.units import cds
from datetime import datetime
cds.enable()

def format_weather_data(temperature, humidity, pressure):
   return (f"Temperature: {temperature} °C\n"
           f"Humidity: {humidity} %\n"
           f"Pressure: {pressure} hPa")

# Get information about observation location and weather
location = json.load(open('observer_location.json'))
observer_location = EarthLocation.from_geodetic(location['Longtitude'], 
                                                location['Latitude'], 
                                                location['Elevation'])

API_KEY = location['WEATHER_API_KEY']
URL = (f"https://api.openweathermap.org/data/2.5/weather?"
       f"lat={location['Latitude']}&lon={location['Longtitude']}"
       f"&appid={API_KEY}&units=metric")

response = requests.get(URL)

if response.status_code == 200:
   data = response.json()
   main = data['main']
   temperature, humidity, pressure = (main['temp'], main['humidity'], main['pressure'])
   print(format_weather_data(temperature, humidity, pressure))
else:
   print("Couldn't get weather data from online. Setting dummy values:")
   temperature, humidity, pressure = 5, 80, 1013.25
   print(format_weather_data(temperature, humidity, pressure))

observer = Observer(name='VORLOV Telescope',
               location=observer_location,
               pressure=pressure * u.hPa,
               relative_humidity=humidity/100,
               temperature=temperature * u.deg_C,
               timezone=timezone('Europe/Kiev'),
               description="Telescope of Vladyslav Orlov, Kyiv, Ukraine")

         
object_name = 'Altair'
target_object = FixedTarget.from_name(object_name)
time = Time(datetime.now())

