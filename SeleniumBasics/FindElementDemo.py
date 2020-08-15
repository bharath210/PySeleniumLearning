from selenium import webdriver

driver = webdriver.Firefox(executable_path='E:\\Selenium\\Jar Files\\geckodriver.exe')
driver.get('Http://facebook.com')
driver.find_element_by_link_text('Create New Account').click()
title = driver.title
print(title)
driver.close()