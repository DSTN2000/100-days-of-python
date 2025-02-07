from my_selenium_modules.webdriver_getter import *
import time, pandas as pd

FORMS_URL = 'https://docs.google.com/forms/d/e/1FAIpQLSfjzrU5zzw2n-xO8YOgb_Ym1wLN9Kl0c7EhqMuHf7XC_3yHng/viewform?usp=dialog'

driver = get_driver(False, 'uc')

def submit_form(data):
    driver.get(FORMS_URL)
    wait = WebDriverWait(driver, 20)
    input_fields = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'input[type=\'text\']')))
    list(map(lambda x: x.send_keys(next(data)), input_fields))
    submit_button = driver.find_element(By.CSS_SELECTOR, '.Y5sE8d > span:nth-child(3) > span:nth-child(1)')
    submit_button.click()
    #time.sleep(10)


df = pd.read_csv('53/data.csv')
# print(df)
for id, row in df.iterrows():
    data = (x for x in [row['address'], row['price'], row['link']])
    submit_form(data)
    print(f'Submitted form {id}')
