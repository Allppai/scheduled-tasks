import requests
import os
from twilio.rest import Client

timestamp_list = []

MY_LAT = 52.7391137102
MY_LONG = -3.883579799

my_phone = os.environ.get("MY_PHONE")
twilio_phone = os.environ.get("TWILIO_PHONE")

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

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
        from_=twilio_phone,
        to=my_phone,
    )
    print(message.status)
