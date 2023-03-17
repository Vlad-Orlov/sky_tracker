def format_weather_data(temperature, humidity, pressure):
   return (f"Temperature: {temperature} °C\n"
           f"Humidity: {humidity} %\n"
           f"Pressure: {pressure} hPa")

def get_weather_data(location):
   API_KEY = location[WEATHER_API_KEY]
   URL = (f"https://api.openweathermap.org/data/2.5/weather?"
         f"lat={location['Latitude']}&lon={location['Longtitude']}"
         f"&appid={API_KEY}&units=metric")

   response = requests.get(URL)

   if response.status_code == 200:
      main = response.json()['main']
      temperature, humidity, pressure = (main['temp'], main['humidity'], main['pressure'])
      print(format_weather_data(temperature, humidity, pressure))
   else:
      print("Couldn't get weather data from online. Setting dummy values:")
      temperature, humidity, pressure = 5, 80, 1013.25
      print(format_weather_data(temperature, humidity, pressure))

   return (temperature, humidity, pressure)
