from my_selenium_modules.webdriver_getter import *
import time

URL = 'https://en.wikipedia.org/wiki/MainPage'

driver = get_driver(False, 'uc')
driver.get(URL)
total_articles = driver.find_elements(By.CSS_SELECTOR, 'a[title=\'Special:Statistics\']')[1].text
print(total_articles)

search_bar = driver.find_element(By.CSS_SELECTOR, 'input[name=\'search\'')
search_bar.send_keys('Python\n')
time.sleep(10)
driver.close()
