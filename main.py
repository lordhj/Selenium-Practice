from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_driver_path = "C:\software\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path = chrome_driver_path)
#driver.get("https://www.python.org") Getting to the URL

#Clicking automate
"""driver.get("https://en.wikipedia.org/wiki/Thor:_Love_and_Thunder")
valk = driver.find_element(By.LINK_TEXT, "Valkyrie")
valk.click()"""

#Searching Automate
driver.get("https://www.wikipedia.org/")
search_bar = driver.find_element(By.NAME, "search")
search_bar.send_keys("python")
search_bar.send_keys(Keys.ENTER)

#driver.quit()