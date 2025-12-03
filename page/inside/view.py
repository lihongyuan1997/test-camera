import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, InvalidElementStateException
import common_utils

class Pallete:

    TIEHUI: str = "com.inreii.neutralapp:id/ib_tiehui"
    CAIHONG: str = "com.inreii.neutralapp:id/ib_caihong"
    GAOCAIHONG: str = "com.inreii.neutralapp:id/ib_gaocaihong"
    TIEHONG: str = "com.inreii.neutralapp:id/ib_tiehong"
    HONGTOU: str = "com.inreii.neutralapp:id/ib_hongtou"
    HEIRE: str = "com.inreii.neutralapp:id/ib_heire"
    BAIRE: str = "com.inreii.neutralapp:id/baire_mode_button"
    MOHUI: str = "com.inreii.neutralapp:id/rl_mohui1"
    BINGLENG: str = "com.inreii.neutralapp:id/rl_bingleng1"

    @staticmethod
    def display_palette_row(wait) -> None:
        """
        展示色板栏
        :param wait:
        :return:
        """
        # 找到色板入口元素
        palette: WebElement = wait.until \
            (method=EC.presence_of_element_located \
                (locator=(By.ID, "com.inreii.neutralapp:id/sql_image_sb")))
        # 展示色板
        palette.click()

    @staticmethod
    def get_hongtou_palette(wait) -> WebElement:
        """
        获取红头色板元素
        :param wait:
        :return:
        """
        palette_hongtou: WebElement = wait.until \
            (method=EC.presence_of_element_located \
                (locator=(By.ID, Pallete.HONGTOU)))
        return palette_hongtou

    @staticmethod
    def swipe_palette_row_to_left(wait, driver, palette_hongtou: WebElement) -> None:
        """
        向左滑动色板栏
        :param palette_hongtou: 红头色板元素
        :param wait:
        :param driver:
        :return:
        """

        # 获取红头色板的坐标和尺寸
        x, y, width, height = common_utils.get_element_coordinate_size(palette_hongtou)

        # 获取屏幕指定位置坐标
        specified_position: dict[str: int] = common_utils.get_specified_position(driver)

        # 向左滑动色板栏
        driver.swipe(specified_position['x_3_4'], y + 0.5 * height, 0, y + 0.5 * height)

    @staticmethod
    def swipe_palette_row_to_right(wait, driver, palette_hongtou: WebElement) -> None:
        """
        向右滑动色板栏
        :param palette_hongtou: 红头色板元素
        :param wait:
        :param driver:
        :return:
        """

        # 获取红头色板的坐标和尺寸
        x, y, width, height = common_utils.get_element_coordinate_size(palette_hongtou)

        # 获取屏幕指定位置坐标
        specified_position: dict[str: int] = common_utils.get_specified_position(driver)

        # 向右滑动色板栏
        driver.swipe(specified_position['x_1_4'], y + 0.5 * height, specified_position['x'], y + 0.5 * height)

    @staticmethod
    def choose_palette(wait, driver, palette_name: str) -> None:
        """
        选择色板
        :param driver:
        :param palette_name:
        :param wait:
        :return:
        """
        i = 0
        while i < 2:
            try:
                # 找到具体色板元素
                palette_ele: WebElement = wait.until \
                    (method=EC.presence_of_element_located \
                        (locator=(By.ID, palette_name)))
                # 选择色板
                palette_ele.click()
            # 第一次没找到的处理
            except (NoSuchElementException, TimeoutException, InvalidElementStateException):
                # 找到红头色板
                palette_hongtou: WebElement = Pallete.get_hongtou_palette(wait)

                # 如果是冰冷、墨灰、白热、黑热色板，没找到的话向右滑
                if palette_name in (Pallete.BINGLENG, Pallete.MOHUI, Pallete.BAIRE, Pallete.HEIRE):
                    Pallete.swipe_palette_row_to_right(wait, driver, palette_hongtou)

                # 如果是铁红、高彩虹、彩虹、铁灰色板，没找到的话向左滑
                if palette_name in (Pallete.TIEHONG, Pallete.GAOCAIHONG, Pallete.CAIHONG, Pallete.TIEHUI):
                    Pallete.swipe_palette_row_to_left(wait, driver, palette_hongtou)

                i += 1

class MeasureTempTool:

    @staticmethod
    def click_call_measure_temp_tool_icon(wait) -> None:
        """
        点击测温工具图标，调出测温工具栏
        :param wait:
        :return:
        """
        measure_temp_tool_icon: WebElement = wait.until \
            (method=EC.presence_of_element_located \
                (locator=(By.ID, "com.inreii.neutralapp:id/temp_button")))
        measure_temp_tool_icon.click()

    @staticmethod
    def get_center_temp_icon(wait) -> WebElement:
        """
        获取中心点测温图标
        :param wait:
        :return:
        """
        center_temp_icon: WebElement = wait.until \
            (method=EC.presence_of_element_located \
                (locator=(By.ID, "com.inreii.neutralapp:id/iv_center_temp")))
        return center_temp_icon

    @staticmethod
    def get_max_temp_icon(wait) -> WebElement:
        """
        获取测量最高温图标
        :param wait:
        :return:
        """
        max_temp_icon: WebElement = wait.until \
            (method=EC.presence_of_element_located \
                (locator=(By.ID, "com.inreii.neutralapp:id/iv_max_mini")))
        return max_temp_icon

    @staticmethod
    def get_min_temp_icon(wait) -> WebElement:
        """
        获取测量最低温图标
        :param wait:
        :return:
        """
        min_temp_icon: WebElement = wait.until \
            (method=EC.presence_of_element_located \
                (locator=(By.ID, "com.inreii.neutralapp:id/iv_9square")))
        return min_temp_icon

    @staticmethod
    def get_point_temp_icon(wait) -> WebElement:
        """
        获取测量某一点温度图标
        :param wait:
        :return:
        """
        point_temp_icon: WebElement = wait.until \
            (method=EC.presence_of_element_located \
                (locator=(By.ID, "com.inreii.neutralapp:id/ll_point_mode")))
        return point_temp_icon

    @staticmethod
    def get_line_temp_icon(wait) -> WebElement:
        """
        获取测量线段温度图标
        :param wait:
        :return:
        """
        line_temp_icon: WebElement = wait.until \
            (method=EC.presence_of_element_located \
                (locator=(By.ID, "com.inreii.neutralapp:id/line_mode_button")))
        return line_temp_icon

    @staticmethod
    def get_rectangle_temp_icon(wait) -> WebElement:
        """
        获取测量矩形框温度图标
        :param wait:
        :return:
        """
        rectangle_temp_icon: WebElement = wait.until \
            (method=EC.presence_of_element_located \
                (locator=(By.ID, "com.inreii.neutralapp:id/rectangle_mode_button")))
        return rectangle_temp_icon

    @staticmethod
    def get_del_temp_icon(wait) -> WebElement:
        """
        获取清除点线框温度图标
        :param wait:
        :return:
        """
        del_temp_icon: WebElement = wait.until \
            (method=EC.presence_of_element_located \
                (locator=(By.ID, "com.inreii.neutralapp:id/iv_delete_button")))
        return del_temp_icon

class TempRuler:

    @staticmethod
    def click_call_temp_ruler_icon(wait) -> None:
        """
        点击调用等温尺图标
        :param wait:
        :return:
        """
        call_temp_ruler_icon: WebElement = wait.until \
            (method=EC.presence_of_element_located \
                (locator=(By.ID, "com.inreii.neutralapp:id/tempchi_button")))
        call_temp_ruler_icon.click()

    @staticmethod
    def get_temp_ruler_bar(wait) -> WebElement:
        """
        获取等温尺图标
        :param wait:
        :return:
        """
        temp_ruler_icon: WebElement = wait.until \
            (method=EC.presence_of_element_located \
                (locator=(By.ID, "com.inreii.neutralapp:id/sb_vertical")))
        return temp_ruler_icon

class ImageSetting:

    @staticmethod
    def click_call_img_set_icon(wait) -> None:
        """
        点击图像设置图标
        :param wait:
        :return:
        """
        img_set_icon: WebElement = wait.until \
            (method=EC.presence_of_element_located \
                (locator=(By.ID, "com.inreii.neutralapp:id/button_imgset")))
        img_set_icon.click()

    @staticmethod
    def get_brightness_icon(wait) -> WebElement:
        """
        获取亮度图标
        :param wait:
        :return:
        """
        brightness_icon: WebElement = wait.until \
            (method=EC.presence_of_element_located \
                (locator=(By.ID, "com.inreii.neutralapp:id/brightness")))
        return brightness_icon

    @staticmethod
    def click_brightness_icon(wait) -> None:
        """
        点击调出亮度栏
        :param wait:
        :return:
        """
        brightness_icon: WebElement = wait.until \
            (method=EC.presence_of_element_located \
                (locator=(By.ID, "com.inreii.neutralapp:id/brightness")))
        brightness_icon.click()

    @staticmethod
    def get_contrast_icon(wait) -> WebElement:
        """
        获取对比度图标
        :param wait:
        :return:
        """
        contrast_icon: WebElement = wait.until \
            (method=EC.presence_of_element_located \
                (locator=(By.ID, "com.inreii.neutralapp:id/whiteness")))
        return contrast_icon

    @staticmethod
    def click_contrast_icon(wait) -> None:
        """
        点击调出对比度栏
        :param wait:
        :return:
        """
        contrast_icon: WebElement = wait.until \
            (method=EC.presence_of_element_located \
                (locator=(By.ID, "com.inreii.neutralapp:id/whiteness")))
        contrast_icon.click()

    @staticmethod
    def get_brightness_contrast_bar(wait) -> WebElement:
        """
        获取亮度条/对比度条
        :param wait:
        :return:
        """
        brightness_contrast_bar: WebElement = wait.until \
            (method=EC.presence_of_element_located \
                (locator=(By.ID, "com.inreii.neutralapp:id/ll_bright")))
        return brightness_contrast_bar

    @staticmethod
    def get_xuanzhuan_icon(wait) -> WebElement:
        """
        获取旋转图标
        :param wait:
        :return:
        """
        xuanzhuan_icon: WebElement = wait.until \
            (method=EC.presence_of_element_located \
                (locator=(By.ID, "com.inreii.neutralapp:id/xuanzhuan_button")))
        return xuanzhuan_icon

    @staticmethod
    def get_jingxiang_icon(wait) -> WebElement:
        """
        获取镜像图标
        :param wait:
        :return:
        """
        jingxiang_icon: WebElement = wait.until \
            (method=EC.presence_of_element_located \
                (locator=(By.ID, "com.inreii.neutralapp:id/jingxiang_button")))
        return jingxiang_icon


def judge_alert(wait) -> None:
    """
    判断是否有弹框提示授权APP访问camera+，点击允许
    :param wait:
    :return:
    """
    try:
        alert: WebElement = wait.until \
            (method=EC.presence_of_element_located \
                (locator=(By.ID, "android:id/alertTitle")))
        admission: WebElement = wait.until \
            (method=EC.presence_of_element_located \
                (locator=(By.ID, "android:id/button1")))
        admission.click()
    except (NoSuchElementException, InvalidElementStateException, TimeoutException):
        pass

def find_view_element(wait) -> None:
    """
    找到取景器元素
    :param wait:
    :return:
    """
    # flag: int = 0
    # while flag < 4:
    #     try:
    #         view: WebElement = wait.until \
    #             (method=EC.presence_of_element_located \
    #                 (locator=(By.ID, "com.inreii.neutralapp:id/yulan")))
    #         break
    #     except (NoSuchElementException, TimeoutException, InvalidElementStateException):
    #         time.sleep(5)
    #         flag += 1
    #
    # if flag == 4:
    #     assert False, "找不到取景器元素"

    try:
        view: WebElement = wait.until \
            (method=EC.presence_of_element_located \
                (locator=(By.ID, "com.inreii.neutralapp:id/yulan")))
    except (NoSuchElementException, TimeoutException, InvalidElementStateException):
        assert False, "找不到取景器元素"

def take_video(wait, n: int, t: int) -> None:
    """
    录制n段视频，时间到达后停止
    :param n:
    :param t:
    :param wait:
    :return:
    """
    # 找到录制视频元素
    record: WebElement = wait.until \
        (method=EC.presence_of_element_located \
            (locator=(By.ID, "com.inreii.neutralapp:id/ib_camera")))

    # 开始录制
    for _ in range(n):
        record.click()
        time.sleep(t)
        record.click()

def take_photo(wait, n: int) -> None:
    """
    拍摄n张照片
    :param wait:
    :param n:
    :return:
    """
    # 找到拍摄照片元素
    take_photo: WebElement = wait.until \
        (method=EC.presence_of_element_located \
            (locator=(By.ID, "com.inreii.neutralapp:id/ib_color")))

    # 拍摄照片
    for _ in range(n):
        take_photo.click()
        time.sleep(1)

def enter_albums(wait) -> None:
    """
    进入相册
    :param wait:
    :return:
    """
    # 找到album元素
    album: WebElement = wait.until \
        (method=EC.presence_of_element_located \
            (locator=(By.ID, "com.inreii.neutralapp:id/imgK")))

    # 点击进入
    album.click()

def back_shell(wait) -> None:
    """
    返回外壳
    :param wait:
    :return:
    """
    back: WebElement = wait.until \
        (method=EC.presence_of_element_located \
            (locator=(By.ID, "com.inreii.neutralapp:id/sql_image_fh")))
    back.click()

def enter_setting(wait) -> None:
    """
    进入设置页面
    :param wait:
    :return:
    """
    setting: WebElement = wait.until \
        (method=EC.presence_of_element_located \
            (locator=(By.ID, "com.inreii.neutralapp:id/setting_button")))
    setting.click()

