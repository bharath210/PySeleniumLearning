from selenium import webdriver

driver = webdriver.Firefox(executable_path='E:\\Selenium\\Jar Files\\geckodriver.exe')
driver.delete_all_cookies()
driver.implicitly_wait(20)
driver.get('Http://google.com')
driver.find_element_by_name('q').send_keys('Selenium')
suggestions = driver.find_element_by_class_name('erkvQe').find_elements_by_tag_name('li')
for i in suggestions:
    print(i.text)

suggestions[0].click()
driver.close()