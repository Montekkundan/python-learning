import requests
from twilio.rest import Client

ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = ""
account_sid = ""
auth_token = ""

weather_params = {
    "lat": 30.733315,
    "lon": 76.779419,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_date in weather_slice:
    condition_code = hour_date["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It is going to rain today! Remember to bring an umbrella ☔️",
        from_="",
        to=""
    )
    print(message.status)
