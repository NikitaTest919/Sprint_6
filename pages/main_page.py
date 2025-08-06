from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocators

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.locators = MainPageLocators()

    def click_order_button(self):
        self.driver.find_element(*self.locators.ORDER_BUTTON_TOP).click()

    def click_order_button_bottom(self):
        self.driver.find_element(*self.locators.ORDER_BUTTON_BOTTOM).click()

    def click_logo_scooter(self):
        self.driver.find_element(*self.locators.LOGO_SCOOTER).click()

    def click_logo_yandex(self):
        self.driver.find_element(*self.locators.LOGO_YANDEX).click()

    def get_questions(self):
        return self.driver.find_elements(*self.locators.QUESTIONS)
