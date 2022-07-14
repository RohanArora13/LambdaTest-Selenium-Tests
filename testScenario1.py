from ast import Raise
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium_utilities import getChromeDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time


cm_option = Options()
cm_option.add_argument("--lang=en-US")

test_url = "https://www.lambdatest.com/selenium-playground"

driver = webdriver.Chrome(executable_path=getChromeDriver(),options=cm_option)

## 1. Open LambdaTest’s Selenium Playground from https://www.lambdatest.com/selenium-playground


driver.get(test_url)

## 2. Click “Simple Form Demo” under Input Forms

# you can find via Xpath as well
#driver.find_element_by_xpath("/html/body/div[1]/div/section[2]/div/div/div[1]/div[1]/ul/li[1]/a").click()

# but this is the best method i can find 
driver.find_element(By.CSS_SELECTOR,"div.pr-30:nth-child(1) > div:nth-child(1) > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1)").click()

## 3. Validate that the URL contains “simple-form-demo”.
current_url = driver.current_url

if("simple-form-demo" in current_url):
    print("Simple form is open")
else:
    #print("Simple form is not open")
    raise Exception("simple form is not open.")

## 4. Create a variable for a string value E.g: “Welcome to LambdaTest”.

input_data = "Welcome to LambdaTest"

## 5. Use this variable to enter values in the “Enter Message” text box.

# another method is using find_elements_by_id
#driver.find_elements_by_id("user-message")

# but here i wanted to demonstrate use of find_element_by_xpath
element_list = driver.find_elements(By.XPATH,'//*[@id="user-message"]')

for element in element_list:
    if(element.tag_name=="input"):
        input_element = element

input_element.send_keys(input_data)

## 6. Click “Get Checked Value”.

driver.find_element(By.ID,'showInput').click()

## 7. Validate whether the same text message is displayed in the right-hand
## panel under the “Your Message:” section.


message = driver.find_element(By.XPATH,'//*[@id="message"]')

if(str(message.text).lower() == input_data.lower()):
    print("Message added succesfully")
else:
    print("Message not added correctly ")
    raise Exception("Could not Validate same text message is displayed in the right-hand panel")


driver.implicitly_wait(3)
print("Test Scenario 1 Complete")

