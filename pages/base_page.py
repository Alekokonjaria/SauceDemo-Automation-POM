import os
from datetime import datetime
from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find(self, locator):
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            self.takescreenshot(f"error_{locator[1]}")
            
    def click(self, locator):
        self.find(locator).click()

    def write(self, locator, text):
        self.find(locator).send_keys(text)

    def get_text(self, locator):
        return self.find(locator).text

    def take_screenshot(self, name):
        if not os.path.exists("screenshots"):
            os.mkdir("screenshots")

        now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        path = f"screenshots/{name}-{now}.png"
        self.driver.save_screenshot(path)
        print(f"screenshot saved at: {path}")

