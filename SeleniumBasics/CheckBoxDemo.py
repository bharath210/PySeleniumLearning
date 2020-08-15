from selenium import webdriver

driver = webdriver.Firefox(executable_path='E:\\Selenium\\Jar Files\\geckodriver.exe')
driver.delete_all_cookies()
driver.implicitly_wait(20)
driver.get('Http://spicejet.com')
cb = driver.find_element_by_id('ctl00_mainContent_chk_friendsandfamily')
print(cb.is_selected())
if not cb.is_selected():
    cb.click()
