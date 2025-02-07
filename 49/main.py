from my_selenium_modules.webdriver_getter import *
from threading import *
import time, dotenv, os

URL = 'https://www.linkedin.com/jobs/search?'

env_vars = dict(dotenv.dotenv_values())
PASSWORD, MY_EMAIL = env_vars.values()

locations = ['United States', 'Europe', 'United Kingdom']

params_list = []
for location in locations: 
    params = {
        'keywords': 'Python Developer',
        'location': location,
        'f_TPR': '&f_WT=2'
    }
    params_list.append(params)

driver = get_driver(False, 'uc')

def save_jobs():
    for params in params_list:
        url = URL + str('&'.join([f'{k}={v}' for (k,v) in params.items()]))
        driver.get(url)

        wait = WebDriverWait(driver,10)
        try:
            sign_in_button = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button')))
            sign_in_button.click()

            email_field = wait.until(EC.visibility_of_element_located((By.XPATH ,'//*[@id="base-sign-in-modal_session_key"]')))
            email_field.send_keys(MY_EMAIL)

            password_field = wait.until(EC.visibility_of_element_located((By.XPATH ,'//*[@id="base-sign-in-modal_session_password"]')))
            password_field.send_keys(PASSWORD+'\n')
        except:
            pass

        #time.sleep(100)
        def save_all_on_page():


            save_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME ,'jobs-save-button__text')))

            job_postings = driver.find_elements(By.CSS_SELECTOR, '.hTpjJTkbbHIePPiRZSAuhLZgzXdXmWlxpc li[id]')
            print(len(job_postings))
            for i in range(len(job_postings)):
                job_postings[i].click()
                time.sleep(2)
                save_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME ,'jobs-save-button__text')))
                if 'Saved' not in save_button.text:
                    save_button.click()
                job_postings = driver.find_elements(By.CSS_SELECTOR, '.hTpjJTkbbHIePPiRZSAuhLZgzXdXmWlxpc li[id]')
                # driver.execute_script('arguments[0].click();', save_button)
            
            time.sleep(5)
            next_page_button = driver.find_elements(By.CSS_SELECTOR, 'button[aria-label~=\'next\']')
            print(next_page_button)
            if len(next_page_button):
                next_page_button[0].click()
                save_all_on_page()
        save_all_on_page()


save_jobs()