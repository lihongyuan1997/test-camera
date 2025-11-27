from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC

def enter_device(wait) -> None:
    """
    进入设备页面
    :param wait:
    :return:
    """
    device: WebElement = wait.until \
        (method=EC.presence_of_element_located \
            (locator=(By.ID, "com.inreii.neutralapp:id/menu_device")))
    device.click()

def enter_gallery(wait) -> None:
    """
    进入外壳相册
    :param wait:
    :return:
    """
    gallery: WebElement = wait.until \
        (method=EC.presence_of_element_located \
            (locator=(By.ID, "com.inreii.neutralapp:id/menu_gallery")))
    gallery.click()


def enter_setting(wait) -> None:
    """
    进入外壳设置页面
    :param wait:
    :return:
    """
    setting: WebElement = wait.until \
        (method=EC.presence_of_element_located \
            (locator=(By.ID, "com.inreii.neutralapp:id/menu_setting")))
    setting.click()
