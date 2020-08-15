from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox(executable_path='E:\\Selenium\\Jar Files\\geckodriver.exe')
driver.delete_all_cookies()
driver.implicitly_wait(20)
driver.get('Http://google.com')
gapps = driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/a[1]')
act = ActionChains(driver)
act.move_to_element(gapps)
act.perform()
act.click(gapps)
act.perform()
act.click(gapps)
act.perform()
gmail = driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/a[1]')
search = driver.find_element_by_xpath("//input[@name='q']")
act.drag_and_drop(gmail,search)
act.perform()
