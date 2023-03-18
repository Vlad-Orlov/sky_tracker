from astropy import units as u
from astropy.time import Time
from astropy.coordinates import SkyCoord, EarthLocation, AltAz

m42 = SkyCoord.from_name('M42')
print(m42)