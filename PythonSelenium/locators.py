from select import select

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="/Users/madinaochilova/Downloads/chromedriver")
driver.get("https://rahulshettyacademy.com/angularpractice")  # get method to hit url on browser

#driver.find_element_by_name("name").send_keys("Rahul")
driver.find_element_by_css_selector("input[name='name']").send_keys("Rahul")
driver.find_element_by_name("email").send_keys("Shetty")

driver.find_element_by_id("exampleCheck1").click()

# select class provides the methods to handle the options in dropdown

dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))  # creating an object in python
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)



driver.find_element_by_xpath("//input[@type='submit']").click()
message = driver.find_element_by_class_name("alert-success").text

assert "success" in message



