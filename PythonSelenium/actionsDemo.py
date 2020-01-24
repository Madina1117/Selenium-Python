from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="/Users/madinaochilova/Downloads/chromedriver")
#driver.get("https://www.familysearch.org/en/")

# Action chains
#action = ActionChains(driver)
#action.move_to_element(driver.find_element_by_id("search")).perform()

# action.move_to_element(driver.find_element_by_link_text("Genealogies")).click().perform()

driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
action = ActionChains(driver)
action.context_click(driver.find_element_by_id("double-click")).perform()  # right clicking
action.double_click(driver.find_element_by_id("double-click")).perform()  # double clicking

# alert popup
alert = driver.switch_to.alert
assert "You double clicked me!!!, You got to be kidding me" == alert.text
alert.accept()  # clicking "ok" button in popup dialog


