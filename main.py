import astroplan
from pytz import timezone
import requests, json
from astropy.coordinates import SkyCoord, EarthLocation
from astroplan import Observer, FixedTarget
import astropy.units as u
from astropy.units import cds
cds.enable()
# Get information about observation location and weather


location = json.load(open('observer_location.json'))
observer_location = EarthLocation.from_geodetic(location['Longtitude'], 
                                                location['Latitude'], 
                                                location['Elevation'])

API_KEY = "76b21e0bf8ed80be297c0b937f476a65"
URL = (f"https://api.openweathermap.org/data/2.5/weather?"
       f"lat={location['Latitude']}&lon={location['Longtitude']}"
       f"&appid={API_KEY}&units=metric")

print(URL)
response = requests.get(URL)

if response.status_code == 200:
   data = response.json()
   main = data['main']
   temperature = main['temp']
   humidity = main['humidity']
   pressure = main['pressure']

print(temperature, humidity, pressure)

observer = Observer(name='VORLOV Telescope',
               location=observer_location,
               pressure=pressure * cds.mmHg,
               relative_humidity=humidity/100,
               temperature=temperature * u.deg_C,
               timezone=timezone('Europe/Kiev'),
               description="Telescope of Vladyslav Orlov, Kyiv, Ukraine")