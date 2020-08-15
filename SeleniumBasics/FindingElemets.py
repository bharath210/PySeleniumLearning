from selenium import webdriver

driver = webdriver.Firefox(executable_path='E:\\Selenium\\Jar Files\\geckodriver.exe')
driver.get('Http://orangehrm.qedgetech.com')
driver.find_element_by_id('txtUsername').send_keys('Admin')
driver.find_element_by_name('txtPassword').send_keys('Qedge123!@#')
driver.find_element_by_xpath("//input[@id='btnLogin']").click()

driver.find_element_by_partial_link_text('Welcome').click()
driver.find_element_by_link_text('Logout').click()
driver.close()