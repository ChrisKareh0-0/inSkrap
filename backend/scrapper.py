import os 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
from dotenv import load_dotenv
from os.path import join, dirname


# Configure Chrome options
options = Options()
options.headless = True
driver_path = os.environ.get("CHROMEDRIVER_PATH")  # Make sure to set the correct path to the ChromeDriver
service = Service(driver_path)

def login_instagram(driver, username, password):
    driver.get("https://www.instagram.com/accounts/login/")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )

    username_input = driver.find_element(By.NAME, "username")
    password_input = driver.find_element(By.NAME, "password")

    username_input.send_keys(username)
    password_input.send_keys(password)
    password_input.send_keys(Keys.RETURN)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Search']"))
    )

def search_instagram(driver, query, country):
    search_box = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search']")
    search_box.send_keys(f"{query} {country}")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@role='none']"))
    )
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)
    search_box.send_keys(Keys.RETURN)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "article"))
    )

    results = driver.page_source
    return results

def get_profiles(results):
    soup = BeautifulSoup(results, 'html.parser')
    profiles = []

    for profile in soup.find_all('div', class_='v1Nh3 kIKUG _bz0w'):
        link = profile.find('a')['href']
        profiles.append(f"https://www.instagram.com{link}")

    return profiles

if __name__ == "__main__":
    username = os.environ.get("INSTAGRAM_USERNAME")
    password = os.environ.get("INSTAGRAM_PASSWORD")
    driver = webdriver.Chrome(service=service, options=options)

    try:
        login_instagram(driver, username, password)
        results = search_instagram(driver, "business category", "country")
        profiles = get_profiles(results)
        print(profiles)
    finally:
        driver.quit()
