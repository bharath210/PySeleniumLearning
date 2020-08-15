from selenium import webdriver

driver = webdriver.Firefox(executable_path='E:\\Selenium\\Jar Files\\geckodriver.exe')
driver.get('Http://google.com')

all_links = list(driver.find_elements_by_tag_name('a'))
print(len(all_links))
for i in all_links:
    print(i.text)

driver.close()