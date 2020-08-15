from selenium import webdriver
from selenium.webdriver.support.ui import Select


driver = webdriver.Firefox(executable_path='E:\\Selenium\\Jar Files\\geckodriver.exe')
driver.delete_all_cookies()
driver.implicitly_wait(20)
driver.get('Http://spicejet.com')
#Code for handling DropDown list

currency = Select(driver.find_element_by_id('ctl00_mainContent_DropDownListCurrency'))
currency.select_by_visible_text('USD')
driver.find_element_by_id('divpaxinfo').click()
adults = Select(driver.find_element_by_id('ctl00_mainContent_ddl_Adult'))
adults.select_by_visible_text('4')
child = Select(driver.find_element_by_id('ctl00_mainContent_ddl_Child'))
child.select_by_visible_text('3')
infants = Select(driver.find_element_by_id('ctl00_mainContent_ddl_Infant'))
infants.select_by_visible_text('2')

#code for handling Radio buttons
