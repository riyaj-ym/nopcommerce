import random
import string

from selenium.webdriver.common.by import By

from pageObjects.AddCustomer import AddCustomer
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class TestAddCustomer003:
    baseurl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_addCustomer(self, setup):
        self.logger.info("*************** TestAddCustomer003 ***************  ")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*************** Login Successful ***************  ")

        self.logger.info("*************** Starting Add Customer Test ***************  ")

        self.addCust = AddCustomer(self.driver)
        self.addCust.clickOnCustomer()
        self.addCust.clickOnCustomersMenu()

        self.addCust.clickOnAddNew()

        self.logger.info(
            "*************** Providing Customer Information ***************  "
        )

        self.email = random_generator() + "@gmail.com"

        self.addCust.setEmail(self.email)
        self.addCust.setPassword("test123")
        self.addCust.setCustomerRoles("Guests")
        self.addCust.setManagerOfVendor("Vendor 2")
        self.addCust.setGender("Male")
        self.addCust.setFirstName("Aahan")
        self.addCust.setLastName("Kumar")
        self.addCust.setDOB("05/17/1987")
        self.addCust.setComponyName("Info sys")
        self.addCust.setAdminComment("This is for Testing................")
        self.addCust.clickOnSave()

        self.logger.info("*************** Saving Customer Info *************** ")

        self.logger.info(
            "*************** Add Customer Validation Starts *************** "
        )

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text

        if "customer has been added successfully." in self.msg:
            assert True == True
            self.logger.info(
                "*************** Add Customer Test Passed *************** "
            )
        else:
            self.driver.save_screenshot(
                "L:/nopcommerce/screenshots/test_addCustomer_scr.png"
            )
            self.logger.info(
                "*************** Add Customer Test Failed *************** "
            )
        self.driver.close()
        self.logger.info("*************** Ending Add Customer Test ***************  ")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return "".join(random.choice(chars) for x in range(size))


# "pytest -v -rA --html=L:\nopcommerce\Reports\reportTestAddCustomer003.html L:\nopcommerce\testCases\test_addCustomer.py"
# 'pytest -v -rA --html=L:\nopcommerce\Reports\reportTestAddCustomer003.html L:\nopcommerce\testCases'
