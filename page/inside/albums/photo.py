from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC


def find_file_title(wait) -> str:
    """
    获取文件标题
    :return:
    """
    # 获取标题
    file_title: WebElement = wait.until \
        (method=EC.presence_of_element_located \
            (locator=(By.ID, "com.inreii.neutralapp:id/title_content")))
    return file_title.text

def click_generate_report(wait) -> None:
    """
    点击生成报告
    :param wait:
    :return:
    """
    reporting: WebElement = wait.until \
        (method=EC.presence_of_element_located \
            (locator=(By.ID, "com.inreii.neutralapp:id/addreportAll")))
    reporting.click()

def confirm_generate_report(wait) -> None:
    """
    确认生成报告
    :param wait:
    :return:
    """
    sure: WebElement = wait.until \
        (method=EC.presence_of_element_located \
            (locator=(By.ID, "com.inreii.neutralapp:id/positive")))
    sure.click()

def cancel_generate_report(wait) -> None:
    """
    取消生成报告
    :param wait:
    :return:
    """
    cancel: WebElement = wait.until \
        (method=EC.presence_of_element_located \
            (locator=(By.ID, "com.inreii.neutralapp:id/negtive")))
    cancel.click()