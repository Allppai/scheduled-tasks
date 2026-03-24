import requests
import os
from twilio.rest import Client

timestamp_list = []

MY_LAT = 57.50584
MY_LONG = -1.79806


my_phone = "+48785470298"
twilio_phone = "+15672294410"

account_sid = "AC18e63bfaefece9bcef93aea0a05079be"
auth_token = "da559487379f0705ea6f1ddf43331bb7"

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "0cce284ec4c36aa5f7d1df8fc8a5e010"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": 4
}


response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()

for timestamp in weather_data["list"]:
    print(timestamp["weather"][0]["id"])
    timestamp_list.append(timestamp["weather"][0]["id"])

if any(weather_id < 700 for weather_id in timestamp_list):
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It's going to rain! Take umbrella.",
        from_="+15672294410",
        to="+48785470298",
    )
    print(message.status)



