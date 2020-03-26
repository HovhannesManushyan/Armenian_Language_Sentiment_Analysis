from selenium import webdriver

homelink = (
    "path of the cloned directory"
    + "/pdfextracter/pdfs"
)

chrome_options = webdriver.ChromeOptions()
prefs = {"download.default_directory": homelink}
chrome_options.add_experimental_option("prefs", prefs)


driver = webdriver.Chrome("../drivers/chromedriver", options=chrome_options)

for i in range(100, 2000):
    driver.get(f"https://lib.armedu.am/resource/{i}")
    try:
        driver.find_element_by_xpath("//a[contains(@href, '/download/')]").click()
    except:
        pass