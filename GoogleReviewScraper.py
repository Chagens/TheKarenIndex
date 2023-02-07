from pathlib import Path
from selenium import webdriver
from bs4 import BeautifulSoup

#file for attempting to scrape google for reviews 

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument("--lang=en")

browser = webdriver.Chrome("chromedriver.exe",options=options,)

url = "https://www.amazon.com/Streamlight-75636-Flashlight/dp/B003TODYU2/ref=sr_1_12?keywords=flashlights&qid=1646865764&sprefix=flashl%2Caps%2C129&sr=8-12"

browser.get(url)

soup = BeautifulSoup(browser.page_source,'html.parser')

for item in soup.find_all("span",class_="review-full-text"):
    print(item.get_text())
    
