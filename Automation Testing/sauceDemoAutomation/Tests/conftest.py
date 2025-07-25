import pytest
from utils.driver_setup import get_driver


@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()
