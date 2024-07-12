from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup

options = Options()
options.headless = True
driver_path = '/usr/bin/chromedriver'  # Make sure to set the correct path to the ChromeDriver
service = Service(driver_path)

def search_instagram(query, country):
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://www.instagram.com")
    time.sleep(2)

    search_box = driver.find_element_by_css_selector("input[placeholder='Search']")
    search_box.send_keys(f"{query} {country}")
    time.sleep(2)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)
    search_box.send_keys(Keys.RETURN)
    time.sleep(5)

    results = driver.page_source
    driver.quit()

    soup = BeautifulSoup(results, 'html.parser')
    profiles = []

    for profile in soup.find_all('div', class_='v1Nh3 kIKUG  _bz0w'):
        link = profile.find('a')['href']
        profiles.append(f"https://www.instagram.com{link}")

    return profiles
