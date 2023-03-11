import requests


p = requests.get("https://cataas.com/cat/says/hello%20world!")
out = open("img.jpg", "wb")
out.write(p.content)
out.close()
