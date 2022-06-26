from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
        print("Launching chrome browser.....")
    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("Launching firefox browser.....")
    else:
        driver = webdriver.Edge()
        print("Launching edge browser.....")
    return driver


def pytest_addoption(parser):  # This will get value from CLI /hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the Browser value to set up method
    return request.config.getoption("--browser")


############ pytest HTML Reports ############

# it is hook for adding Enviroment info to HTML Report
def pytest_configure(config):
    config._metadata["Project Name"] = "nop Commerce"
    config._metadata["Module Name"] = "customer"
    config._metadata["Tester"] = "Akash"


# it is hook for delete/modify Environment info to HTML Report
@pytest.mark.optonalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugis", None)
