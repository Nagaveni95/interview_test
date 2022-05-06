from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\\Baby\\chromedriver_win32\\chromedriver.exe")

driver.get("https://www.techlistic.com/p/demo-selenium-practice.html")

driver.maximize_window()
rows = len(driver.find_elements_by_xpath("//table[@class='tsc_table_s13']/tbody/tr"))
print("row count", rows)
col = len(driver.find_elements_by_xpath("//table[@class='tsc_table_s13']/thead/tr/th"))
print("column count ", col)
count = 0
height_cm = []
for r in range(1, rows + 1):
    structure = driver.find_element_by_xpath(
        "//table[@class='tsc_table_s13']/child::tbody/tr[" + str(r) + "]/th[1]").text
    height = driver.find_element_by_xpath("//table[@class='tsc_table_s13']/child::tbody/tr[" + str(r) + "]/td[3]").text
    height_cm.append(height)
    print("structure name and height ", structure, ":", height)

    count = count + 1
print("count is ", count)
print("height is ", height_cm)


