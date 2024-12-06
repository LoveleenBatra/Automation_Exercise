# Automation_Exercise
## Overview :
This program is an automated testing suite for KloudShip's web application, built using Python and Selenium WebDriver.
It Perform The function of Adding a Package
Adding a Package includes 
Log in to application, navigates to the "Package Types" section, and adds a package with a randomly generated name and dimensions.
## Design Decisions:
I Choose a Selenium WebDriver because of its versatility and compatibility with Python for browser automation.
Dynamic Locators is Employed techniques like XPath, CSS selectors, and safe waiting mechanisms to handle dynamic elements and ensure reliable interaction with the UI.
Randomized Data Package names and dimensions are randomized to test application functionality with varied input data.
Saving the "name" which includes the added package name with dimensions. further this file used in the Deletion of the same package 
Reusability Key functionalities like element finding and login are modularized to enhance readability and reusability.
## Approach :
        ### Initialization: 
              -Configured Selenium WebDriver for Chrome.
              -Defined constants for login credentials and application URL.
        ### Safe Interaction:
              -Used WebDriverWait with expected_conditions to handle dynamic elements and ensure actions only execute when elements are visible or clickable.
              -Random Data Generation:
              -Package names are generated dynamically by combining random first and last names.
              -Dimensions (length, width, height) are randomized within specified constraints.
        ### Error Handling:
              -Implemented safe element finding to minimize script failure due to timing issues.
              -Logged errors for debugging purposes.
              -Logging and Output:
## Chracteristics:
        -The package name and status of operations are printed to the console for clarity.
        -This ensures easy tracking of test results during execution.
## Program Output:
        -User should be able to see newly created package when they login to the application after the execution of Test case 01.
