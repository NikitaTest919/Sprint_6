import pytest
from selenium.webdriver.common.by import By
from pages.main_page import MainPage

def test_questions(driver):
    main_page = MainPage(driver)
    questions = main_page.get_questions()

    for question in questions:
        question.click()
        assert question.find_element(By.CLASS_NAME, "accordion__panel").is_displayed(), "Текст не отображается"
