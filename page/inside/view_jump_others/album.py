import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, InvalidElementStateException
from page import common_utils

def find_latest_file(wait, driver) -> WebElement | None:
    """
    获取最近一个文件，如果没有找到，返回空
    :return: None
    """
    i = 0
    while i < 3:
        try:
            # 找到最近一个文件
            latest_file: WebElement = wait.until \
                (method=EC.presence_of_element_located \
                    (locator=(By.XPATH, '(//android.widget.ImageView[@resource-id="com.inreii.neutralapp:id/image"])[1]')))
            print("第一个文件元素：", latest_file)
            return latest_file
        except (InvalidElementStateException, NoSuchElementException, TimeoutException):
            print(f"第 {i} 次没找到第一个文件")
            if i == 2:
                print("第一个文件不存在")
            # 没有找到的话向下滑动刷新
            common_utils.swipe_y_1_4_to_y_3_4(driver)
            i += 1
    return None

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

def find_files_titles(wait, driver, n: int) -> list[str] | None:
    """
    找到相册里前N个文件标题，文件数不足N，返回全部文件
    :param driver:
    :param wait:
    :param n:
    :return:
    """
    files_titles: list[str] = []
    # 找到第一个文件
    latest_file = find_latest_file(wait, driver)

    # 如果至少存在一个文件
    if latest_file:
        # 进入第一个文件详情
        latest_file.click()
        last_file_title: str = find_file_title(wait)

        i = 1
        while n:
            print(f"第 {i} 个文件标题：", last_file_title)

            files_titles.append(last_file_title)

            # 向左滑
            common_utils.swipe_x_3_4_to_x_1_4(driver)

            time.sleep(1)

            if last_file_title == find_file_title(wait):  # 如果文件标题没有变化，说明到了最后一个，跳出循环
                break
            else:
                last_file_title: str = find_file_title(wait)  # 否则，将文件标题赋给last_file_title
            n -= 1
            i += 1

        return files_titles

    return None
