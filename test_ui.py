from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Chrome options for EC2 (headless)
options = Options()
options.binary_location = "/usr/bin/google-chrome"
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")

# Start driver
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

try:
    # Open your EC2 app URL
    driver.get("http://127.0.0.1:5000")
    time.sleep(2)

    # Get title text
    title = driver.find_element(By.ID, "title").text
    print("Title:", title)

    # Enter name
    driver.find_element(By.ID, "name").send_keys("Dhyey")

    # Click button
    driver.find_element(By.ID, "btn").click()
    time.sleep(2)

    # Get output message
    message = driver.find_element(By.ID, "message").text
    print("Message:", message)

    # Validation
    if "Hello, Dhyey" in message:
        print("✅ UI Test Passed")
    else:
        print("❌ UI Test Failed")

except Exception as e:
    print("Error:", e)

finally:
    driver.quit()