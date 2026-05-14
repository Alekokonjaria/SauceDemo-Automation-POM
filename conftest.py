import os

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    chrome_options = Options()

    # Browser Configuration
    chrome_options.add_argument("--incognito")
    #chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)

    prefs = {
        "profile.password_manager_enabled": False,
        "profile.default_content_setting_values.notifications": 2,
        "credentials_enable_service": False
    }
    chrome_options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=chrome_options)

    yield driver
    driver.quit()


def pytest_sessionfinish():
    env_info = (
        "Browser=Chrome\n"
        "Browser.Version=Latest\n"
        "Stand=Production\n"
        "Python.Version=3.12\n"
    )

    results_dir = "allure-results"
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == 'call' and report.failed:
        try:
            driver = item.funcargs["driver"]
            allure.attach(driver.get_screenshot_as_png(),
                              name = "Screenshot_on_Failure",
                              attachment_type=AttachmentType.PNG)
        except Exception as e:
            print(f"Fail to take screenshot: {e}")