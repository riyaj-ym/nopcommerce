from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import pytest


class TestLogin001:
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    baseurl = ReadConfig.getApplicationUrl()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("*************** TestLogin001 ***************")
        self.logger.info("*************** Verifying HomePage Title ***************")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseurl)
        act_Title = self.driver.title

        if act_Title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info(
                "*************** Home Page Title Test is Passed ***************"
            )
        else:
            self.driver.save_screenshot(
                "L:\\nopcommerce\\screenshots\\test_homePageTitle.png"
            )
            self.logger.error(
                "*************** Home Page Title Test is Failed ***************"
            )
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_loginPageTitle(self, setup):
        self.logger.info("*************** TestLogin001 ***************")
        self.logger.info("*************** Verifying LoginPage Title ***************")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseurl)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title

        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info(
                "*************** Login Page Title Test is Passed ***************"
            )
        else:
            self.driver.save_screenshot(
                "L:\\nopcommerce\\screenshots\\test_loginPageTitle.png"
            )
            self.driver.close()
            self.logger.error(
                "*************** Login Page Title Test is Failed ***************"
            )

            assert False

        # self.lp.clickLogout()
        # 'pytest -s -v --html=Reports\report.html'
