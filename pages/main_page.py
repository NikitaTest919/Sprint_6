from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators()

    def click_order_button_top(self):
        self.click(self.locators.ORDER_BUTTON_TOP)

    def click_order_button_bottom(self):
        self.click(self.locators.ORDER_BUTTON_BOTTOM)

    def click_logo_scooter(self):
        self.click(self.locators.LOGO_SCOOTER)

    def click_logo_yandex(self):
        self.click(self.locators.LOGO_YANDEX)

    def get_questions(self):
        return self.find_all(self.locators.QUESTIONS)
