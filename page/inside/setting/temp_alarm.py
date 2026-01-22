from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC

def click_high_temp_alarm(wait) -> None:
    """
    点击高温报警开关
    :param wait:
    :return:
    """
    high_temp_alarm: WebElement = wait.until \
        (method=EC.presence_of_element_located \
            (locator=(By.ID, "com.inreii.neutralapp:id/switch_gwbj")))
    high_temp_alarm.click()

def get_high_temp_alarm_status(wait) -> bool:
    """
    获取高温报警开关状态
    :param wait:
    :return:
    """
    high_temp_alarm: WebElement = wait.until \
        (method=EC.presence_of_element_located \
            (locator=(By.ID, "com.inreii.neutralapp:id/switch_gwbj")))
    return high_temp_alarm.get_attribute("checked") == "true"

def click_low_temp_alarm(wait) -> None:
    """
    点击低温报警开关
    :param wait:
    :return:
    """
    low_temp_alarm: WebElement = wait.until \
        (method=EC.presence_of_element_located \
            (locator=(By.ID, "com.inreii.neutralapp:id/switch_dwbj")))
    low_temp_alarm.click()

def get_low_temp_alarm_status(wait) -> bool:
    """
    获取低温报警开关状态
    :param wait:
    :return:
    """
    low_temp_alarm: WebElement = wait.until \
        (method=EC.presence_of_element_located \
            (locator=(By.ID, "com.inreii.neutralapp:id/switch_dwbj")))
    return low_temp_alarm.get_attribute("checked") == "true"

def click_alarm_sound(wait) -> None:
    """
    点击报警声音开关
    :param wait:
    :return:
    """
    alarm_sound: WebElement = wait.until \
        (method=EC.presence_of_element_located \
            (locator=(By.ID, "com.inreii.neutralapp:id/switch_bjsy")))
    alarm_sound.click()

def get_alarm_sound_status(wait) -> bool:
    """
    获取报警声音开关状态
    :param wait:
    :return:
    """
    alarm_sound: WebElement = wait.until \
        (method=EC.presence_of_element_located \
            (locator=(By.ID, "com.inreii.neutralapp:id/switch_bjsy")))
    return alarm_sound.get_attribute("checked") == "true"

def get_high_temp(wait) -> str:
    """
    获取高温阈值
    :param wait:
    :return:
    """
    high_temp: WebElement = wait.until \
        (method=EC.presence_of_element_located \
            (locator=(By.ID, "com.inreii.neutralapp:id/gwfz_value")))
    return high_temp.text

def input_high_temp(wait, temp: float) -> None:
    """
    输入高温阈值
    :param wait:
    :param temp:
    :return:
    """
    # 找到高温阈值显示值并点击
    high_temp: WebElement = wait.until \
        (method=EC.presence_of_element_located \
            (locator=(By.ID, "com.inreii.neutralapp:id/gwfz_value")))
    high_temp.click()

    # 找到高温阈值输入框并输入温度
    high_temp_input: WebElement = wait.until \
        (method=EC.presence_of_element_located \
            (locator=(By.ID, "com.inreii.neutralapp:id/message")))
    high_temp_input.send_keys(str(temp))

    # 点击确定
    sure: WebElement = wait.until \
        (method=EC.presence_of_element_located \
            (locator=(By.ID, "com.inreii.neutralapp:id/positive")))
    sure.click()

def get_low_temp(wait) -> str:
    """
    获取低温阈值
    :param wait:
    :return:
    """
    low_temp: WebElement = wait.until \
        (method=EC.presence_of_element_located \
            (locator=(By.ID, "com.inreii.neutralapp:id/dwfz_value")))
    return low_temp.text

def input_low_temp(wait, temp: float) -> None:
    """
    输入低温阈值
    :param wait:
    :param temp:
    :return:
    """
    # 找到低温阈值显示值并点击
    low_temp: WebElement = wait.until \
        (method=EC.presence_of_element_located \
            (locator=(By.ID, "com.inreii.neutralapp:id/dwfz_value")))
    low_temp.click()

    # 找到低温阈值输入框并输入温度
    low_temp_input: WebElement = wait.until \
        (method=EC.presence_of_element_located \
            (locator=(By.ID, "com.inreii.neutralapp:id/message")))
    low_temp_input.send_keys(str(temp))

    # 点击确定
    sure: WebElement = wait.until \
        (method=EC.presence_of_element_located \
            (locator=(By.ID, "com.inreii.neutralapp:id/positive")))
    sure.click()