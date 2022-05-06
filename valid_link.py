import time

import requests
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="D:\\Baby\\chromedriver_win32\\chromedriver.exe")
driver.get("https://demoqa.com/broken")
driver.maximize_window()
driver.find_element_by_xpath("//a[text()='Click Here for Valid Link']").click()
time.sleep(2)

list_link = driver.find_elements_by_xpath("//*[contains(@href,'https')]")
print(len(list_link))
for link in list_link:
    print(link.text)
    r = requests.head(link.get_attribute('href'))
    if r.status_code == 400:
        print("not vaild link")

    else:
        print("vaild link")
        print(link.get_attribute("href"), r.status_code)

