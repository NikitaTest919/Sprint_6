from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage

class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderPageLocators()

    def fill_order_form(self, name, surname, address, metro, phone):
        self.send_keys(self.locators.NAME_INPUT, name)
        self.send_keys(self.locators.SURNAME_INPUT, surname)
        self.send_keys(self.locators.ADDRESS_INPUT, address)
        self.send_keys(self.locators.METRO_INPUT, metro)
        self.send_keys(self.locators.PHONE_INPUT, phone)
        self.click(self.locators.NEXT_BUTTON)

    def confirm_order(self):
        self.click(self.locators.CONFIRM_YES_BUTTON)

    def is_confirmation_displayed(self):
        return len(self.find_all(self.locators.CONFIRMATION_MODAL)) > 0

    def get_confirmation_text(self):
        return self.find(self.locators.CONFIRMATION_HEADER).text
