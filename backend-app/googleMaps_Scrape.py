import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import json

def scrape_google_maps(keyword, output_file='results.json'):
    chrome_options = webdriver.ChromeOptions()

    # Add necessary options for running Chrome in a Docker container
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--remote-debugging-port=9222")

    # Ensure the path is correct and points to the chromedriver binary
    service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get(f'https://www.google.com/maps/search/?api=1&query={keyword}')

        try:
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "form:nth-child(2)"))).click()
        except Exception:
            pass

        scrollable_div = driver.find_element(By.CSS_SELECTOR, 'div[role="feed"]')
        driver.execute_script("""
            var scrollableDiv = arguments[0];
            function scrollWithinElement(scrollableDiv) {
                return new Promise((resolve, reject) => {
                    var totalHeight = 0;
                    var distance = 1000;
                    var scrollDelay = 3000;

                    var timer = setInterval(() => {
                        var scrollHeightBefore = scrollableDiv.scrollHeight;
                        scrollableDiv.scrollBy(0, distance);
                        totalHeight += distance;

                        if (totalHeight >= scrollHeightBefore) {
                            totalHeight = 0;
                            setTimeout(() => {
                                var scrollHeightAfter = scrollableDiv.scrollHeight;
                                if (scrollHeightAfter > scrollHeightBefore) {
                                    return;
                                } else {
                                    clearInterval(timer);
                                    resolve();
                                }
                            }, scrollDelay);
                        }
                    }, 200);
                });
            }
            return scrollWithinElement(scrollableDiv);
        """, scrollable_div)

        items = driver.find_elements(By.CSS_SELECTOR, 'div[role="feed"] > div > div[jsaction]')

        results = []
        phone_pattern = re.compile(r'\b\d{2}\s?\d{3}\s?\d{3}\b')

        for item in items:
            data = {}

            try:
                data['title'] = item.find_element(By.CSS_SELECTOR, ".fontHeadlineSmall").text
            except Exception:
                pass

            try:
                data['link'] = item.find_element(By.CSS_SELECTOR, "a").get_attribute('href')
            except Exception:
                pass

            try:
                data['website'] = item.find_element(By.CSS_SELECTOR, 'div[role="feed"] > div > div[jsaction] div > a').get_attribute('href')
            except Exception:
                pass

            try:
                rating_text = item.find_element(By.CSS_SELECTOR, '.fontBodyMedium > span[role="img"]').get_attribute('aria-label')
                rating_numbers = [float(piece.replace(",", ".")) for piece in rating_text.split(" ") if piece.replace(",", ".").replace(".", "", 1).isdigit()]

                if rating_numbers:
                    data['stars'] = rating_numbers[0]
                    data['reviews'] = int(rating_numbers[1]) if len(rating_numbers) > 1 else 0
            except Exception:
                pass

            try:
                text_content = item.text
                matches = phone_pattern.findall(text_content)

                unique_phone_numbers = list(set(matches))

                data['phone'] = unique_phone_numbers[0] if unique_phone_numbers else None
            except Exception:
                pass

            if data.get('title'):
                results.append(data)

        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=2)

    finally:
        time.sleep(60)
        driver.quit()

if __name__ == "__main__":
    scrape_google_maps('lawyer')
