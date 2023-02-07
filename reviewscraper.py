from audioop import reverse
from operator import truediv
import this
import requests
from bs4 import BeautifulSoup
from pathlib import Path
from selenium import webdriver

class Scrap():
    def __init__(self) -> None:
        pass

    class Review:

        def __init__(self,text):
            self.review_text = text
            self.review_star = ""
            pass

        def add_star(self,star):
            self.review_star = star

    HEADER = ({'User-Agent':
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
                'Accept-Language': 'en-US, en;q=0.5'})

    #get the html from the webste
    def getdata(url):
        r = requests.get(url,headers= Scrap.HEADER)
        return r.text

    #search through the parsed data and pull out the review text
    #returns a list of review classes with the text and star of each review
    def parsedata(self,soup):
        review_list = []
        review_stars = []
        review_stars_tmp = []
        data_str = ""

        #get the review text
        for item in soup.find_all("div",class_="a-expander-content reviewText review-text-content a-expander-partial-collapse-content"):
            review_list.append(item.get_text())

        #get the review stars
        for item in soup.find_all(attrs={"data-hook": "review-star-rating"}):
            review_stars_tmp.append(item.get_text())
          
        for item in review_stars_tmp:
            tmp = item.split(" ")
            review_stars.append(tmp[0])

        #combine the two lists into a dictionay keyed on stars
        combined = zip(review_stars,review_list)
        return tuple(combined)

    #function that returns a pruned list of reviews for only the correct stars
    def prunereviews(self,review_list,stars):
        pruned_list = []

        #sort the list in reverse so that the largest are at the front
        review_list.sort(key=lambda x: x.review_stars, reverse = True)

        for reviews in review_list:
            if reviews.review_stars == stars:
                pruned_list.append(reviews)

        return pruned_list

    #put the html into the Beautiful Soup parser and get out the reviews with the correct stars
    def html_code(self,url):

        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument("--lang=en")

        browser = webdriver.Chrome("chromedriver.exe",options=options,)
        browser.get(url)

        soup = BeautifulSoup(browser.page_source,'html.parser')
        reviews = self.parsedata(soup)
        #pruned_reviews = self.prunereviews(reviews,5)
        return reviews
        

#s = Scrap()
    #URL = "https://www.google.com/search?q=ups%20store%20huntsville%20alabama&rlz=1C1MKDC_enUS856US856&oq=up&aqs=chrome.0.69i59j69i57j46i199i291i433i512j0i433i512j46i199i291i433i512j0i433i512j69i61l2.860j0j7&sourceid=chrome&ie=UTF-8&tbs=lf:1,lf_ui:4&tbm=lcl&rflfq=1&num=10&rldimm=8478361796219820579&lqi=Chx1cHMgc3RvcmUgaHVudHN2aWxsZSBhbGFiYW1hIgOIAQFIz-XOleaAgIAIWjIQABABGAAYARgCGAMiHHVwcyBzdG9yZSBodW50c3ZpbGxlIGFsYWJhbWEqBggCEAAQAZIBHHNoaXBwaW5nX2FuZF9tYWlsaW5nX3NlcnZpY2WaASNDaFpEU1VoTk1HOW5TMFZKUTBGblNVTkpNelppVEVwQkVBRaoBERABKg0iCXVwcyBzdG9yZSgA&ved=2ahUKEwjPx4ap2rf2AhWEVN8KHchOAgQQvS56BAgCEE0&rlst=f#rlfi=hd:;si:8478361796219820579,l,Chx1cHMgc3RvcmUgaHVudHN2aWxsZSBhbGFiYW1hIgOIAQFIz-XOleaAgIAIWjIQABABGAAYARgCGAMiHHVwcyBzdG9yZSBodW50c3ZpbGxlIGFsYWJhbWEqBggCEAAQAZIBHHNoaXBwaW5nX2FuZF9tYWlsaW5nX3NlcnZpY2WaASNDaFpEU1VoTk1HOW5TMFZKUTBGblNVTkpNelppVEVwQkVBRaoBERABKg0iCXVwcyBzdG9yZSgA;mv:[[34.8281121,-86.4785579],[34.6188113,-86.7321992]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!2m1!1e3!3sIAE,lf:1,lf_ui:4"
#s.html_code("https://www.amazon.com/Streamlight-75636-Flashlight/dp/B003TODYU2/ref=sr_1_12?keywords=flashlights&qid=1646865764&sprefix=flashl%2Caps%2C129&sr=8-12")
    #reviews = parsedata(soup)
    #reviews = parsedata(soup)

    #print(reviews)
