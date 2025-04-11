import requests
from bs4 import BeautifulSoup
import re

cat = (
    ""
    , "categories/domestic"
    , "categories/world"
    , "categories/business"
    , "categories/entertainment"
    , "categories/sports"
    , "categories/it"
    , "categories/science"
    , "categories/local"
    , "categories/life"
    )

class Scraper:

    def __init__(self, site):
        self.site = site
        print("----------------------------", self.site, "----------------------------------")

    def scrape_pickup(self):

        res = requests.get(self.site)
        scrp = BeautifulSoup(res.text, "html.parser")

        counter = 0
        for topics in scrp.find_all(href = re.compile("news.yahoo.co.jp/pickup")):
#            print(topics,"\n\n")
#            for topic in topics:
            if counter < 8:
                print(topics.contents[0], "\n\n=========", topics.attrs['href'], "\n\n\n")
                counter += 1

        self.scrape_top(scrp)

    def scrape_expert(self):

        res = requests.get(self.site)
        scrp = BeautifulSoup(res.text, "html.parser")

        for topics in scrp.find_all(href = re.compile("https://news.yahoo.co.jp/expert/articles")):
                print(topics.contents[0], ">>", topics.attrs['href'], "\n\\n")

        self.scrape_top(scrp)

    def scrape_top(self,scrp):
        print("=====TOP-rated Articles==============================================")
        for topics in scrp.find_all(href = re.compile("news.yahoo.co.jp/articles")):
            topic = topics.find("p")
            print(topic.text, ">>", topics.attrs['href'], "\n\n")

news = "https://news.yahoo.co.jp/"
#news = "https://news.google.com"

for ca in cat:
    if ca != "categories/life":
        Scraper(news+ca).scrape_pickup()
    else:
        Scraper(news+ca).scrape_expert()
