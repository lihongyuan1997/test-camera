from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, InvalidElementStateException

import utility


def find_latest_report(wait, driver) -> WebElement | None:
    """
    获取最近一个报告，如果没有找到，返回空
    :return: None
    """
    i = 0
    while i < 3:
        try:
            # 找到最近一个报告
            report: WebElement = wait.until \
                (method=EC.presence_of_element_located \
                    (locator=(By.XPATH, '(//android.widget.RelativeLayout[@resource-id="com.inreii.neutralapp:id/rpImageMain"])[1]/android.widget.RelativeLayout')))
            print("第一个报告元素：", report)
            return report
        except (InvalidElementStateException, NoSuchElementException, TimeoutException):
            print(f"第 {i} 次没找到第一个报告")
            if i == 2:
                print("第一个报告不存在")
            # 没有找到的话向下滑动刷新
            utility.swipe_y_1_4_to_y_3_4(driver)
            i += 1
    return None

def get_all_reports(wait, driver) -> list[str] | None:
    """
    获取所有报告标题
    :param wait:
    :param driver:
    :return:
    """
    previous_page_source: str = ''
    titles_str_all: list[str] = []
    count: int = 1
    while True:
        try:
            # 页面不再变化，退出循环
            if driver.page_source == previous_page_source:
                break
            # 否则记录当前页面
            previous_page_source: str = driver.page_source

            print(f"第{count}次查找报告标题")

            # 寻找当前页面所有报告标题
            titles_ele: list[WebElement] = wait.until \
                (method=EC.presence_of_all_elements_located \
                    (locator=(By.XPATH, '//android.widget.TextView[@resource-id="com.inreii.neutralapp:id/rpName"]')))
            titles_str: list[str] = [title_ele.text for title_ele in titles_ele]
            titles_str_all.extend(titles_str)

            # 向上滑
            utility.swipe_y_3_4_to_y_1_4(driver)
            count += 1
        except(TimeoutException, InvalidElementStateException, NoSuchElementException):
            return None
    return titles_str_all
