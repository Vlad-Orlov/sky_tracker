# sky_tracker
GOTO system for my telescope base on Raspberry Pi

## Usage
To start using the existing code, create observer_location.json file with the following structure:
{
    "Latitude": 0.0,
    "Longtitude": 0.0,
    "Elevation": 0.0,
    "WEATHER_API_KEY":"example api_key"
}

Where "Latitude" and "Longtitude" are your geographical coordinates in degrees, "Elevation" -- your elevation above sea level (in meters), WEATHER_API_KEY -- api key to openweathermap.org (need to register on the website to get it.
