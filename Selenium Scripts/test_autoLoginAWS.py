# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestAutoLoginAWS():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_autoLoginAWS(self):
    self.driver.get("https://aws.amazon.com/")
    WebDriverWait(self.driver, 30000).until(expected_conditions.presence_of_element_located((By.XPATH, "//span[contains(.,\'Sign In to the Console\')]")))
    self.driver.find_element(By.XPATH, "//span[contains(.,\'Sign In to the Console\')]").click()
    WebDriverWait(self.driver, 30000).until(expected_conditions.presence_of_element_located((By.ID, "resolving_input")))
    self.driver.find_element(By.ID, "resolving_input").send_keys(self.vars["usernameVar"])
    self.driver.find_element(By.ID, "next_button").click()
    WebDriverWait(self.driver, 30000).until(expected_conditions.presence_of_element_located((By.ID, "password")))
    self.driver.find_element(By.ID, "password").send_keys(self.vars["passwordVar"])
    self.driver.find_element(By.ID, "signin_button").click()
    WebDriverWait(self.driver, 10000).until(expected_conditions.visibility_of_element_located((By.ID, "password")))
    if self.driver.execute_script("return (id=password)"):
      print(str("No good"))
    else:
      self.vars["self.vars["credentialsFound"] | AWS"] = "self.vars["credentialsFound"]"
      print(str("I\'m in!!!!"))
  