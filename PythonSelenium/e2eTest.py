from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="/Users/madinaochilova/Downloads/chromedriver")
driver.get("https://rahulshettyacademy.com/angularpractice")

driver.find_element_by_css_selector("a[href*='shop']").click()
products = driver.find_elements_by_xpath("//div[@class='card h-100']")

# //div[@class="card h-100"]/div/h4/a
# product = //div[@class="card h-100"]/div/h4/a
for product in products:
    productName = product.find_element_by_xpath('div/h4/a').text
    if productName == "Blackberry":
        product.find_element_by_xpath("div/button").click()  #  Add item into cart

driver.find_element_by_css_selector("a[class*='btn-primary']").click()
driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
driver.find_element_by_id("country").send_keys("ind")

wait = WebDriverWait(driver,7)  # for th load we need to five wait
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element_by_link_text("India").click()
driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
driver.find_element_by_css_selector("[type='submit']").click()
successText = driver.find_element_by_class_name("alert-success").text

assert "Success! Thank you!" in successText

# taking screenshot using selenium
driver.get_screenshot_as_file("screen.png")  # grab the screenshot and it will store into one file








