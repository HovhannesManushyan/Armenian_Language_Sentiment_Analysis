import requests
from bs4 import BeautifulSoup
import re


def get_all_ids(url_arr):

    # get ids of links from the main page
    return [[i.split("=")[1].split("&")[0], i.split("=")[2]] for i in url_arr]


def scrap_page(url):

    # get the text from each id
    page = requests.get(url).content
    soup = BeautifulSoup(page, "html.parser")
    data = [i.get_text() for i in soup.find_all("span", class_="Apple-style-span")]

    # split by : as sentence delimeter and remove duplicates
    return list(set([j for i in data for j in i.split(":") if j]))


finallist = []

for a in range(1, 39):

    # get all the links to be scraped
    page = requests.get(
        f"https://www.encyclopedia.am/encyclopedia1.php?lId={a}"
    ).content
    soup = BeautifulSoup(page, "html.parser")
    all_ids = get_all_ids([i.get("href") for i in soup.find_all("a", class_="headers")])

    # scrap and use counter as a track of success
    counter = 0
    lendone = len(all_ids)
    for b, c in all_ids:
        counter = counter + 1
        print(lendone - counter)
        scraped = scrap_page(f"https://www.encyclopedia.am/pages.php?bId={b}&hId={c}")
        finallist.extend(scraped)

# write all collected data to a file
with open("test.cor", "a") as f:
    for item in finallist:
        f.write("%s\n" % item)