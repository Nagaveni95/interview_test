import time

import requests
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="D:\\Baby\\chromedriver_win32\\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/broken_images")
driver.maximize_window()
list_image=driver.find_elements_by_tag_name("img")
print(len(list_image))
for images in list_image:
    r=requests.get(images.get_attribute('src'))
    if r.status_code!=200:
        print(images.get_attribute('outerHTML'))
        print("broken image")
    else:
        print(images.get_attribute('outerHTML'))
        print("not broken image")

