import requests

location = [(32.965557,-96.715836), (32.907223,-96.635277), (32.705002, -97.122780 ), (30.266666,-97.733330), (32.779167,-96.808891), (29.749907, -95.358421), (31.845682,-102.367645), (26.203407,-98.230011), (	29.691063, -95.209099), (40.931210,-73.898750),]

locationslon =  (  -96.715836,  -96.635277,  -97.122780 ,  -97.733330, -96.808891, -95.358421,  -102.367645,  -98.230011, 	 -95.209099, -73.898750)

locationslad =  ( 32.965557,  32.907223,  32.705002, 30.266666, -97.733330, 32.779167,  29.749907,  31.845682,  26.203407,  	29.691063,  40.931210, )



key = "xNV9aYu0PfZTPIXNRn4dzuixUKxYg1kx"

class location_info:
  def __init__(self, lat, lon):
    self.lat = lat
    self.lon = lon
   

def get_weather_data(list):
  location = []
  for item in list:
    data = location_info(item[0], item[1])
    location.append(data)
    print(location)

get_weather_data(location)


url = "https://api.climacell.co/v3/weather/realtime"
payload = {"apikey": "MlzJxYVk8vU6tjV0U4SNf9WKItn4fTzq", "lat":locationslad[0], "lon":locationslon[1],
"unit_system": "us",
"fields": [
  "precipitation", "temp", "feels_like", "humidity"
]}

response = requests.get(url, params = payload)

print(response.text)



