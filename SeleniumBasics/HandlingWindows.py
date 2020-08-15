from selenium import webdriver
from  time import sleep

driver = webdriver.Firefox(executable_path='E:\\Selenium\\Jar Files\\geckodriver.exe')
driver.delete_all_cookies()
driver.implicitly_wait(20)
driver.get('http://amazon.in')

driver.find_element_by_id('twotabsearchtextbox').send_keys("oneplus")
driver.find_element_by_class_name('nav-input').click()

driver.find_element_by_partial_link_text("OnePlus Bullets Wireless").click()
print(driver.current_url)
windows = driver.window_handles
w1 = windows[0]
w2 = windows[1]
driver.switch_to.window(w2)
sleep(5)
print(driver.current_url)