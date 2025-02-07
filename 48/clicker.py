from my_selenium_modules.webdriver_getter import *
from threading import *
import time

URL = 'https://orteil.dashnet.org/cookieclicker/'

driver = get_driver(False, 'uc')
driver.get(URL)
wait = WebDriverWait(driver, 10)
lang_field = wait.until(EC.visibility_of_element_located((By.ID,'langSelect-EN')))
driver.execute_script('arguments[0].click();', lang_field)

bulk_buy = driver.find_element(By.ID,'storeBulk10')
driver.execute_script('arguments[0].click();', bulk_buy)

the_cookie = driver.find_element(By.CSS_SELECTOR, '#bigCookie')

def get_store_items():
    items = driver.find_elements(By.CSS_SELECTOR, '.product.unlocked.enabled')
    return items

def get_upgrades():
    upgrades = driver.find_elements(By.CSS_SELECTOR, '.crate.upgrade.enabled')
    return upgrades


def click_the_cookie():
    #print(f'Hi! I am {current_thread().ident}')
    while True:
        #print(f'Hi! I am {current_thread().ident}, a clicking thread')
        the_cookie.click()
        #driver.execute_script('arguments[0].click();', the_cookie)

def think():
    #print(f'Hi! I am {current_thread().ident}')
    while True:
        #print(f'Hi! I am {current_thread().ident}, a thinking thread')
        try:
            if get_store_items():
                driver.execute_script('arguments[0].click();', get_store_items()[0])
            if get_upgrades():
                driver.execute_script('arguments[0].click();', get_upgrades()[0])
        except:
            pass


threads = []
clicking_threads = [Thread(target=click_the_cookie) for _ in range(1)]
for clicking_thread in clicking_threads:
    clicking_thread.daemon = True
    clicking_thread.start()
    threads.append(clicking_thread)

thinking_thread = Thread(target=think)
thinking_thread.daemon = True
thinking_thread.start()
thinking_thread.join()
threads.append(thinking_thread)
for thread in threads:
    thread.join()

#-----TESTS-----#

# print(get_store_items())
# while len(get_store_items())<1:
#     print(get_store_items())
#     print('test')
# think()