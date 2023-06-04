from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
info = []


# Set up a Selenium driver

service = Service('your-chrome-driver')

driver = webdriver.Chrome(service=service)

# Open the URL
url = "https://milton.nutrislice.com/menu/forbes/dinner"
driver.get(url)

time.sleep(7)

# Click the button to continue to the menu screen
button = driver.find_element(By.CSS_SELECTOR, '.primary')
button.click()

# Wait for the page to load
wait = WebDriverWait(driver, 10)  # Wait for up to 10 seconds
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.content-container")))


# Get the updated HTML
updated_html = driver.page_source

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(updated_html, 'html.parser')

print(soup)
# Find the desired element
display = soup.find_all('div', class_='modal-display')
print(display)
for display_element in display:
    content_elements = display_element.find('div', class_='content')
    info.extend(content_elements)
print(info)
# Quit the driver
driver.quit()

