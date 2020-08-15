import selenium
from selenium import webdriver

driver = webdriver.Firefox(executable_path='E:\\Selenium\\Jar Files\\geckodriver.exe')
driver.delete_all_cookies()
driver.implicitly_wait(20)
driver.get('Http://spicejet.com')
def departure_cal(dd,mm,yyyy):
    day = dd
    month = mm
    year = yyyy
    driver.find_element_by_id('ctl00_mainContent_view_date1').click()

    y = int(driver.find_element_by_class_name('ui-datepicker-year').text)
    next_el = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[2]/div[1]/a[1]/span[1]")
    if year != y:
        while year != y:
            try:
                next_el.click()
            except selenium.common.exceptions.StaleElementReferenceException as e:
                next_el = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[2]/div[1]/a[1]/span[1]")
                next_el.click()

            y = int(driver.find_element_by_class_name('ui-datepicker-year').text)

        m = driver.find_element_by_class_name('ui-datepicker-month').text
        if not (month.__eq__(m)):
            while not (month.__eq__(m)):
                try:
                    next_el.click()
                except selenium.common.exceptions.StaleElementReferenceException as e:
                    next_el = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[2]/div[1]/a[1]/span[1]")
                    next_el.click()
                m = driver.find_element_by_class_name('ui-datepicker-month').text

            days = list(driver.find_elements_by_xpath("//a[@class='ui-state-default']"))
            for i in days:
                d = int(i.text)
                if day == d:
                    i.click()
                    break
def return_cal(dd,mm,yyyy):
    day = dd
    month = mm
    year = yyyy
    driver.find_element_by_id('ctl00_mainContent_view_date2').click()

    y = int(driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/span[2]").text)
    next_el = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[2]/div[1]/a[1]/span[1]")
    if year != y:
        while year != y:
            try:
                next_el.click()
            except selenium.common.exceptions.StaleElementReferenceException as e:
                print(e)
                next_el = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[2]/div[1]/a[1]/span[1]")
                next_el.click()

            y = int(driver.find_element_by_xpath('/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/span[2]').text)

        m = driver.find_element_by_xpath('/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/span[1]').text
        if not (month.__eq__(m)):
            while not (month.__eq__(m)):
                try:
                    next_el.click()
                except selenium.common.exceptions.StaleElementReferenceException as e:
                    print(e)
                    next_el = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[2]/div[1]/a[1]/span[1]")
                    next_el.click()
                m = driver.find_element_by_xpath('/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/span[1]').text

            days = list(driver.find_elements_by_xpath("//a[@class='ui-state-default']"))
            for i in days:
                d = int(i.text)
                if day == d:
                    i.click()
                    break
departure_cal(5,'March',2021)
return_cal(10,'April',2021)





