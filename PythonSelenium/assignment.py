

# Verify if search functionality in homepage is working
# type "ber"
# 3 products - x,y,z
# put assertion

import time

from selenium import webdriver

list = []
driver = webdriver.Chrome(executable_path="/Users/madinaochilova/Downloads/chromedriver")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(4)
# validate is 3 products are visible after typing "ber"
count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))  # created customized xpath
assert count == 3
veggies = driver.find_elements_by_xpath("//div[@class='product-name']/button")
# //div[@class='product-action']/button/parent::div/parent::div/h4
for veggie in veggies:
    list.append(veggie.find_element_by_xpath("parent::div/parent::div/h4").text)
    veggie.click()
print(list)