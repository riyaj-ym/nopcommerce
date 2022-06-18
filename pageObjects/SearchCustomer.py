from selenium.webdriver.common.by import By


class SearchCustomer:
    txt_SearchCustomerByEmail_xpath = (
        '//input[@class="form-control text-box single-line" and @name="SearchEmail"]'
    )
    txt_SearchCustomerByFirstName_xpath = '//input[@id="SearchFirstName"]'
    txt_SearchCustomerByLastName_xpath = '//input[@id="SearchLastName"]'
    btn_SearchCustomer_xpath = '//button[@id="search-customers"]'
    tbl_CustomerTable_xpath = '//*[@id="customers-grid"]'
    tbl_Rows_xpath = '//*[@id="customers-grid"]//tbody/tr'
    tbl_Columns_xpath = '//*[@id="customers-grid"]//tbody/tr/td'

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, Email):
        self.driver.find_element(By.XPATH, self.txt_SearchCustomerByEmail_xpath).clear()
        self.driver.find_element(
            By.XPATH, self.txt_SearchCustomerByEmail_xpath
        ).send_keys(Email)

    def setFirstName(self, FirstName):
        self.driver.find_element(
            By.XPATH, self.txt_SearchCustomerByFirstName_xpath
        ).clear()
        self.driver.find_element(
            By.XPATH, self.txt_SearchCustomerByFirstName_xpath
        ).send_keys(FirstName)

    def setLastName(self, LastName):
        self.driver.find_element(
            By.XPATH, self.txt_SearchCustomerByLastName_xpath
        ).clear()
        self.driver.find_element(
            By.XPATH, self.txt_SearchCustomerByLastName_xpath
        ).send_keys(LastName)

    def clickSearch(self):
        self.driver.find_element(By.XPATH, self.btn_SearchCustomer_xpath).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH, self.tbl_Rows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements(By.XPATH, self.tbl_Columns_xpath))

    def searchByEmail(self, email):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element(By.XPATH, self.tbl_CustomerTable_xpath)
            emailId = table.find_element(
                By.XPATH, '//*[@id="customers-grid"]//tbody/tr["+str(r)+"]/td[2]'
            ).text
            if emailId == email:
                flag = True
                break
        return flag

    def searchByName(self, Name):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element(By.XPATH, self.tbl_CustomerTable_xpath)
            name = table.find_element(
                By.XPATH, '//*[@id="customers-grid"]//tbody/tr["+str(r)+"]/td[3]'
            ).text
            if name == Name:
                flag = True
                break
        return flag
        #


# driver=webdriver.Chrome()
# driver.find_element(By.XPATH,).send_keys()
# 'pytest -v -rA --html=L:\nopcommerce\Reports\report.html L:\nopcommerce\testCases'
