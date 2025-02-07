from my_selenium_modules.webdriver_getter import *
import time

URL = 'https://secure-retreat-92358.herokuapp.com'

driver = get_driver(False, 'uc')
driver.get(URL)
test_value = (x for x in ['test']*2+['test@gmail.com'])
list(map(lambda x: x.send_keys(next(test_value)), driver.find_elements(By.CSS_SELECTOR, 'input')))
driver.execute_script("arguments[0].click();", driver.find_element(By.CSS_SELECTOR, 'button'))
time.sleep(5)
driver.close()