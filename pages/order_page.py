from locators.order_page_locators import OrderPageLocators

class OrderPage:
    def __init__(self, driver):
        self.driver = driver
        self.locators = OrderPageLocators()

    def fill_order_form(self, name, surname, address, metro, phone):
        self.driver.find_element(*self.locators.NAME_INPUT).send_keys(name)
        self.driver.find_element(*self.locators.SURNAME_INPUT).send_keys(surname)
        self.driver.find_element(*self.locators.ADDRESS_INPUT).send_keys(address)
        self.driver.find_element(*self.locators.METRO_INPUT).send_keys(metro)
        self.driver.find_element(*self.locators.PHONE_INPUT).send_keys(phone)
        self.driver.find_element(*self.locators.NEXT_BUTTON).click()

    def confirm_order(self):
        self.driver.find_element(*self.locators.CONFIRM_YES_BUTTON).click()

    def is_confirmation_displayed(self):
        return len(self.driver.find_elements(*self.locators.CONFIRMATION_MODAL)) > 0

    def get_confirmation_text(self):
        return self.driver.find_element(*self.locators.CONFIRMATION_HEADER).text
