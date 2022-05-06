from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\\Baby\\chromedriver_win32\\chromedriver.exe")

driver.get("https://demo.guru99.com/test/web-table-element.php")

driver.maximize_window()

rows = len(driver.find_elements_by_xpath("//*[@class='dataTable']/tbody/tr"))
print("rows count", rows)
col = len(driver.find_elements_by_xpath("//*[@class='dataTable']/thead/tr/th"))
print("column count", col)
third_row=driver.find_element_by_xpath("//*[@class='dataTable']/tbody/tr[3]").text
print("3rd row",third_row)
group_value = driver.find_element_by_xpath("//*[@class='dataTable']/tbody/tr[3]/td[2]").text
print("group",group_value)
current_prize=[]
for r in range(1,rows+1):
    prize=driver.find_element_by_xpath("//*[@class='dataTable']/tbody/tr["+str(r)+"]/td[4]").text
    row = driver.find_element_by_xpath("//*[@class='dataTable']/tbody/tr[" + str(r) + "]").text
    current_prize.append(prize)


print(current_prize)
print(max(current_prize))
# print("corresponding row for maximum value",row)


