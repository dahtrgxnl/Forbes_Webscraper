from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Set up a Selenium driver
service = Service('your-chrome-driver')
driver = webdriver.Chrome(service=service)

# Open the URL
url = "https://milton.nutrislice.com/menu/forbes/dinner/2023-05-22"
driver.get(url)

# Click the button to view the menus. You'll need to replace 'button-id' with the actual ID of the button.
# If the button doesn't have an ID, you might be able to use its class or XPath instead.
button = driver.find_element("css selector", ".primary")
button.click()

# Wait for the page to load after clicking the button. This isn't always necessary, but can help avoid issues
# if the page takes a while to load the menus. You might need to adjust the number of seconds to wait.
import time
time.sleep(10)

# Get the page's HTML
html = driver.page_source

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find the menu items in the parsed HTML
menu_items = soup.find_all('div', class_='food-name-container')

for item in menu_items:
    name = item.find('span', class_='food-name').text
    print(name)

# Extract the information you want from each menu item
print(menu_items)

# Close the Selenium driver
driver.quit()
