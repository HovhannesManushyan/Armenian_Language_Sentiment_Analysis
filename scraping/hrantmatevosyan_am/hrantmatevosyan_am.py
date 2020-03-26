import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import itertools
import time

wd= webdriver.Chrome('../../drivers/chromedriver')


wd.get("https://hrantmatevossian.org/hy/works")


#finding pages

ux = [i.get_attribute('href') for i in wd.find_elements_by_xpath("//a")]

#pass over each href

for i in ux:
    cur = str(i)
    if(cur[-11:len(cur)]!="#tabcontent"):
        continue
    #get each page
    wd.get(i)
    soup = BeautifulSoup(wd.page_source, "html.parser")
    page_data = itertools.chain.from_iterable(
        [i.get_text().replace(':','։').split("։") for i in soup.find_all("p") if i.get_text()]
    )

    # write to file each page
    with open("hrantmatevosian.cor", "a",encoding="utf-8") as f:
        for i in page_data:
            f.write("%s\n" % i.replace("\n", "").lstrip())