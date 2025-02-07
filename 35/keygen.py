from my_selenium_modules.webdriver_getter import *
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pyperclip


url1 = "https://tempmailo.com/"
url2 = 'https://temp-mail.io/en'

results=[]
pages_amount=0

def tempmailo_received_new_letter(driver:webdriver):
    letters = driver.find_elements(By.CLASS_NAME,'mail-item')
    letters_amount = len(letters)
    print(letters_amount)
    if letters_amount > 1:
        print('Received_new_letter')
        return True
    else:
        print('No new letters')
        return

def get_a_temp_mail(url):
    print(url)
    driver = get_driver(headless=True, driver_type='seleniumbase')
    driver.get(url)
    wait = WebDriverWait(driver, 10)
    if url == url1:
        element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'iconx')))
        element.click()
    else:
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'header-btn')))
        driver.find_elements(By.CLASS_NAME,'header-btn')[0].click()
        print('Copied')

    # wait = WebDriverWait(driver, 10)
    # while not tempmailo_received_new_letter(driver):
    #     print('Waiting...')
    #     time.sleep(1)

    time.sleep(2)    
    driver.close()
    driver.quit()

def login_open_weather(url='https://home.openweathermap.org/users/sign_up'):

    SITE_KEY = '6LfOfhQUAAAAAFIMgtwcp1CBRsxWw0JxlFpD90aq'

    driver = get_driver(driver_type='uc')
    driver.get(url)
    #time.sleep(20)
    #driver.get("https://bot.sannysoft.com/")
    wait = WebDriverWait(driver, 10)
    username_field = wait.until(EC.visibility_of_element_located((By.ID,'user_username')))
    # username_field.send_keys('__')

    # email_field = driver.find_element(By.ID,'user_email')
    # email_field.send_keys(pyperclip.paste())


    # password_field = driver.find_element(By.ID,'user_password')
    # password_field.send_keys('12345678')


    # password_confirmation_field = driver.find_element(By.ID,'user_password_confirmation')
    # password_confirmation_field.send_keys('12345678')

    # driver.find_element(By.ID,'agreement_is_age_confirmed').click()
    # driver.find_element(By.ID,'agreement_is_accepted').click()

    all_frames = driver.find_elements(By.CSS_SELECTOR,'iframe')
    print(all_frames)
    
    # time.sleep(5)
    
    # frame = WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it(
    #     (By.CSS_SELECTOR,"iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']")))
    # print(frame)
    driver.switch_to.frame(all_frames[0])
    time.sleep(3)
    box = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME,'recaptcha-checkbox-checkmark')))
    time.sleep(5)
    driver.execute_script("arguments[0].click();", box)  
    time.sleep(5)
    driver.save_screenshot('1.png')
    time.sleep(20)

#get_a_temp_mail(url2)
login_open_weather()
