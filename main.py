import astroplan
import json
from astropy.coordinates import SkyCoord
from astroplan import Observer, FixedTarget

coordinates = SkyCoord('19h50m47.6s', '+08d52m12.0s', frame='icrs')
altair = FixedTarget(name='Altair', coord=coordinates)


observer_location
observer = Observer.at_site