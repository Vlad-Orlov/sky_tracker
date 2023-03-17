import astroplan
from astropy.coordinates import Angle
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
lon, lat = (Angle(location['Longitude'] * u.deg), Angle(location['Latitude'] * u.deg))
print(lon, lat) 
observer_location = EarthLocation.from_geodetic(lon=lon, lat=lat, 
                                                height = location['Elevation'] * u.m)

print(observer_location)
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
print(target_object)
# print(observer.target_is_up(time, target_object))

