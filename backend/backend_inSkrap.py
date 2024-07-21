from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

def setup_driver():
    """
    Sets up the Selenium WebDriver.
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

def fetch_business_profiles(driver, category, location):
    """
    Fetches business profiles based on a category and location from Google Maps.
    """
    search_url = f"https://www.google.com/maps/search/{category}+in+{location}"
    driver.get(search_url)
    time.sleep(3)
    
    profiles = []
    
    # Scroll down to load more results
    for _ in range(5):  # Adjust the range for more scrolling
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        time.sleep(2)
    
    # Find all business listings on the page
    listings = driver.find_elements(By.XPATH, '//div[contains(@class, "section-result")]')
    
    for listing in listings:
        try:
            name = listing.find_element(By.XPATH, './/h3').text
            address = listing.find_element(By.XPATH, './/span[contains(@class, "section-result-location")]').text
            phone = ""
            website = ""
            try:
                phone = listing.find_element(By.XPATH, './/span[contains(@class, "section-result-phone-number")]').text
            except:
                pass
            try:
                website = listing.find_element(By.XPATH, './/a[contains(@class, "section-result-action-icon")]').get_attribute('href')
            except:
                pass
            profiles.append((name, address, phone, website))
        except Exception as e:
            print(f"Error extracting listing: {e}")
    
    return profiles

def export_to_excel(profiles, filename):
    """
    Exports the profiles to an Excel file.
    """
    df = pd.DataFrame(profiles, columns=["Name", "Address", "Phone", "Website"])
    df.to_excel(filename, index=False)
    print(f"Data successfully exported to {filename}")

def main(category, location, filename):
    driver = setup_driver()
    try:
        profiles = fetch_business_profiles(driver, category, location)
        print(f"Business profiles in {category} category from {location}:")
        for profile in profiles:
            print(profile)
        
        export_to_excel(profiles, filename)
    finally:
        driver.quit()

if __name__ == "__main__":
    category = "restaurant"
    location = "USA"
    filename = "business_profiles.xlsx"
    main(category, location, filename)
