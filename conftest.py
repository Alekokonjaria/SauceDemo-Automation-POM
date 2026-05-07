import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    chrome_options = Options()

    # ბრაუზერის კონფიგურაცია
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--headless")
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


def pytest_sessionfinish(session, exitstatus):
    env_info = (
        "Browser=Chrome\n"
        "Browser.Version=Latest\n"
        "Stand=Production\n"
        "Python.Version=3.12\n"
    )

    results_dir = "allure-results"
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)

    with open(os.path.join(results_dir, "environment.properties"), "w") as f:
        f.write(env_info)