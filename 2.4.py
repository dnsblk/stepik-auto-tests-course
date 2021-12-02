from selenium import webdriver
import time
import os
from selenium.webdriver.common.by import By
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(link)   


    wait = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100"))

    book = browser.find_element_by_id("book")
    book.click()
    
    x = browser.find_element_by_id("input_value").text

    def calc(x):
     return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)

    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    button = browser.find_element_by_css_selector("[type=submit]")
    button.click()

finally:
    time.sleep(20)
    browser.quit()
