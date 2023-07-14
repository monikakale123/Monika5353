import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from PageObjects.LoginPage import login
from PageObjects.AddCust_Page import Add_Customer
from Utilities.Readproperties import Readconfig


class Test_AddCust:
    url = Readconfig.Url()
    email = Readconfig.Email()
    password = Readconfig.Password()

    def test_addcust_003(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.lp = login(self.driver)
        self.lp.Enter_Email(self.email)
        self.lp.Enter_Password(self.password)
        self.lp.Click_Login_Button()
        time.sleep(2)
        self.ac = Add_Customer(self.driver)
        self.ac.Click_MenuBar()
        self.ac.Click_Accounts()
        self.ac.Click_Customers()
        self.ac.Click_Add()
        self.ac.Enter_First_name("Monika")
        self.ac.Enter_Last_name("Kale")
        self.ac.Enter_Email("admin@phptravels.com")
        self.ac.Enter_Password("demoadmin")
        self.ac.Enter_Mobile("9898989898")
        time.sleep(2)
        self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[2]/div[2]/main[1]/div[1]/form[1]/div[1]/div[1]/div["
                                          "1]/div[1]/div[3]/div[6]/div[1]/div[1]/a[1]/span[1]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@class='select2-input select2-focused']").send_keys("India")
        time.sleep(2)
        Select(self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[3]")).select_by_index(1)
        time.sleep(2)

        # self.ac.Click_Country(2)
        self.ac.Enter_Address1("Pune")
        self.ac.Enter_Address2("411061")
        self.ac.Click_Email_news_checkbox()
        self.ac.Click_Currency(2)
        self.ac.Select_Vendor1()
        self.ac.Enter_Balance("1000")
        self.ac.Save()


