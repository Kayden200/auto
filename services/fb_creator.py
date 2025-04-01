import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def create_fb_account(email, password, first_name, last_name):
    options = uc.ChromeOptions()
    options.add_argument("--headless")  
    driver = uc.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.get("https://www.facebook.com/")
    time.sleep(2)
    
    driver.find_element(By.NAME, "firstname").send_keys(first_name)
    driver.find_element(By.NAME, "lastname").send_keys(last_name)
    driver.find_element(By.NAME, "reg_email__").send_keys(email)
    driver.find_element(By.NAME, "reg_passwd__").send_keys(password)
    driver.find_element(By.NAME, "websubmit").click()
    
    time.sleep(5)
    driver.quit()
    return "Account Created Successfully!"
