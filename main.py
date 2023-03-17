import astroplan
from astropy.time import Time
from pytz import timezone
import json
from astropy.coordinates import SkyCoord, EarthLocation
from astroplan import Observer, FixedTarget
import astropy.units as u
from astropy.units import cds
from datetime import datetime
from weather import get_weather_data, format_weather_data

cds.enable()

# Get information about observation location and weather
location = json.load(open('observer_data.json'))
observer_location = EarthLocation.from_geodetic(lon = location['Longitude'], 
                                                lat = location['Latitude'], 
                                                height = location['Elevation'])

temperature, humidity, pressure = get_weather_data(location)

observer = Observer(name='VORLOV Telescope',
                    location=observer_location,
                    pressure=pressure * u.hPa,
                    relative_humidity=humidity/100.0,
                    temperature=temperature * u.deg_C,
                    timezone=timezone('Europe/Kiev'),
                    description="Telescope of Vladyslav Orlov, Kyiv, Ukraine")

         
object_name = 'Altair'
target_object = FixedTarget.from_name(object_name)
time = Time(datetime.now())

print(observer.target_is_up(time, target_object))

