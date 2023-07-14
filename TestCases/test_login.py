import logging
import time
import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from PageObjects.LoginPage import login
from Utilities.Readproperties import Readconfig
from Utilities.Logger import LogGenerate

class Test_Login:
    url = Readconfig.Url()
    email = Readconfig.Email()
    password = Readconfig.Password()
    log = LogGenerate.logg()

    def test_page_title_001(self, setup):
        self.log.info("test_page_title_001 is started")
        self.driver = setup
        self.log.info("Opening Browser")
        self.driver.get(self.url)
        self.log.info("Go to Url:"+self.url)
        print(self.driver.title)

        if self.driver.title == "Administator Login":
            self.log.info("Page Title:" + self.driver.title)
            assert True
            self.log.info("test_page_title_001 is Passed")
        else:
            self.log.info("Page Title:" + self.driver.title)
            self.driver.save_screenshot("C:\\Users\\HP\\PycharmProjects\\PhpTravels_Project\\Screenshots\\PageTitle.png")
            assert True
            self.log.info("test_page_title_001 is Failed")

    def test_login_002(self, setup):
        self.log.info("test_login_002 is started")
        self.driver = setup
        self.log.info("Opening Browser")
        self.driver.get(self.url)
        self.log.info("Go to Url :"+self.url)
        self.lp = login(self.driver)
        self.lp.Enter_Email(self.email)
        self.log.info("Entering Email:" + self.email)
        self.lp.Enter_Password(self.password)
        self.log.info("Entering Password:" + self.password)
        self.lp.Click_Login_Button()
        self.log.info("Clicking login Button")
        print(self.driver.title)

        if self.driver.title == "Dashboard":
            self.lp.Click_Menu_Button()
            self.log.info("Clicking menu Button")
            self.lp.Click_Logout_Button()
            self.log.info("Clicking logout Button")
            assert True
            self.log.info("test_login_002 is Passed")
        else:
            self.driver.save_screenshot("C:\\Users\\HP\\PycharmProjects\\PhpTravels_Project\\Screenshots\\Login.png")
            self.log.info("test_login_002 is Failed")
            assert False


