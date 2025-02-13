import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

# ---------------------------
# Configure Chrome options for incognito mode
# ---------------------------
options = uc.ChromeOptions()
options.add_argument("--incognito")  # Start Chrome in incognito mode

# Specify the Chrome version (update version_main if needed)
driver = uc.Chrome(options=options, version_main=131)

# Navigate to the target URL
url ="your url link her"
driver.get(url)

# -----------------------------------------
# Optional: Try to interact with the CAPTCHA automatically.
# If your CAPTCHA requires manual solving, you can comment out this block.
# This example assumes a reCAPTCHA-style widget.
# -----------------------------------------
try:
    # Increase the wait time for slow-loading CAPTCHA elements.
    captcha_iframe = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, "//iframe[contains(@title, 'captcha')]"))
    )
    driver.switch_to.frame(captcha_iframe)
    
    captcha_checkbox = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.ID, "recaptcha-anchor"))
    )
    
    # Use JavaScript to click the CAPTCHA checkbox.
    driver.execute_script("arguments[0].click();", captcha_checkbox)
    print("Attempted to click the CAPTCHA checkbox using JavaScript.")
    
    # Switch back to the default content.
    driver.switch_to.default_content()
except Exception as e:
    print("Optional CAPTCHA auto-click did not execute (or not needed):", e)
    print("If the CAPTCHA appears stuck, please solve it manually.")

# -----------------------------------------
# Provide a 4-minute countdown timer to allow manual CAPTCHA solving.
# -----------------------------------------
total_seconds = 4 * 60  # 4 minutes in seconds
print("Website loaded in incognito mode.")
print("Please solve the CAPTCHA manually if needed.")
print("The scraping process will start automatically in 4 minutes.")

for remaining in range(total_seconds, 0, -1):
    mins, secs = divmod(remaining, 60)
    timer = f"{mins:02d}:{secs:02d}"
    print(f"Time remaining: {timer}", end="\r")
    time.sleep(1)
print("\nTime is up. Starting scraping process...")

# ---------------------------
# Begin scraping/automation
# ---------------------------
# 1. Select the option "define the option you want"
try:
    national = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'National - other')]"))
    )
    driver.execute_script("arguments[0].click();", national_option)
    print("Selected 'National - other'")
except Exception as e:
    print("Could not select 'National  - other':", e)
    driver.quit()
    sys.exit(1)

time.sleep(1)

# 2. Select the option "1 person"
try:
    one_person_option = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), '1 person')]"))
    )
    driver.execute_script("arguments[0].click();", one_person_option)
    print("Selected '1 person'")
except Exception as e:
    print("Could not select '1 person':", e)
    driver.quit()
    sys.exit(1)

print("Scraping process complete. You can now proceed with further automation if needed.")
time.sleep(10)

driver.quit()
