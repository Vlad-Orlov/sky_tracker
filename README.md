# sky_tracker
GOTO system for my telescope based on Raspberry Pi

## Usage
For the initial setup, create ```observer_data.json``` file with the following structure:
```json
{
    "Latitude": 0.0,
    "Longtitude": 0.0,
    "Elevation": 0.0,
    "WEATHER_API_KEY":"example api_key"
}
```
Where ```"Latitude"``` and ```"Longtitude"``` are your geographical coordinates in degrees, ```"Elevation"``` - your elevation above sea level (in meters), ```"WEATHER_API_KEY"``` - api key to [openweathermap.org](https://openweathermap.org) (need to register on the website to get it).
