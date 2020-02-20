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

class TestAutoLoginNetflix():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_autoLoginNetflix(self):
    self.driver.get("https://www.netflix.com/Login?nextpage=http%3A%2F%2Fwww3.netflix.com%2Fbrowse")
    WebDriverWait(self.driver, 30000).until(expected_conditions.presence_of_element_located((By.ID, "id_userLoginId")))
    self.driver.find_element(By.ID, "id_userLoginId").send_keys(self.vars["usernameVar"])
    self.driver.find_element(By.ID, "id_password").send_keys(self.vars["passwordVar"])
    self.driver.find_element(By.CSS_SELECTOR, ".login-button").click()
    WebDriverWait(self.driver, 10000).until(expected_conditions.visibility_of_element_located((By.ID, "id_password")))
    if self.driver.execute_script("return (id=id_password)"):
      print(str("No good"))
    else:
      self.vars["self.vars["credentialsFound"] | Netflix"] = "self.vars["credentialsFound"]"
      print(str("I\'m in!!!!"))
  