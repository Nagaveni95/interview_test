from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\\Baby\\chromedriver_win32\\chromedriver.exe")

driver.get("https://demo.guru99.com/test/table.html")

driver.maximize_window()
driver.implicitly_wait(3)
rows_count = len(driver.find_elements_by_xpath("//table//tbody/tr"))
print("row count is ",rows_count)
for r in range(1,rows_count+1):
    col=driver.find_element_by_xpath("//table//tbody/tr["+str(r)+"]").text
    print("cell value of row number",r,"and column number is",col)
    # print(col)