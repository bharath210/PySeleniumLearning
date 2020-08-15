from selenium import webdriver

driver = webdriver.Firefox(executable_path='E:\\Selenium\\Jar Files\\geckodriver.exe')
driver.delete_all_cookies()
driver.implicitly_wait(20)
driver.get('Http://spicejet.com')

driver.find_element_by_id('ctl00_mainContent_rbtnl_Trip_1').click()
val = driver.find_element_by_id('ctl00_mainContent_rbtnl_Trip_1').get_attribute('value')
print(val)