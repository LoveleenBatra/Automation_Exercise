from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time
import random
import json
# Constants
URL = "https://ecspro-qa.kloudship.com"
USERNAME = "kloudship.qa.automation@mailinator.com"
PASSWORD = "Password1"

def safe_find(driver, locator):
    """Safely find an element with a timeout."""
    return WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator))
driver = webdriver.Chrome()
driver.get(URL)
# Login
safe_find(driver, (By.ID, "login-email")).send_keys(USERNAME)
time.sleep(1)
safe_find(driver, (By.ID, "login-password")).send_keys(PASSWORD)
time.sleep(1)
safe_find(driver, (By.ID, "login-btn")).click()
time.sleep(1)
print("Loggin succesfully")
# Add Package
# List of sample first names and last names
first_names = ["John", "Jane", "Alex", "Emily", "Chris", "Katie"]
last_names = ["Smith", "Johnson", "Brown", "Williams", "Jones", "Miller"]
# Generate a random package name
package_name = f"{random.choice(first_names)}_{random.choice(last_names)}{random.randint(1, 999)}"
safe_find(driver, (By.CSS_SELECTOR, ".text-count-card.wordwrap-none")).click()
time.sleep(3)
safe_find(driver, (By.CSS_SELECTOR, ".mat-focus-indicator.button-disabled.mat-icon-button.mat-button-base.ng-star-inserted")).click()
time.sleep(1)
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@formcontrolname='name']"))
).send_keys(package_name)
key1=random.randint(1, 20)
key2=random.randint(1, 20)
key3=random.randint(1, 20)
keys=str(key1)+" x "+str(key2)+" x "+str(key3)
safe_find(driver, (By.XPATH, "//input[@formcontrolname='length']")).send_keys(key1)
safe_find(driver, (By.XPATH, "//input[@formcontrolname='width']")).send_keys(key2)
safe_find(driver, (By.XPATH, "//input[@formcontrolname='height']")).send_keys(key3)
time.sleep(5)
safe_find(driver, (By.XPATH, "//mat-toolbar[@class='mat-toolbar module-header mat-toolbar-single-row']//button[@class='mat-focus-indicator mat-icon-button mat-button-base ng-star-inserted']")).click()
name=package_name+" "+"1"+str(key1)+" x "+"1"+str(key2)+" x "+"1"+str(key3)
with open("package_data.json", "w") as file:
    json.dump({"package_name": name}, file)
print(f"Package '{package_name}' added successfully.")
print(f"Dimensions '{keys}' added successfully.")
#logging out
safe_find(driver, (By.CSS_SELECTOR, ".mat-focus-indicator.mat-menu-trigger.mat-tooltip-trigger.mat-icon-button.mat-button-base")).click()
safe_find(driver, (By.CSS_SELECTOR, ".mat-focus-indicator.mat-menu-item.ng-tns-c99-1")).click()
print("Logged Out Succesfully")