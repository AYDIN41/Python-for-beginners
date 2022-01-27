from selenium import webdriver
import loginInfo
import time

browser = webdriver.Firefox()


browser.get("https://twitter.com/")

time.sleep(3)

giris_yap = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]/div")

giris_yap.click()

time.sleep(5)

username = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input")

password = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input")
username.send_keys(loginInfo.username)
password.send_keys(loginInfo.password)
time.sleep(3)

login = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div")
login.click()
time.sleep(5)

lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount == lenOfPage or lastCount == lenOfPage-5:
        match=True
time.sleep(5)
elements = browser.find_elements_by_css_selector(".css-901oao.css-16my406.r-poiln3.r-n6v787.r-1cwl3u0.r-1k6nrdp.r-1e081e0.r-d3hbe1.r-axxi2z.r-qvutc0")
 
for element in elements:
    try:
        element.click()
        time.sleep(2)
    except Exception:
        print("Kafamda bir tuhaflık ")

browser.close()