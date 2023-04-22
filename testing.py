import requests
via=requests.get("https://www.flickr.com/services/rest/?method=flickr.photos.getPopular&api_key=2f989b5fafa5bed68188fedba3791d86&user_id=198158351%40N03&format=json&nojsoncallback=1")
print(via.status_code)
print(via.json())