from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, InvalidElementStateException
from device_context import DeviceContext


def find_latest_report(wait, driver) -> WebElement | None:
    """
    获取最近一个报告，如果没有找到，返回空
    :return: None
    """
    print("查找最近一个报告")
    i = 1
    while True:
        try:
            # 找到最近一个报告
            print(f"第{i}次查找")
            report: WebElement = wait.until \
                (method=EC.presence_of_element_located \
                    (locator=(By.XPATH, '(//android.widget.RelativeLayout[@resource-id="com.inreii.neutralapp:id/rpImageMain"])[1]/android.widget.RelativeLayout')))
            return report
        except (InvalidElementStateException, NoSuchElementException, TimeoutException):
            if i == 3:
                print("报告不存在")
                break
            # 没有找到的话向下滑动刷新
            driver.swipe(DeviceContext.WIDTH * 0.5, DeviceContext.HEIGHT * 0.25, DeviceContext.WIDTH * 0.25, DeviceContext.HEIGHT * 0.75)
            i += 1
    return None

def get_all_reports(wait, driver) -> list[str] | None:
    """
    获取所有报告标题
    :param wait:
    :param driver:
    :return:
    """
    print("查找所有报告")
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

            print(f"第{count}次查找报告")

            # 寻找当前页面所有报告标题
            titles_ele: list[WebElement] = wait.until \
                (method=EC.presence_of_all_elements_located \
                    (locator=(By.XPATH, '//android.widget.TextView[@resource-id="com.inreii.neutralapp:id/rpName"]')))
            titles_str: list[str] = [title_ele.text for title_ele in titles_ele]
            titles_str_all.extend(titles_str)

            # 向上滑
            driver.swipe(DeviceContext.WIDTH * 0.5, DeviceContext.HEIGHT * 0.75,DeviceContext.WIDTH * 0.5, DeviceContext.HEIGHT * 0.25)
            count += 1

        except(TimeoutException, InvalidElementStateException, NoSuchElementException):
            print("报告不存在")
            return None

    return titles_str_all
