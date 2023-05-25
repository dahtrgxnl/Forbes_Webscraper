from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Set up a Selenium driver
service = Service('/Users/alexanderlandis-arnold/Downloads/chromedriver_mac64/chromedriver')
driver = webdriver.Chrome(service=service)

# Open the URL
url = "https://milton.nutrislice.com/menu/forbes/dinner"
driver.get(url)

# Clicks the button to continue to the menu screen
button = driver.find_element("css selector", ".primary")
button.click()

# Waits for the page to load
import time

time.sleep(10)

# Get the page's HTML
html = driver.page_source

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

date = soup.find_all('div', class_='day-label-wrapper')
menu = soup.find_all('div', class_='menu-container')
x = 0
for i in date:
   day_menu = str(i.text) + str(menu[x].text)
   day_menu = day_menu.replace("  ", "\n")
   print(day_menu)
   x += 1

# Close the Selenium driver
driver.quit()
