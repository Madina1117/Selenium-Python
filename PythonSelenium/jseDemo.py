
# JS DOM can access any elements on web page just like how selenium does
# Selenium have a method to execute javascript code in it
# js technique is not used heavily at work, whenever selenium technique doe snot work use this technique
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="/Users/madinaochilova/Downloads/chromedriver")
driver.get("https://rahulshettyacademy.com/angularpractice")

driver.find_element_by_name("name").send_keys("hello")
print(driver.find_element_by_name("name").text)
print(driver.find_element_by_name("name").get_attribute("value"))
print(driver.execute_script('return document.getElementsByName("name")[0].value'))  # this is js

shopButton = driver.find_element_by_css_selector("a[href*='shop']")
driver.execute_script("arguments[0].click();", shopButton)

# scroll down the page using js, selenium does not support that
# this is famous interview question
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")   # ";" is treated as complete step, scrolling from beginning till end
