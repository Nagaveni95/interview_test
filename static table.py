import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\\Baby\\chromedriver_win32\\chromedriver.exe")

driver.get("https://www.techlistic.com/p/demo-selenium-practice.html")

driver.maximize_window()
rows = len(driver.find_elements_by_xpath("//table[@id='customers']/tbody/tr"))
print(rows)
columns = len(driver.find_elements_by_xpath("//table[@id='customers']/tbody/tr[1]/th"))
print(columns)
print("company"+"      "+"contact"+"    "+"country")
for r in range(2,rows+1):
    for c in range(1, columns+1):
        table_value = driver.find_element_by_xpath(
            "//table[@id='customers']/tbody/tr[" + str(r) + "]/td[" + str(c) + "]").text
        print(table_value,end='     ')
    print()
