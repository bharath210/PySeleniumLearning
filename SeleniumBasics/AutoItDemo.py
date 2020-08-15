from selenium import webdriver
import os
from time import sleep

driver = webdriver.Firefox(executable_path='E:\\Selenium\\Jar Files\\geckodriver.exe')
driver.delete_all_cookies()
driver.implicitly_wait(20)
driver.get('http://tinyupload.com/')
sleep(10)
# driver.find_element_by_xpath("/html[1]/body[1]/table[1]/tbody[1]/tr[4]/td[1]/table[1]/tbody[1]/tr[1]/td[2]/form[1]/table[1]/tbody[1]/tr[2]/td[1]/input[2]").send_keys(r"C:\Users\Bharath\Downloads\demoAI.exe")

os.system("E:\\demoAI.exe")