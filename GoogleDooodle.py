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
auth = tweepy.OAuthHandler("K6tD9wK0LYx0sZzcYIf7Tv2R4", "SqyO48bhcTq1tr8GrI7OfohW61NCFDQBkHlzx5S5ADP6iXd5Ij")
auth.set_access_token("2455218148-kGjjj9ny273xybc2yk2DLwIHbsgfuRTv6MtHJbX", "CKrVxEjRFaLwitz3ri7O500I3Fh3WkXz9zpm7Xazphwlr")

api = tweepy.API(auth)
api.update_with_media("img.gif", "First post")
