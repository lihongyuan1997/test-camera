from selenium.common import NoSuchElementException, TimeoutException, InvalidElementStateException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC


def get_title(wait) -> str:
    """
    获取文件标题
    :return:
    """
    # 获取标题
    file_title: WebElement = wait.until(EC.presence_of_element_located((By.ID, "com.inreii.neutralapp:id/title_content")))
    return file_title.text

def get_photo_view(wait) -> WebElement:
    """
    返回照片主体元素
    :param wait:
    :return:
    """
    return wait.until(EC.presence_of_element_located((By.ID,"com.inreii.neutralapp:id/edit_surface_view")))

def enter_analysis(wait) -> None:
    """
    进入离线分析
    :param wait:
    :return:
    """
    # 获取离线分析图标并点击
    analysis: WebElement = wait.until(EC.presence_of_element_located((By.ID, "com.inreii.neutralapp:id/offlinetext")))
    analysis.click()

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

def call_thermal_ruler(wait) -> None:
    """
    调用等温尺
    :param wait:
    :return:
    """
    call_ruler: WebElement = wait.until \
        (method=EC.presence_of_element_located \
            (locator=(By.ID, "com.inreii.neutralapp:id/isothermalscaleAll")))
    call_ruler.click()

def get_thermal_ruler(wait) -> WebElement:
    """
    获取等温尺
    :param wait:
    :return:
    """
    ruler: WebElement = wait.until \
        (method=EC.presence_of_element_located \
            (locator=(By.ID, "com.inreii.neutralapp:id/sb_vertical_4")))
    print('----------------------已获取等温尺----------------------')
    return ruler

class Analysis:

    @staticmethod
    def get_pallete_icon(wait) -> WebElement:
        """
        获取色板栏图标
        :param wait:
        :return:
        """
        pallete: WebElement = wait.until \
            (method=EC.presence_of_element_located \
                (locator=(By.ID, "com.inreii.neutralapp:id/mOneImg")))
        return pallete

    @staticmethod
    def call_pallete(wait) -> None:
        """
        展示色板栏
        :param wait:
        :return:
        """
        pallete: WebElement = Analysis.get_pallete_icon(wait)
        pallete.click()

    @staticmethod
    def get_emissivity_icon(wait) -> WebElement:
        """
        获取发射率图标
        :param wait:
        :return:
        """
        emissivity: WebElement = wait.until \
            (method=EC.presence_of_element_located \
                (locator=(By.ID, "com.inreii.neutralapp:id/mTwoImg")))
        return emissivity

    @staticmethod
    def call_emissivity(wait) -> None:
        """
        展示发射率列表
        :param wait:
        :return:
        """
        emissivity: WebElement = Analysis.get_emissivity_icon(wait)
        emissivity.click()

    @staticmethod
    def get_point_icon(wait) -> WebElement:
        """
        获取点图标
        :param wait:
        :return:
        """
        point: WebElement = wait.until \
            (method=EC.presence_of_element_located \
                (locator=(By.ID, "com.inreii.neutralapp:id/mThree")))
        return point

    @staticmethod
    def choose_point(wait) -> None:
        """
        选择点标注
        :param wait:
        :return:
        """
        point: WebElement = Analysis.get_point_icon(wait)
        point.click()

    @staticmethod
    def get_line_icon(wait) -> WebElement:
        """
        获取线图标
        :param wait:
        :return:
        """
        line: WebElement = wait.until \
            (method=EC.presence_of_element_located \
                (locator=(By.ID, "com.inreii.neutralapp:id/mFour")))
        return line

    @staticmethod
    def choose_line(wait) -> None:
        """
        选择线标注
        :param wait:
        :return:
        """
        line: WebElement = Analysis.get_line_icon(wait)
        line.click()

    @staticmethod
    def get_rectangle_icon(wait) -> WebElement:
        """
        获取框图标
        :param wait:
        :return:
        """
        rectangle: WebElement = wait.until \
            (method=EC.presence_of_element_located \
                (locator=(By.ID, "com.inreii.neutralapp:id/mFive")))
        return rectangle

    @staticmethod
    def choose_rectangle(wait) -> None:
        """
        选择框标注
        :param wait:
        :return:
        """
        rectangle: WebElement = Analysis.get_rectangle_icon(wait)
        rectangle.click()

    @staticmethod
    def get_textbox_icon(wait) -> WebElement:
        """
        获取文本框图标
        :param wait:
        :return:
        """
        textbox: WebElement = wait.until \
            (method=EC.presence_of_element_located \
                (locator=(By.ID, "com.inreii.neutralapp:id/mSevenImg")))
        return textbox

    @staticmethod
    def choose_textbox(wait) -> None:
        """
        选择文本框标注
        :param wait:
        :return:
        """
        textbox: WebElement = Analysis.get_textbox_icon(wait)
        textbox.click()

    @staticmethod
    def get_clear_icon(wait) -> WebElement:
        """
        获取清除图标
        :param wait:
        :return:
        """
        clear: WebElement = wait.until \
            (method=EC.presence_of_element_located \
                (locator=(By.ID, "com.inreii.neutralapp:id/mEightImg")))
        return clear

    @staticmethod
    def clear_all(wait) -> None:
        """
        清除所有标注
        :param wait:
        :return:
        """
        clear: WebElement = Analysis.get_clear_icon(wait)
        clear.click()

class AnalysisPallete:
    PALLETE: dict[str:str] = {
        "baire": "com.inreii.neutralapp:id/baire_mode_button1",  # 白热
        "heire": "com.inreii.neutralapp:id/ib_heire1",  # 黑热
        "hongtou": "com.inreii.neutralapp:id/ib_hongtou1",  # 红头
        "tiehong": "com.inreii.neutralapp:id/ib_tiehong1",  # 铁红
        "gaocaihong": "com.inreii.neutralapp:id/ib_gaocaihong1",  # 高彩虹
        "caihong": "com.inreii.neutralapp:id/ib_caihong1",  # 彩虹
        "tiehui": "com.inreii.neutralapp:id/ib_tiehui1",  # 铁灰
        }

    @staticmethod
    def swipe_pallete_row_right(driver, photo_ele: WebElement):
        """
        向右滑动色板栏
        :param photo_ele:
        :param driver:
        :return:
        """
        # 确定色板栏纵坐标
        axis_y = photo_ele.location['y'] + photo_ele.size['height'] - 100

        # 向右滑动
        driver.swipe(0, axis_y, photo_ele.size['width'], axis_y)

    @staticmethod
    def swipe_pallete_row_left(driver, photo_ele: WebElement):
        """
        向左滑动色板栏
        :param photo_ele:
        :param driver:
        :return:
        """
        # 确定色板栏纵坐标
        axis_y = photo_ele.location['y'] + photo_ele.size['height'] - 100

        # 向右滑动
        driver.swipe(photo_ele.size['width'] * 0.75, axis_y, photo_ele.size['width'] * 0.25, axis_y)

    @staticmethod
    def choose_palette(wait, driver, photo: WebElement, palette: str) -> None:
        """
        选择色板
        :param palette:
        :param photo:
        :param driver:
        :param wait:
        :return:
        """
        count = 0
        while True:
            try:
                # 找到具体色板元素
                palette_ele: WebElement = wait.until \
                    (method=EC.presence_of_element_located \
                        (locator=(By.ID, AnalysisPallete.PALLETE[palette])))
                # 选择色板
                palette_ele.click()
                print(f"--------已选择{palette}色板--------")
                break
            # 没找到向左滑
            except (NoSuchElementException, TimeoutException, InvalidElementStateException):
                AnalysisPallete.swipe_pallete_row_left(driver, photo)
                count += 1
                if count == 3:
                    assert False, f"--------找不到{palette}色板--------"