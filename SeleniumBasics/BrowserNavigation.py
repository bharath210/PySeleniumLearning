from selenium import webdriver
from time import sleep

driver = webdriver.Firefox(executable_path='E:\\Selenium\\Jar Files\\geckodriver.exe')
driver.get('http://google.com')
sleep(1)
driver.get("http://facebook.com")
sleep(1)
driver.minimize_window()
sleep(1)
driver.maximize_window()
sleep(1)
driver.back()
sleep(1)
driver.forward()
sleep(1)
driver.refresh()
sleep(1)
driver.close()
driver.quit()