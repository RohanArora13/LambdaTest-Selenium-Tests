from click import style
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium_utilities import getChromeDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

## Test Scenario 3

cm_option = Options()
cm_option.add_argument("--lang=en-US")

test_url = "https://www.lambdatest.com/selenium-playground"

driver = webdriver.Chrome(executable_path="chromedriver.exe",options=cm_option)

## 1. Open LambdaTest’s Selenium Playground from https://www.lambdatest.com/selenium-playground

driver.get(test_url)

## click “Input Form Submit” under “Input Forms”

driver.find_element(By.CSS_SELECTOR,"div.pr-30:nth-child(1) > div:nth-child(1) > ul:nth-child(2) > li:nth-child(5) > a:nth-child(1)").click()

## Click “Submit” without filling in any information in the form

driver.find_element(By.XPATH,'//*[@class="text-right mt-20"]/button').click()

## 3. Assert “Please fill in the fields” error message

message = driver.find_element(By.NAME,"name").get_attribute("validationMessage")
print(message)

assert message.lower() == "Please fill out this field.".lower() , "error no alert message"


## 4. Fill in Name, Email, and other fields

input_data = {
    "name":"Rohan Arora",
    "email":"rohanarora1313@gmail.com",
    "password":"Pa$$W0rd123",
    "company":"lambda Test",
    "website":"www.rohanarora.dev",
    "city":"mumbai",
    "address_line1":"lokhandawala",
    "address_line2":"mumbai",
    "zip":"400001",
}

for field,data in input_data.items():
    driver.find_element(By.NAME,field).send_keys(data)


dropdown = Select(driver.find_element(By.CSS_SELECTOR,"select.w-full"))

dropdown.select_by_visible_text("United States")

# inputState

driver.find_element(By.ID,"inputState").send_keys("Washington")


driver.find_element(By.XPATH,'//*[@class="text-right mt-20"]/button').click()

# wait for message to be displayed
time.sleep(0.5)


## 7. Once submitted, validate the success message “Thanks for contacting us, we will get back to you shortly.” on the screen.

# below commented code is not working it should work but something is wrong
#driver.find_element(By.LINK_TEXT,"Thanks for contacting us, we will get back to you shortly.")
#driver.find_element(By.PARTIAL_LINK_TEXT,"Thanks for contacting us")

try:
    message = driver.find_element(By.CLASS_NAME,"success-msg")
    message_style = message.get_attribute("style")

    # style is set to display if form is submmited succesfully
    if (message_style == 'display: block;'):
        print("form submited form succesfully")
    else:
        raise
except:
    print("cannot submit form succesfully")


time.sleep(200)