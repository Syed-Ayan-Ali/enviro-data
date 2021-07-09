from selenium import webdriver
from time import sleep
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get('http://127.0.0.1:5500/map.htm')
sleep(0.35)

driver.get_screenshot_as_file("screenshot.png")
driver.quit()
print("end...")