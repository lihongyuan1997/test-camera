import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, InvalidElementStateException
from page import common_utils

def enter_temp_alarm(wait) -> None:
    """
    进入温度告警页面
    :param wait:
    :return:
    """
    temp_alarm: WebElement = wait.until \
        (method=EC.presence_of_element_located \
            (locator=(By.ID, "com.inreii.neutralapp:id/two_img1_msg")))
    temp_alarm.click()

def enter_temp_unit(wait) -> None:
    """
    进入温度单位页面
    :param wait:
    :return:
    """
    temp_unit: WebElement = wait.until \
        (method=EC.presence_of_element_located \
            (locator=(By.ID, "com.inreii.neutralapp:id/two_img2_msg")))
    temp_unit.click()

def enter_temp_switch(wait) -> None:
    """
    进入温度范围切换页面
    :param wait:
    :return:
    """
    temp_switch: WebElement = wait.until \
        (method=EC.presence_of_element_located \
            (locator=(By.ID, "com.inreii.neutralapp:id/two_img4_msg")))
    temp_switch.click()

def enter_temp_parameter(wait) -> None:
    """
    进入温度参数页面
    :param wait:
    :return:
    """
    temp_parameter: WebElement = wait.until \
        (method=EC.presence_of_element_located \
            (locator=(By.ID, "com.inreii.neutralapp:id/two_img3_msg")))
    temp_parameter.click()

def get_auto_shutter_status(wait) -> bool:
    """
    获取自动快门开关状态
    :param wait:
    :return:
    """
    auto_shutter: WebElement = wait.until \
        (method=EC.presence_of_element_located \
            (locator=(By.ID, "com.inreii.neutralapp:id/three_img1_switch")))
    if auto_shutter.get_attribute("checked") == "true":
        return True
    return False

def click_auto_shutter(wait) -> None:
    """
    点击自动快门开关
    :param wait:
    :return:
    """
    auto_shutter: WebElement = wait.until \
        (method=EC.presence_of_element_located \
            (locator=(By.ID, "com.inreii.neutralapp:id/three_img1_switch")))
    auto_shutter.click()

def get_time_watermark_status(wait) -> bool:
    """
    获取时间水印开关状态
    :param wait:
    :return:
    """
    time_watermark: WebElement = wait.until \
        (method=EC.presence_of_element_located \
            (locator=(By.ID, "com.inreii.neutralapp:id/three_img3_switch")))
    if time_watermark.get_attribute("checked") == "true":
        return True
    return False

def click_time_watermark(wait) -> None:
    """
    点击时间水印开关
    :param wait:
    :return:
    """
    time_watermark: WebElement = wait.until \
        (method=EC.presence_of_element_located \
            (locator=(By.ID, "com.inreii.neutralapp:id/three_img3_switch")))
    time_watermark.click()

def get_microphone_status(wait) -> bool:
    """
    获取时间水印开关状态
    :param wait:
    :return:
    """
    microphone: WebElement = wait.until \
        (method=EC.presence_of_element_located \
            (locator=(By.ID, "com.inreii.neutralapp:id/three_img4_switch")))
    if microphone.get_attribute("checked") == "true":
        return True
    return False

def click_microphone(wait) -> None:
    """
    点击麦克风开关
    :param wait:
    :return:
    """
    microphone: WebElement = wait.until \
        (method=EC.presence_of_element_located \
            (locator=(By.ID, "com.inreii.neutralapp:id/three_img4_switch")))
    microphone.click()