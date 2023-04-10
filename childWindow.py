from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service (r"C:\Users\BHAGYASHRI\Downloads\chromedriver_win32 (1)\chromedriver")
driver =webdriver.Chrome(service=service_obj)
driver.implicitly_wait(3)
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
driver.find_element(By.LINK_TEXT, "Click Here").click()
parentwindow = driver.window_handles
#switch to child window
driver.switch_to.window(parentwindow[1])
print(driver.find_element(By.XPATH, "//h3").text)
driver.close()
#switch to parent window
driver.switch_to.window(parentwindow[0])
print(driver.find_element(By.XPATH, "//h3").text)
assert "Opening a new window" == driver.find_element(By.XPATH, "//h3").text
driver.close()