import pytest
from selene import browser
from selenium import webdriver


# добавляем фикстуры

@pytest.fixture(scope="session")
def browser_settings():
    driver_options = webdriver.ChromeOptions
    driver_options.page_load_strategy = 'normal'
    browser.config.driver_options = driver_options
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    print("Браузер открыт!")

    yield

    print("Закрываем браузер!")
