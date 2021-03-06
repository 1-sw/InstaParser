
import os,time,config

from instaclient import BaseProfile
from instaclient import InstaClient
from instaclient.errors import *

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver_path = str(os.getcwd()+"/var/chromedriver")
driver = webdriver.Chrome(driver_path)

def send_direct_message(usernames=""):
        #It doecnt work
        direct_message_button = ""
        print("Отправляем сообщение...")
        #direct_message = driver.find_element_by_xpath(direct_message_button).click()
        driver.find_element_by_link_text("Direct").click()
        time.sleep(random.randrange(2, 4))

#  selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element:
#  {"method":"xpath","selector":"/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a"}
# (Session info: chrome=87.0.4280.88)


def connect(username,pwd):
  client = InstaClient(driver_path=driver_path)
  print(BaseProfile.from_username("testd_eveloper"))
  #
  try:
    client.login(username=username, password=pwd)
  except VerificationCodeNecessary:
    code = input('Enter the 2FA security code generated by your Authenticator App or sent to you by SMS')
    client.input_verification_code(code)
  except SuspisciousLoginAttemptError as error:
    if error.mode == SuspisciousLoginAttemptError.EMAIL:
      code = input('Enter the security code that was sent to you via email: ')
    else:
      code = input('Enter the security code that was sent to you via SMS: ')
    client.input_security_code(code)


def main():
  print("1")
  connect(config.LOGIN,config.PASSWORD)
  time.sleep(10)
  print("2")
  send_direct_message("1_sw_git")
  time.sleep(10)
  print("3")
  driver.close()
main()
