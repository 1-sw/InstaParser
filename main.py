
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



def connect(username,pwd):
  client = InstaClient(driver_path=driver_path)
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
  connect(config.LOGIN,config.PASSWORD)
  time.sleep(10)
  driver.close()
main()
