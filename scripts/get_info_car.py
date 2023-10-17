import time
import undetected_chromedriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def get_data(url):
    option = Options()
    try:
        driver = undetected_chromedriver.Chrome(options=option)
        driver.get(url=url)
        time.sleep(15)
        result = str(driver.find_element(By.CLASS_NAME, "truncate-text__wrapper").get_attribute("innerHTML"))
        result = result.replace("&nbsp;", "")
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
        
    return result

def get_car_name(car_number):
    url = f"https://avtocod.ru/proverkaavto/{car_number}?rd=GRZ"
    result = get_data(url)
    return result
