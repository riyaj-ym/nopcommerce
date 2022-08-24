import time

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import xlUtils


class TestLogin002DDT:
    baseurl = ReadConfig.getApplicationUrl()
    path = "C:\\Users\\USER\\Desktop\\Login.xlsx"
    sheet = "Sheet1"
    logger = LogGen.loggen()

    def test_login_ddt(self, setup):
        self.logger.info("*************** TestLogin002DDT ***************")
        self.logger.info("*************** Verifying Login DDT Test ***************")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseurl)
        self.lp = LoginPage(self.driver)

        self.rows = xlUtils.getRowCount(self.path, self.sheet)

        list_status = []  # Empty list

        for r in range(2, self.rows + 1):
            self.user = xlUtils.readData(self.path, self.sheet, r, 1)
            self.password = xlUtils.readData(self.path, self.sheet, r, 2)
            self.exp = xlUtils.readData(self.path, self.sheet, r, 3)

            self.lp.setUsername(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("*************** Passed ***************")
                    self.lp.clickLogout()
                    list_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("*************** Failed ***************")
                    self.lp.clickLogout()
                    list_status.append("Fail")

            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("*************** Failed ***************")
                    list_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("*************** Passed ***************")
                    list_status.append("Pass")
            for i in list_status:
                xlUtils.writeData(self.path, self.sheet, r, 4, i)

        if "Fail" not in list_status:
            self.logger.info("*************** Login DDT Test Passed ***************")
            self.driver.close()
            assert True

        else:
            self.logger.info("*************** Login DDT Test Failed ***************")
            self.driver.close()
            assert False

        self.logger.info("*************** End of Login DDT Test ***************")
        self.logger.info("*************** Completed TestLogin002DDT ***************")

    # self.lp.clickLogout()
    # 'pytest -s -v --html=Reports\report.html'

    # 'pytest -v -rA --html=Reports\report.html test_login_ddt.py'
