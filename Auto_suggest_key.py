import time

from selenium import webdriver

from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path="D:\\Baby\\chromedriver_win32\\chromedriver.exe")

driver.get("https://www.google.com/")

driver.maximize_window()
search=driver.find_element_by_xpath("//*[@title='Search']")
search.send_keys("computer")
search.send_keys(Keys.ENTER)


