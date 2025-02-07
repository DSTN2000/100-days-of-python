from my_selenium_modules.webdriver_getter import *
import pandas as pd

URL = 'https://www.python.org'
driver = get_driver(True, driver_type='seleniumbase')
driver.get(URL)

events = driver.find_elements(By.CSS_SELECTOR, '.shrubbery .menu')[1]
lines = events.text.split('\n')
data = {}
for i in range(0,len(lines),2):
    data[i//2] = {
    'date': lines[i],
    'name': lines[i+1]
    }
data = pd.DataFrame(data)
data = data.transpose()
print(data)