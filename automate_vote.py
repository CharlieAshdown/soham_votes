from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

for i in range(1000):


# Set Chrome options for incognito mode
	chrome_options = Options()
	chrome_options.add_argument("--incognito")

	# Initialize the WebDriver for Chrome with the specified options
	driver = webdriver.Chrome(options=chrome_options)
# Open the Opera browser in incognito mode and navigate to a website
	driver.get("https://poll.fm/13852675")

	time.sleep(1)

# Example: Click at a specific location (x, y) on the webpage

# Create an ActionChains object
	actions = ActionChains(driver)

# Perform other actions on the Opera browser as usual
# For example:
# - Find elements
# - Click buttons
# - Input text

# Example: Find the page title and print it
	title = driver.title
	print("Page Title:", title)

	element = driver.find_element("id", "PDI_answer61781958")
	element.click()
	element = driver.find_element("id", "pd-vote-button13852675")
	element.click()

# Keep the browser window open for watching the bot working
# input("Press Enter to quit...")

# Example: Close the browser when finished
	driver.quit()
