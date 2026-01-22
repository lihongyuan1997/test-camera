from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC

def choose_celsius(wait) -> None:
    """
    选择℃
    :param wait:
    :return:
    """
    celsius: WebElement = wait.until \
        (method=EC.presence_of_element_located \
            (locator=(By.ID, "com.inreii.neutralapp:id/ssd")))
    celsius.click()

def choose_fahrenheit(wait) -> None:
    """
    选择℉
    :param wait:
    :return:
    """
    fahrenheit: WebElement = wait.until \
        (method=EC.presence_of_element_located \
            (locator=(By.ID, "com.inreii.neutralapp:id/bt_hua")))
    fahrenheit.click()

def choose_kaierwen(wait) -> None:
    """
    选择K
    :param wait:
    :return:
    """
    kaierwen: WebElement = wait.until \
        (method=EC.presence_of_element_located \
            (locator=(By.ID, "com.inreii.neutralapp:id/bt_k")))
    kaierwen.click()