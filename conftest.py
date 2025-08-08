import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from config import BASE_URL

@pytest.fixture(scope="function")
def driver():
    options = Options()
    # options.add_argument("--headless")  # Раскомментируйте для безголового режима
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    driver.get(BASE_URL)
    yield driver
    driver.quit()
