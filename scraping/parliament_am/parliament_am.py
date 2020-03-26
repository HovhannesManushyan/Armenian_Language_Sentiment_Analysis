import requests
from bs4 import BeautifulSoup
import itertools

# get all pages of deputies
page = requests.get("http://www.parliament.am/deputies.php").content
soup = BeautifulSoup(page, "html.parser")
deputylist = [i.get("href") for i in soup.find_all("a", class_="blue_sm")]

for i in deputylist:

    # get deputy page and process
    soup = BeautifulSoup(
        requests.get("http://www.parliament.am/" + i).content, "html.parser"
    )

    # remove new lines from each line. split by : and flatten the array
    chain = itertools.chain.from_iterable(
        [
            i.get_text().replace("\n", "").split(":")
            for i in soup.find_all("div", class_="content")
        ]
    )

    # write the text to file
    with open("parliament_am.cor", "a") as f:
        for q in chain:
            f.write("%s\n" % q.lstrip())