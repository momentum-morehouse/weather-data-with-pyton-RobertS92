import requests

location = [ (30.2672, 97.7431),(41.8781, 87.6298), (40.7128, 74.0060), (9.0820, 8.6753,) (31.9686, 99.9018), (41.6752, 60.7598), (7.9465, 1.0232), (29.5636, 95.2860)
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
 