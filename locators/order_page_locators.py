from selenium.webdriver.common.by import By

class OrderPageLocators:
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    CONFIRM_YES_BUTTON = (By.XPATH, "//button[text()='Да']")
    CONFIRMATION_MODAL = (By.CLASS_NAME, "Order_Modal__YZ-d3")
    CONFIRMATION_HEADER = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")
