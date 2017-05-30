import  requests

page = requests.get("https://www.google.ru")
html1 = page.text
img = html1.split("<img ")[1]
img1 = img.split('src="')[1]
img1 = img1.split('" title="')

if len(img1) > 1:
    img1 = img1[0]
    rsh = img1.split(".")
    rsh = rsh[len(rsh)-1]
    img1 = "http://www.google.ru" + img1 
    print(img1)
    name = "img." + rsh
    p = requests.get(img1)
    out = open(name, "wb")
    out.write(p.content)
    out.close()

import tweepy
auth = tweepy.OAuthHandler("***", "***")
auth.set_access_token("***", "***")

api = tweepy.API(auth)
api.update_with_media("img.gif", "First post")
