from selenium import webdriver

driver = webdriver.Firefox(executable_path='E:\\Selenium\\Jar Files\\geckodriver.exe')
driver.delete_all_cookies()
driver.implicitly_wait(20)
driver.get('Http://orangehrm.qedgetech.com')
driver.find_element_by_id('txtUsername').send_keys('Admin')
driver.find_element_by_name('txtPassword').send_keys('Qedge123!@#')
driver.find_element_by_xpath("//input[@id='btnLogin']").click()
driver.find_element_by_link_text('PIM').click()
driver.find_element_by_link_text('Add Employee').click()
eid_element = driver.find_element_by_id('employeeId')

print(eid_element.get_attribute('value'))
eid_element.clear()
eid_element.send_keys('2020')