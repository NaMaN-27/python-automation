from selenium import webdriver
import pyautogui
import os 
import time


url = 'https://www.gmail.com'


gmail_username = 'naman.jain19@vit.edu'
gmail_password = 'vit1234$'


driver = webdriver.Chrome('C:/Users/naman/OneDrive/Desktop/automation project/chromedriver.exe')

driver.get(url)

driver.implicitly_wait(60)
driver.find_element_by_id('identifierId').send_keys(gmail_username)
driver.find_element_by_id('identifierNext').click()

driver.implicitly_wait(60)
driver.find_element_by_name('password').send_keys(gmail_password)
driver.find_element_by_id('passwordNext').click()

driver.find_element_by_class_name('gb_la').click()
driver.maximize_window()
driver.find_element_by_id('gb_71').click()