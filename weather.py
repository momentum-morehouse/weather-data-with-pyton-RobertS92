import requests

location = [ { (32.965557, -96.715836), (32.907223, -96.635277), (32.705002, -97.122780 ), (30.266666, -97.733330), (32.779167, -96.808891), (29.749907, -95.358421), (31.845682, -102.367645), (26.203407, -98.230011), (	29.691063, -95.209099), (40.931210, -73.898750)
}]


url = "https://api.climacell.co/v3/weather/forecast/daily"

response = requests.request("GET", url)

print(response.text)


[
  {
    "precipitation": [
      {
        "observation_time": "2020-06-30T22:00:00Z",
        "max": {
          "value": 0.0295,
          "units": "in/hr"
        }
      }
    ],
    "observation_time": {
      "value": "2020-06-30"
    },
    "lat": 42.35544,
    "lon": -71.05991
  },
  {
    "precipitation": [
      {
        "observation_time": "2020-07-01T19:00:00Z",
        "max": {
          "value": 0.0517,
          "units": "in/hr"
        }
      }
    ],
    "observation_time": {
      "value": "2020-07-01"
    },
    "lat": 42.35544,
    "lon": -71.05991
  }
]

 
