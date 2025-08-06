import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage

@pytest.mark.parametrize("name, surname, address, metro, phone", [
    ("Иван", "Иванов", "Москва, ул. Пушкина, д. 1", "Киевская", "1234567890"),
    ("Петр", "Петров", "Москва, ул. Ленина, д. 2", "Краснопресненская", "0987654321")
])
def test_order_flow(driver, name, surname, address, metro, phone):
    main_page = MainPage(driver)
    main_page.click_order_button()
    
    order_page = OrderPage(driver)
    order_page.fill_order_form(name, surname, address, metro, phone)
    order_page.confirm_order()
    
    assert order_page.is_confirmation_displayed(), "Подтверждение заказа не отображается"
    assert order_page.get_confirmation_text() == "Заказ оформлен", "Неверный текст подтверждения"
