import requests

locatiod =  [
  "29.7604° N, 95.3698° W", "32.7767° N, 96.7970° W", "30.2672° N, 97.7431° W",
 "41.8781° N, 87.6298° W", "40.7128° N, 74.0060° W", "9.0820° N, 8.6753° E", "31.9686° N, 99.9018° W", "41.6752° N, 60.7598° E", "7.9465° N, 1.0232° W", "29.5636° N, 95.2860° W"
]




url = "https://api.climacell.co/v3/weather/forecast/daily?key=xNV9aYu0PfZTPIXNRn4dzuixUKxYg1kx"

response = requests.request("GET", url)

print(response.text)


[
  {
    "precipitation": [
      {
        "observation_time": "2020-06-30T01:00:00Z",
        "max": {
          "value": 0.6875,
          "units": "mm/hr"
        }
      }
    ],
    "observation_time": {
      "value": "2020-06-29"
    },
    "lat": 42.35544,
    "lon": -71.05991
  }
]
 