from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json
with open("package_data.json", "r") as file:
    data = json.load(file)
    package_name = data["package_name"]
print(f"Package name loaded: {package_name}")
# Constants
URL = "https://ecspro-qa.kloudship.com"
USERNAME = "kloudship.qa.automation@mailinator.com"
PASSWORD = "Password1"
def safe_find(driver, locator):
    """Safely find an element with a timeout."""
    return WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator))
driver = webdriver.Chrome()  # Ensure correct WebDriver is used
driver.get(URL)
# Login
safe_find(driver, (By.ID, "login-email")).send_keys(USERNAME)
safe_find(driver, (By.ID, "login-password")).send_keys(PASSWORD)
safe_find(driver, (By.ID, "login-btn")).click()
wait = WebDriverWait(driver, 5)
# Delete Package
safe_find(driver, (By.CSS_SELECTOR, ".text-count-card.wordwrap-none")).click()
safe_find(driver, (By.CSS_SELECTOR, ".mat-focus-indicator.mat-menu-trigger.mat-tooltip-trigger.header-button.mat-icon-button.mat-button-base")).click()
safe_find(driver, (By.XPATH, "//button[contains(text(), ' Newest First ')]")).click()
time.sleep(1)
driver.find_element(By.XPATH, f"//div[normalize-space()='{package_name}']").click()
print(f"Package '{package_name}' found. Deleting...")
trash_icon = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.XPATH, "//mat-card[1]//div[2]//mat-icon[1]"))
)
trash_icon.click()
time.sleep(1)
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='mat-focus-indicator mat-raised-button mat-button-base mat-primary ng-star-inserted']"))).click()
print(f"Package '{package_name}' deleted successfully!")
#loged out
safe_find(driver, (By.CSS_SELECTOR, ".mat-focus-indicator.mat-menu-trigger.mat-tooltip-trigger.mat-icon-button.mat-button-base")).click()
safe_find(driver, (By.CSS_SELECTOR, ".mat-focus-indicator.mat-menu-item.ng-tns-c99-1")).click()
print("Logged Out Succesfully")