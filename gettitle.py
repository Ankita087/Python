# import requests 
# url = 'https://www.google.com/'
# r = requests.post(url)
# print r
# import requests
# r = requests.get("https://www.google.com/")
# print(r.json())

import requests

from lxml.html import fromstring
list = ["https://www.google.com", "https://www.w3schools.com", "https://www.youtube.com/"]
for link in list:
    r = requests.get(link)
    c =  r.headers["Content-Encoding"]
    title = fromstring(r.content)
    print(title.findtext('.//title'))
