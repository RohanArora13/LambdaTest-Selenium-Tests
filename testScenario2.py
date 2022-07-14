from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium_utilities import getChromeDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time


cm_option = Options()
cm_option.add_argument("--lang=en-US")

test_url = "https://www.lambdatest.com/selenium-playground"

driver = webdriver.Chrome(executable_path="chromedriver.exe",options=cm_option)

## 1. Open LambdaTest’s Selenium Playground from https://www.lambdatest.com/selenium-playground

driver.get(test_url)

## click “Drag & Drop Sliders” under “Progress Bars & Sliders”.

driver.find_element(By.CSS_SELECTOR,"div.pr-30:nth-child(1) > div:nth-child(2) > ul:nth-child(2) > li:nth-child(3) > a:nth-child(1)").click()

## Select the slider “Default value 15” and drag the bar to make it 95

slider = driver.find_element(By.XPATH,'//*[@class="sp__range sp__range-success"]/input')

print(slider.location["x"])
driver.fullscreen_window()

offset_value = 0
while True:
    value = driver.find_element(By.ID,"rangeSuccess").text
    ## validating whether the range value shows 95
    if(value=="95"):
        break

    # move the slider backwards if moved ahead
    if(value>"95"):
        offset_value -=3
    elif(value>"80"):
        offset_value+=3
    else:
        offset_value+=20
    action = ActionChains(driver)
    action.drag_and_drop_by_offset(slider,offset_value, 0)
    action.perform()
    # this prevent an unexpected Error in Actions during loop
    time.sleep(0.5)
    

print("slider moved to 95")
time.sleep(3)
driver.close()

#//*[@id="rangeSuccess"]
# time.sleep(10)
