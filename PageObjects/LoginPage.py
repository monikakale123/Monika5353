import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class login:
    Text_Email_XPATH = (By.XPATH, "//input[@type='text']")
    Text_Password_XPATH = (By.XPATH, "//input[@name='password']")
    Click_Login_Button_XPATH = (By.XPATH, "//span[normalize-space()='Login']")
    Click_Menu_Button_XPATH = (By.XPATH, "//i[@class='material-icons'][normalize-space()='person']")
    Click_Logout_Button_XPATH = (By.XPATH, "//div[normalize-space()='Logout']")

    def __init__(self, setup):
        self.driver = setup
        self.wait = WebDriverWait(self.driver, 10, poll_frequency=1)

    def Enter_Email(self, email):
        self.driver.find_element(*login.Text_Email_XPATH).send_keys(email)

    def Enter_Password(self, password):
        self.driver.find_element(*login.Text_Password_XPATH).send_keys(password)

    def Click_Login_Button(self):
        self.driver.find_element(*login.Click_Login_Button_XPATH).click()

    def Click_Menu_Button(self):
            self.driver.find_element(*login.Click_Menu_Button_XPATH).click()

    def Click_Logout_Button(self):
        self.driver.find_element(*login.Click_Logout_Button_XPATH).click()
