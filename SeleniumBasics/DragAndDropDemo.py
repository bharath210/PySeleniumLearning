from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox(executable_path='E:\\Selenium\\Jar Files\\geckodriver.exe')
driver.delete_all_cookies()
driver.implicitly_wait(20)
driver.get('Http://jqueryui.com')
driver.find_element_by_link_text('Droppable').click()
driver.switch_to_frame(0)

drag = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/p[1]")
drop = driver.find_element_by_xpath("/html[1]/body[1]/div[2]")

act = ActionChains(driver)
act.drag_and_drop(drag,drop)
act.perform()