import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddCustomer:
    lnk_customers_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a"
    lnk_customerItems_xpath = (
        "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a"
    )
    btn_addCustomer_xpath = "/html/body/div[3]/div[1]/form[1]/div/div/a"
    txt_email_xpath = '//input[@id="Email"]'
    txt_password_xpath = '//*[@id="Password"]'
    txt_firstName_xpath = '//input[@id="FirstName"]'
    txt_lastName_xpath = '//input[@id="LastName"]'
    rdo_male_xpath = '//input[@class="form-check-input" and @value="M"]'
    rdo_female_xpath = '//input[@class="form-check-input" and @value="F"]'
    txt_DOB_xpath = '//*[@id="DateOfBirth"]'
    txt_componyName_id = "Company"
    txt_customerRole_xpath = (
        '//*[@id="customer-info"]/div[2]/div[10]/div[2]/div/div[1]/div/div'
    )
    list_roleRegistered_xpath = '//li[text()="Registered"]'
    list_roleAdministrators_xpath = '//li[text()="Administrators"]'
    list_roleForumModerators_xpath = '//li[text()="Forum Moderators"]"]'
    list_roleVendors_xpath = '//li[text()="Vendors"]'
    list_roleGuests_xpath = '//li[text()="Guests"]'
    txt_adminComment_xpath = '//*[@id="AdminComment"]'
    drp_managerOfVendor_xpath = '//*[@id="VendorId"]'
    btn_save_xpath = '//button[@class="btn btn-primary" and @name="save"]'

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomer(self):
        self.driver.find_element(By.XPATH, self.lnk_customers_xpath).click()

    def clickOnCustomersMenu(self):
        self.driver.find_element(By.XPATH, self.lnk_customerItems_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element(By.XPATH, self.btn_addCustomer_xpath).click()

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.txt_email_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.txt_password_xpath).send_keys(password)

    def setFirstName(self, firstName):
        self.driver.find_element(By.XPATH, self.txt_firstName_xpath).send_keys(
            firstName
        )

    def setLastName(self, lastName):
        self.driver.find_element(By.XPATH, self.txt_lastName_xpath).send_keys(lastName)

    def setGender(self, gender):
        if gender == "Male":
            self.driver.find_element(By.XPATH, self.rdo_male_xpath).click()
        elif gender == "Female":
            self.driver.find_element(By.XPATH, self.rdo_female_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.rdo_male_xpath).click()

    def setDOB(self, dob):
        self.driver.find_element(By.XPATH, self.txt_DOB_xpath).send_keys(dob)

    def setComponyName(self, company):
        self.driver.find_element(By.ID, self.txt_componyName_id).send_keys(company)

    def setCustomerRoles(self, role):
        self.driver.find_element(By.XPATH, self.txt_customerRole_xpath).click()
        time.sleep(3)
        if role == "Registered":
            self.listItem = self.driver.find_element(
                By.XPATH, self.list_roleRegistered_xpath
            )
        elif role == "Administrators":
            self.listItem = self.driver.find_element(
                By.XPATH, self.list_roleAdministrators_xpath
            )
        elif role == "Guests":
            self.driver.find_element(
                By.XPATH, '//span[@class="k-select" and @title="delete"]'
            ).click()
            self.listItem = self.driver.find_element(
                By.XPATH, self.list_roleGuests_xpath
            )
        elif role == "Vendors":
            self.listItem = self.driver.find_element(
                By.XPATH, self.list_roleVendors_xpath
            )
        else:
            self.listItem = self.driver.find_element(
                By.XPATH, self.list_roleGuests_xpath
            )
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", self.listItem)

    def setManagerOfVendor(self, value):
        drp = Select(self.driver.find_element(By.XPATH, self.drp_managerOfVendor_xpath))
        drp.select_by_visible_text(value)

    def setAdminComment(self, comment):
        self.driver.find_element(By.XPATH, self.txt_adminComment_xpath).send_keys(
            comment
        )

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.btn_save_xpath).click()


# driver = webdriver.Chrome()
#
# drp = Select(driver.find_element())
#
# drp.select_by_visible_text()
