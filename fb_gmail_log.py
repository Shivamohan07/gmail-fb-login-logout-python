# gmail-fb-login-logout-python
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import pyxhook
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://www.gmail.com");
driver.find_element_by_id('Email').send_keys('shivamohan07@gmail.com')
driver.find_element_by_id('next').click()
driver.find_element_by_id('Passwd').send_keys('gmail pass')
driver.find_element_by_id('signIn').click()
driver.find_element_by_tag_name("body").send_keys(Keys.CONTROL + "t");
driver.get("http://www.facebook.com")
driver.find_element_by_id('email').send_keys('shivamohan07@yahoo.co.in')
driver.find_element_by_id('pass').send_keys('facebook pass')
driver.find_element_by_id('u_0_w').click()



def OnKeyPress(event):
  if event.Ascii==126:      # ~
    driver.find_element_by_id('userNavigationLabel').click()
    time.sleep(5)
    driver.find_element_by_partial_link_text('Log Out').click()
    driver.find_element_by_tag_name("body").send_keys(Keys.CONTROL + "t");
    driver.get("https://accounts.google.com/Logout?hl=en&continue=https%3A%2F%2Fmail.google.com%2Fmail&service=mail&timeStmp=1459360778&secTok=*");
    new_hook.cancel()
    driver.close()


new_hook=pyxhook.HookManager()
new_hook.KeyDown=OnKeyPress
#hook the keyboard
new_hook.HookKeyboard()
#start the session
new_hook.start()
