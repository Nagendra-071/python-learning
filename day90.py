import requests
import json
query=input("WHat type of news are you interested in ?  ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2026-05-07&sortBy=publishedAt&apiKey=e26e1ad2a5fd439fa2f2bb3079701e4a"
r=requests.get(url)
# print(r.text)
news=json.loads(r.text)
# print(news,type(news))

for article in news["articles"]:
    n=int(input ("Enter nuber of news you want ?  "))
    while(n!=0):
        print(article["title"])
        print(article["description"])
        print("----------------------------------------------------------------------------------")
        n-=1
    
    if(n==0) :break
    
    