from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from . import album, photo, report

def enter_album(wait) -> None:
    """
    进入相册页面
    :param wait:
    :return:
    """
    album: WebElement = wait.until \
        (method=EC.presence_of_element_located \
            (locator=(By.ID, "com.inreii.neutralapp:id/album")))
    album.click()

def enter_favorite(wait) -> None:
    """
    进入收藏页面
    :param wait:
    :return:
    """
    favorite: WebElement = wait.until \
        (method=EC.presence_of_element_located \
            (locator=(By.ID, "com.inreii.neutralapp:id/favorites")))
    favorite.click()


def enter_report(wait) -> None:
    """
    进入报告页面
    :param wait:
    :return:
    """
    report: WebElement = wait.until \
        (method=EC.presence_of_element_located \
            (locator=(By.ID, "com.inreii.neutralapp:id/report")))
    report.click()
