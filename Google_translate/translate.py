from nltk.tokenize import sent_tokenize
import glob
import re
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import itertools
import time

from multiprocessing.pool import ThreadPool, Pool
import threading


threadLocal = threading.local()

def driver_create():
    driver = getattr(threadLocal, 'driver', None) 
    if driver is None: # check if thread has it's driver
        chrome_options = Options()
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-gpu") # efficient web driver initization
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome('/home/john/debug/chromedriver',options=chrome_options)
        driver.get("https://translate.google.com/#view=home&op=translate&sl=en&tl=hy") 
        setattr(threadLocal, 'driver', driver)
    return driver


def trans_get(texts):
    driver=driver_create()
    wait = WebDriverWait(driver, 10)
    input=wait.until(lambda driver: driver.find_element_by_xpath('//textarea[@id="source"]')) # get input textarea if it exists
    input.send_keys(texts)
    output=wait.until(lambda driver: driver.find_element_by_xpath('//span[@class="tlid-translation translation"]')) # get output if it exists
    with open('outputneg.txt','a') as f:
        f.write(output.text+'\n')
    time.sleep(1) # wait to avoiding repetated copy
    input.clear()

mylist = [f for f in glob.glob("neg/*.txt")] # get filenames

finalist = itertools.chain.from_iterable([sent_tokenize(re.sub('<.*?>', '', open(i).read())) for i in mylist]) # extract all lines from all files



ThreadPool(10).map(trans_get,finalist) # instantiate threaded translators
