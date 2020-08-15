from selenium import webdriver

driver = webdriver.Firefox(executable_path='E:\\Selenium\\Jar Files\\geckodriver.exe')
driver.delete_all_cookies()
driver.get('Http://google.com')
driver.find_element_by_link_text('Gmail').click()
title = driver.title
url = driver.current_url
print(title)
print(url)
driver.close()