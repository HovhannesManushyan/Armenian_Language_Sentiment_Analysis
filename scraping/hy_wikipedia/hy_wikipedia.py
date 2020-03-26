import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import itertools
import time

driver = webdriver.Chrome("../../drivers/chromedriver")


driver.get("https://hy.wikipedia.org/wiki/")

# continiously fetch random data from wikipedia
while True:

    # alt+shift+x shortcut to get random data in wikipedia
    webdriver.ActionChains(driver).key_down(Keys.ALT).key_down(Keys.SHIFT).send_keys(
        "x"
    ).key_up(Keys.ALT).key_up(Keys.SHIFT).perform()
    soup = BeautifulSoup(driver.page_source, "html.parser")

    # get all sentences from page and split by :, than create one dimensional list using from_iterable
    wikidat = itertools.chain.from_iterable(
        [i.get_text().split("։") for i in soup.find_all("p") if i.get_text()]
    )

    # write to file each page
    with open("hy_wikipedia.cor", "a") as f:
        for i in wikidat:
            f.write("%s\n" % i.replace("\n", "").lstrip())