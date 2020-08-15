from selenium import webdriver
from time import sleep
driver = webdriver.Firefox(executable_path='E:\\Selenium\\Jar Files\\geckodriver.exe')
driver.delete_all_cookies()
driver.implicitly_wait(20)
driver.get('Http://primusbank.qedgetech.com')
driver.find_element_by_id('txtPword').click()
sleep(5)
print(driver.switch_to.alert.text)
driver.switch_to.alert.accept()
driver.find_element_by_id('txtuId').send_keys('Admin')
driver.find_element_by_id('txtPword').send_keys('Admin')
driver.find_element_by_id('login').click()