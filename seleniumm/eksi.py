from selenium import webdriver

import time

browser = webdriver.Firefox()

url = "https://eksisozluk.com/mustafa-kemal-ataturk--34712"

browser.get(url)

time.sleep(10)

elements = browser.find_elements_by_css_selector(".content")
i = 1
for element in elements:
    print("{}.söz".format(i))
    print(element.text)
    print("\n")

    i += 1


browser.close()
