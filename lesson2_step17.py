from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)
    
    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    #Scroll to footer
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    #calculation
    
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    
        #Click on the button
    button = browser.find_element_by_id("solve")
    button.click()
    
    
finally:
    time.sleep(15)
    browser.quit()
    
