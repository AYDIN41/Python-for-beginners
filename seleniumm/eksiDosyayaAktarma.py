from selenium import webdriver
import random
import time

browser = webdriver.Firefox()

url = "https://eksisozluk.com/mustafa-kemal-ataturk--34712?p="

pageCount = 1
entries = []
while pageCount <= 11:
    randonPage = random.randint(1,2126)
    newUrl = url + str(randonPage)
    browser.get(newUrl)
    elements = browser.find_elements_by_css_selector(".content")
    for element in elements:
        entries.append(element.text)
    time.sleep(2)
    pageCount += 1
soz = ". söz: "

with open("C:/Users/asus/Desktop/aydin41.txt","w") as dosya:
    for i in range(1,101):
        dosya.write(str(i))
        dosya.write(str(soz))
        dosya.write(entries[i])
        dosya.write("\n")

browser.close()
