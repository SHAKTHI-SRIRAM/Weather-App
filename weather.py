import requests, json
import playsound
import random
from gtts import gTTS
import os
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
CITY = 'Arcot'
API_KEY = '602b76e14eaa815c5f0a6c26b0afb70f'
URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
response = requests.get(URL)
def speak(text):

    tts= gTTS(text = text, lang = 'en', slow=False)
    r = random.randint(1,10)
    ado_file = f'ado_1- {str(r)} .mp3'
    tts.save(ado_file)
    playsound.playsound(ado_file)
    os.remove(ado_file)
def today_weather():
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        temperature = main['temp']
        humidity = main['humidity']
        pressure = main['pressure']
        report = data['weather']
        speak(f"Temperature: {temperature}")
        speak(f"Humidity in your area is {humidity}")
        speal(f"Air pressure in your area is {pressure}")
        speak(f"today it will be {report[0]} in your area")
    else:
        speak('Sorry my Network is too poor')

today_weather()
