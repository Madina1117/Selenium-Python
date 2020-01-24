from selenium import webdriver

# browser exposes executable file
# through selenium test we need to invoke executable file which will then invoke the actual browser

driver = webdriver.Chrome(executable_path="/Users/madinaochilova/Downloads/chromedriver")
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/")  # get method to hit url on browser
driver = webdriver.Firefox(executable_path="/Users/madinaochilova/Downloads/geckodriver")
print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.minimize_window()
driver.back()
driver.refresh()
driver.close()
