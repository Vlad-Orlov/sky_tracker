import astroplan
from astropy.coordinates import Angle
from astropy.time import Time
from pytz import timezone
import json
from astropy.coordinates import AltAz, SkyCoord, EarthLocation
from astroplan import Observer, FixedTarget
import astropy.units as u
from astropy.units import cds
from datetime import datetime
from weather import get_weather_data, format_weather_data

# cds.enable()

# Get information about observation location and weather
location = json.load(open('observer_data.json'))
observer_location = EarthLocation.from_geodetic(location['Longitude'],
                                                location['Latitude'],
                                                location['Elevation'])

temperature, humidity, pressure = get_weather_data(location)

observer_time_zone = timezone('Europe/Kiev')
observer = Observer(name='VORLOV Telescope',
                    location=observer_location,
                    pressure=pressure * u.hPa,
                    relative_humidity=humidity/100.0,
                    temperature=temperature * u.deg_C,
                    timezone=observer_time_zone,
                    description="Telescope of Vladyslav Orlov, Kyiv, Ukraine")

         
object_name = 'Altair'
target_object = FixedTarget.from_name(object_name)
# target_object.
time = Time.now() 
print(time + 2 * u.h, observer.target_is_up(time, target_object))

target_altaz = SkyCoord.from_name(object_name).transform_to(AltAz(obstime=time,location=observer_location))
print(f"{object_name}'s Altitude = {target_altaz.alt:.5}")
print(f"{object_name}'s Azimuth = {target_altaz.az:.5}")
