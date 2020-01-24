from selenium import webdriver
validateText = "Option3"

driver = webdriver.Chrome(executable_path="/Users/madinaochilova/Downloads/chromedriver")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element_by_css_selector("#name").send_keys(validateText)
driver.find_element_by_id("alertbtn").click()
# java script pop up
alert = driver.switch_to.alert  # swiching driver to alert
alertText = alert.text
assert validateText in alertText
print(alert.text)
alert.accept()  # accept method for clicking ok
alert.dismiss() # dismiss method for negative scenarios like "Cancel"
