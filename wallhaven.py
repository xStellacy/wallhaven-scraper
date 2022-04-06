import json
import requests
import urllib.request
import re

page = 1
while page < 99:
    print("page" + str(page))
    url = 'https://wallhaven.cc/api/v1/search?q=landscape&categories=111&purity=100&sorting=relevance&order=desc&page=' + str(page)
    imagelist2 = requests.get(url).text
    yes1 = json.loads(imagelist2)
    thing1 = yes1['data']
    j = 0
    while j < len(thing1):
        imagelist = requests.get(url).text
        yes = json.loads(imagelist)
        thing = yes['data'][j]['path']
        imagename1 = re.sub('h.*/', '', thing)
        imagename = str(imagename1)
        image = open('images/'+ imagename, 'wb')
        imagedownload = requests.get(thing)
        image.write(imagedownload.content)
        print(str(j))
        j+=1

