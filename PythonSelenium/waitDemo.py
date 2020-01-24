# Implicit wait
# Explicit wait
# pause the test for a few seconds using time class
import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="/Users/madinaochilova/Downloads/chromedriver")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(5)
# wait 5 seconds till object is not displayed
# global wait
# it takes 1,5 seconds to reach the next page - execution will resume in 1.5 seconds
# if object dont show up at all, then max time your test will wait for 5 seconds


driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(4)
# validate is 3 products are visible after typing "ber"
count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))  # created customized xpath
assert count == 3

buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")

for button in buttons:
    button.click()

driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()
# it takes some time promo code to be applied. we will use selenium waits
print(driver.find_element_by_css_selector("span.promoInfo").text)


