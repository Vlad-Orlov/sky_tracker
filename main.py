import astroplan
import requests, json
from astropy.coordinates import SkyCoord, EarthLocation
from astroplan import Observer, FixedTarget

# Get information about observation location and weather

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
response = requests.get(URL)

if response.status_code == 200:
   data = response.json()
   main = data['main']
   temperature = main['temp']
   humidity = main['humidity']
   pressure = main['pressure']

print(temperature, humidity, pressure)

location = json.load(open('observer_location.json'))
observer_location = EarthLocation.from_geodetic(location['Longtitude'], 
                                                location['Latitude'], 
                                                location['Elevation'])

observer = Observer(name='Subaru Telescope',
               location=observer_location,
               pressure=0.615 * u.bar,
               relative_humidity=0.11,
               temperature=0 * u.deg_C,
               timezone=timezone('US/Hawaii'),
               description="Subaru Telescope on Maunakea, Hawaii")