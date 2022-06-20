import time
import pytest

from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomer import AddCustomer
from pageObjects.SearchCustomer import SearchCustomer


class TestSearchCustomer004:
    baseurl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByEmail(self, setup):
        self.logger.info("*************** TestSearchCustomer004 ***************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*************** Login Successful ***************")

        self.addCust = AddCustomer(self.driver)
        self.addCust.clickOnCustomer()
        self.addCust.clickOnCustomersMenu()

        self.logger.info(
            "*************** Starting Search Customer By Email ***************"
        )

        self.logger.info("*************** Searching Customer By Email ***************")

        self.searchCust = SearchCustomer(self.driver)
        self.searchCust.setEmail("james_pan@nopCommerce.com")
        self.searchCust.clickSearch()
        time.sleep(5)
        status = self.searchCust.searchByEmail("james_pan@nopCommerce.com")
        assert True == status
        self.logger.info(
            "*************** TC_SearchCustomerByEmail_004 Finished ***************"
        )

        self.driver.close()

    def test_searchCustomerByName(self, setup):
        self.logger.info("*************** TestSearchCustomer004 ***************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*************** Login Successful ***************")

        self.addCust = AddCustomer(self.driver)
        self.addCust.clickOnCustomer()
        self.addCust.clickOnCustomersMenu()

        self.logger.info(
            "*************** Starting Search Customer By Name ***************"
        )

        self.logger.info("*************** Searching Customer By Name ***************")

        self.searchCust = SearchCustomer(self.driver)
        self.searchCust.setFirstName("Steve")
        self.searchCust.setLastName("Gates")
        self.searchCust.clickSearch()
        time.sleep(5)
        status = self.searchCust.searchByName("Steve Gates")
        assert True == status
        self.logger.info(
            "*************** TC_SearchCustomerByName_004 Finished ***************"
        )

        self.driver.close()
