import os,time
from instaclient import InstaClient
from instaclient.errors import *


def connect(username,pwd):
  client = InstaClient(str(os.getcwd())+"/var/chromedrvier")
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

connect("","")
