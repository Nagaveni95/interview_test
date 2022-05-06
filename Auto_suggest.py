import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\\Baby\\chromedriver_win32\\chromedriver.exe")

driver.get("https://www.google.com/")

driver.maximize_window()
driver.find_element_by_xpath("//*[@title='Search']").send_keys("computer")
time.sleep(3)
search = driver.find_elements_by_xpath("//*[@role='listbox']/li")
print(len(search))
for i in search:
    print(i.text)
    if i.text == 'computer science':
        print("pass")
        i.click()


