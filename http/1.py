import requests


p = requests.get("https://cataas.com/cat")
out = open("img.jpg", "wb")
out.write(p.content)
out.close()

p = requests.get("https://cataas.com/cat?type=or")
out = open("img.jpg", "wb")
out.write(p.content)
out.close()

p = requests.get("https://cataas.com/cat?filter=pixel")
out = open("img.jpg", "wb")
out.write(p.content)
out.close()
