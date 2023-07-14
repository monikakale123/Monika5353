from selenium.common import NoSuchElementException, ElementClickInterceptedException, UnexpectedTagNameException, \
    InvalidSelectorException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Add_Customer:
    Click_MenuBar_XPATH = (By.XPATH, "//i[normalize-space()='menu']")
    Click_Accounts_XPATH = (By.XPATH, "/html[1]/body[1]/div[2]/div[1]/nav[1]/div[1]/div[1]/a[6]")
    Click_Customers_XPATH = (By.XPATH, "/html[1]/body[1]/div[2]/div[1]/nav[1]/div[1]/div[1]/div[5]/nav[1]/a[4]")
    Click_Add_XPATH = (By.XPATH, "//button[@type='submit']")
    Text_First_name_XPATH = (By.XPATH, "//input[@placeholder='First name']")
    Text_Last_name_XPATH = (By.XPATH, "//input[@placeholder='Last name']")
    Text_Email_XPATH = (By.XPATH, "//input[@placeholder='Email address']")
    Text_Password_XPATH = (By.XPATH, "//input[@placeholder='Password']")
    Text_Mobile_XPATH = (By.XPATH, "//input[@placeholder='Mobile Number']")
    Click_Country_XPATH = (By.XPATH, "//div[@id='select2-drop-mask']")
    Select_Address1_XPATH = (By.XPATH, "//input[@name='address1']")
    Text_Address2_XPATH = (By.XPATH, "//input[@name='address1']")
    Click_Email_news_checkbox_XPATH = (By.XPATH, "//input[@name='newssub']")
    Click_Currency_XPATH = (By.XPATH, "//select[@name='currency']")
    Select_Vendor1_XPATH = (By.XPATH, "//select[@id='VendorId'][1]")
    Text_Balance_XPATH = (By.XPATH, "//input[@placeholder='Balance']")
    Click_Save_XPATH = (By.XPATH, "//button[@type='submit']")

    def __init__(self, setup):
        self.driver = setup

    def Click_MenuBar(self):
        self.driver.find_element(*Add_Customer.Click_MenuBar_XPATH).click()

    def Click_Accounts(self):
        try:
            self.driver.find_element(*Add_Customer.Click_Accounts_XPATH).click()
        except NoSuchElementException:
            pass

    def Click_Customers(self):
        self.driver.find_element(*Add_Customer.Click_Customers_XPATH).click()

    def Click_Add(self):
        self.driver.find_element(*Add_Customer.Click_Add_XPATH).click()

    def Enter_First_name(self, firstname):
        self.driver.find_element(*Add_Customer.Text_First_name_XPATH).send_keys(firstname)

    def Enter_Last_name(self, lastname):
        self.driver.find_element(*Add_Customer.Text_Last_name_XPATH).send_keys(lastname)

    def Enter_Email(self, email):
        self.driver.find_element(*Add_Customer.Text_Email_XPATH).send_keys(email)

    def Enter_Password(self, password):
        self.driver.find_element(*Add_Customer.Text_Password_XPATH).send_keys(password)

    def Enter_Mobile(self, mob):
        self.driver.find_element(*Add_Customer.Text_Mobile_XPATH).send_keys(mob)

    def Click_Country(self, c):
        try:
            cntry = Select(self.driver.find_element(*Add_Customer.Click_Country_XPATH))
            c.select_by_index(cntry)
        except NoSuchElementException:
            pass
        except ElementClickInterceptedException:
            pass
        except UnexpectedTagNameException:
            pass
        except InvalidSelectorException:
            pass



    def Enter_Address1(self, add1):
        self.driver.find_element(*Add_Customer.Select_Address1_XPATH).send_keys(add1)

    def Enter_Address2(self, add2):
        self.driver.find_element(*Add_Customer.Text_Address2_XPATH).send_keys(add2)

    def Click_Email_news_checkbox(self):
        self.driver.find_element(*Add_Customer.Click_Email_news_checkbox_XPATH).click()

    def Click_Currency(self, r):
        try:
            currency = Select(self.driver.find_element(*Add_Customer.Click_Currency_XPATH))
            r.select_by_index(currency)
        except NoSuchElementException:
            pass

    def Select_Vendor1(self):
        self.driver.find_element(*Add_Customer.Select_Vendor1_XPATH).click()

    def Enter_Balance(self, bal):
        self.driver.find_element(*Add_Customer.Text_Balance_XPATH).send_keys(bal)

    def Save(self):
        self.driver.find_element(*Add_Customer.Click_Save_XPATH).click()
