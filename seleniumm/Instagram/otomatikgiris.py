from selenium import webdriver
import time
import loginInfo
browser = webdriver.Firefox()
browser.get("https://www.instagram.com/")
time.sleep(2)
username = browser.find_element_by_name("username")
password = browser.find_element_by_name("password")

username.send_keys(loginInfo.username)
password.send_keys(loginInfo.password)

loginButton = browser.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button")
loginButton.click()
time.sleep(20)
profilButton = browser.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[5]/span")
profilButton.click()
time.sleep(10)
followers = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a")
followers.click()
time.sleep(5)
javascrpt = """
followers = document.querySelector(".isgrP");
followers.scrollTo(0, followers.scrollHeight);
lenOfPage=followers.scrollHeight;
return lenOfPage;
"""
lenOfPage = browser.execute_script(javascrpt)
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage = browser.execute_script(javascrpt)
    if lastCount == lenOfPage:
        match=True
followersList = []

follower = browser.find_elements_by_css_selector(".FPmhX.notranslate._0imsa")
for takipci in follower:
    followersList.append(takipci.text)
with open ("C:/Users/asus/Desktop/aydin41.txt","w",encoding = "UTF-8") as dosya:
    for a in followersList:
        dosya.write(a)
        dosya.write("\n")
browser.close()
