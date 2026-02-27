import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from .photo import get_title
from device_context import DeviceContext

def get_latest_file(wait, driver) -> WebElement | None:
    """
    获取最近一个文件，如果没有找到，返回空
    :return: None
    """
    print("-------------------------查找最近一个照片/视频-------------------------")
    i = 1
    while True:
        try:
            # 找到最近一个照片/视频
            print(f"--------第{i}次查找--------")
            file: WebElement = wait.until(EC.presence_of_element_located((By.XPATH, '(//android.widget.ImageView[@resource-id="com.inreii.neutralapp:id/image"])[1]')))
            print("--------已找到最近一张照片/视频--------")
            return file
        except (InvalidElementStateException, NoSuchElementException, TimeoutException):
            if i == 3:
                print("--------没有照片/视频存在--------")
                break
            # 没有找到的话向下滑动刷新
            driver.swipe(DeviceContext.WIDTH * 0.5, DeviceContext.HEIGHT * 0.25, DeviceContext.WIDTH * 0.5, DeviceContext.HEIGHT * 0.75)
            i += 1
    return None

def get_all_titles(wait, driver, n: int) -> list[str] | None:
    """
    找到相册里前n个照片/视频标题，照片/视频数不足n，返回全部照片/视频
    :param driver:
    :param wait:
    :param n:
    :return:
    """
    print("查找相册里前n个照片/视频")
    files_titles: list[str] = []
    # 找到第一个照片/视频
    latest_file = get_latest_file(wait, driver)

    # 如果至少存在一个照片/视频
    if latest_file:
        # 进入第一个照片/视频详情
        latest_file.click()
        last_file_title: str = get_title(wait)

        i = 1
        while n:
            print(f"第 {i} 个照片/视频标题：", last_file_title)

            files_titles.append(last_file_title)

            # 向左滑
            driver.swipe(DeviceContext.WIDTH * 0.75, DeviceContext.HEIGHT * 0.5, DeviceContext.WIDTH * 0.25, DeviceContext.HEIGHT * 0.5)

            time.sleep(1)

            if last_file_title == get_title(wait):  # 如果照片/视频标题没有变化，说明到了最后一个，跳出循环
                break
            else:
                last_file_title: str = get_title(wait)  # 否则，将照片/视频标题赋给last_file_title
            n -= 1
            i += 1

        return files_titles

    return None

def get_files_number(driver,wait) -> int:
    """
    获取相册文件数量
    :param driver:
    :param wait:
    :return:
    """
    previous_page_source = ''
    count = 1
    while True:
        # 循环找到当前页面展示最后一个文件
        try:
            file = wait.until(EC.presence_of_all_elements_located((By.XPATH,f'(//android.widget.ImageView[@resource-id="com.inreii.neutralapp:id/image"])[{count}]')))
            count += 1
        # 没找到判断当前页面是否是最后一页，不是的话向上滑；是的话退出循环
        except:
            if driver.page_source != previous_page_source:
                previous_page_source = driver.page_source
                driver.swipe(DeviceContext.WIDTH * 0.5, DeviceContext.HEIGHT * 0.75, DeviceContext.WIDTH * 0.5, DeviceContext.HEIGHT * 0.25)
            else:
                break
    return count - 1

def edit_files(wait):
    """
    点击右上角编辑按钮
    :param wait:
    :return:
    """
    edit: WebElement = wait.until(EC.presence_of_element_located((By.ID,'com.inreii.neutralapp:id/bianji')))
    edit.click()

def get_day_check_button(wait) -> WebElement:
    """
    获取按天选择照片按钮
    :param wait:
    :return:
    """
    return wait.until(EC.presence_of_element_located((By.ID,'com.inreii.neutralapp:id/dayCheck')))

def check_files_by_day(wait):
    """
    按天选择照片
    :param wait:
    :return:
    """
    day_check = get_day_check_button(wait)
    day_check.click()

def collect_file(wait):
    """
    收藏照片/视频
    :param wait:
    :return:
    """
    collect = wait.until(EC.presence_of_element_located((By.ID,'com.inreii.neutralapp:id/bottom_shoucang')))
    collect.click()

def delete_file(wait):
    """
    删除照片/视频
    :param wait:
    :return:
    """
    delete = wait.until(EC.presence_of_element_located((By.ID,'com.inreii.neutralapp:id/button_delete')))
    delete.click()

def confirm_delete_file(wait):
    """
    确认删除照片/视频
    :param wait:
    :return:
    """
    pass

def get_sign_no_photo_video(wait) -> None:
    """
    获取没有照片/视频标志
    :param wait:
    :return:
    """
    sign = wait.until(EC.presence_of_element_located((By.XPATH,'//android.widget.TextView[@text="No pictures or reports"]')))