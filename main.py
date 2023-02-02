from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = Options()

chrome_options.add_experimental_option("detach", True)

chrome_driver_path = "C:\python\chromedriver.exe"
driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)

driver.get("https://www.linkedin.com/home")

username = driver.find_element(By.ID, "session_key")
password = driver.find_element(By.ID, "session_password")

username.send_keys("pythontestbripor@gmail.com")
password.send_keys("southlak3")

sign_in_button = driver.find_element(By.CLASS_NAME, "sign-in-form__submit-button")
sign_in_button.click()

time.sleep(1.5)
# Now logged in on home page
jobs = driver.find_element(By.LINK_TEXT, 'Jobs')
jobs.click()

time.sleep(2)

job_search_bar = driver.find_element(By.CLASS_NAME, 'jobs-search-box__text-input')
job_search_bar.send_keys("SDET")
time.sleep(.5)
job_search_bar.send_keys(Keys.ARROW_DOWN)
job_search_bar.send_keys(Keys.ENTER)

time.sleep(1.5)

easy_apply_filter = driver.find_element(By.XPATH, "//button[contains(@id, 'ember') and contains(@aria-label,'Easy Apply filter.')]")
easy_apply_filter.click()
time.sleep(1)
apply_button = driver.find_element(By.CSS_SELECTOR, '.jobs-apply-button--top-card button')
# time.sleep(1)
# apply_button.click()

# Application incomplete - Linkedin security check on login halted progress, everything up to line 46 works as expected
