import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, InvalidElementStateException, StaleElementReferenceException
import utility
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions.interaction import *

class View:

    @staticmethod
    def admit_access(wait) -> None:
        """
        如果有弹框提示授权APP访问camera+，点击允许
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

    @staticmethod
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

    @staticmethod
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

    @staticmethod
    def call_picture_in_picture(driver, wait) -> None:
        """
        点击调用画中画
        :param driver:
        :param wait:
        :return:
        """
        # 定位顶部栏，获取坐标尺寸
        top_row = wait.until \
            (method=EC.presence_of_element_located \
                (locator=(By.ID, "com.inreii.neutralapp:id/ll_topbuttons")))

        # 画中画图标大概位置
        pip_axis_x = (top_row.location['x'] + top_row.size['width']) * 0.5
        pip_axis_y = (top_row.location['y'] + top_row.size['height']) * 0.3

        # 点击画中画图标，调用画中画
        driver.tap([(pip_axis_x, pip_axis_y)], 100)

    @staticmethod
    def get_picture_in_picture(wait) -> WebElement:
        """
        获取画中画元素
        :param wait:
        :return:
        """
        try:
            pip = wait.until(EC.presence_of_element_located((By.ID, "com.inreii.neutralapp:id/tvdrag")))
            return pip
        except(NoSuchElementException, TimeoutException, InvalidElementStateException, StaleElementReferenceException):
            assert False, "调用画中画失败"

    @staticmethod
    def get_view_element(wait) -> WebElement:
        """
        找到并返回取景器元素
        :param wait:
        :return:
        """
        try:
            view: WebElement = wait.until \
                (method=EC.presence_of_element_located \
                    (locator=(By.ID, "com.inreii.neutralapp:id/yulan")))
            return view
        except (NoSuchElementException, TimeoutException, InvalidElementStateException):
            assert False, "找不到取景器元素"

    @staticmethod
    def call_measure_temp_tool(wait) -> None:
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
    def call_temp_ruler(wait) -> None:
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
    def get_temp_ruler(wait) -> WebElement:
        """
        获取等温尺图标
        :param wait:
        :return:
        """
        temp_ruler_icon: WebElement = wait.until \
            (method=EC.presence_of_element_located \
                (locator=(By.ID, "com.inreii.neutralapp:id/sb_vertical")))
        return temp_ruler_icon

    @staticmethod
    def call_img_setting(wait) -> None:
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
    def call_palette_row(wait) -> None:
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

    @staticmethod
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

    @staticmethod
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

class MeasureTempTool:

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
    def click_center_temp_icon(wait) -> None:
        """
        点击中心点测温图标
        :param wait:
        :return:
        """
        center_temp_icon: WebElement = MeasureTempTool.get_center_temp_icon(wait)
        center_temp_icon.click()

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
    def click_max_temp_icon(wait) -> None:
        """
        点击最高温图标
        :param wait:
        :return:
        """
        max_temp_icon: WebElement = MeasureTempTool.get_max_temp_icon(wait)
        max_temp_icon.click()

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
    def click_min_temp_icon(wait) -> None:
        """
        点击最低温图标
        :param wait:
        :return:
        """
        min_temp_icon: WebElement = MeasureTempTool.get_min_temp_icon(wait)
        min_temp_icon.click()

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
    def click_point_temp_icon(wait) -> None:
        """
        点击点测温图标
        :param wait:
        :return:
        """
        point_temp_icon: WebElement = MeasureTempTool.get_point_temp_icon(wait)
        point_temp_icon.click()

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
    def click_line_temp_icon(wait) -> None:
        """
        点击线测温图标
        :param wait:
        :return:
        """
        line_temp_icon: WebElement = MeasureTempTool.get_line_temp_icon(wait)
        line_temp_icon.click()

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
    def click_rectangle_temp_icon(wait) -> None:
        """
        点击框测温图标
        :param wait:
        :return:
        """
        rectangle_temp_icon: WebElement = MeasureTempTool.get_rectangle_temp_icon(wait)
        rectangle_temp_icon.click()

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

    @staticmethod
    def click_del_temp_icon(wait) -> None:
        """
        点击清除点线框图标
        :param wait:
        :return:
        """
        del_temp_icon: WebElement = MeasureTempTool.get_del_temp_icon(wait)
        del_temp_icon.click()

class ImageSetting:

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

class Pallete:

    PALLETE: dict[str:str] = {"bingleng": "com.inreii.neutralapp:id/rl_bingleng1", # 冰冷
                                 "hongtou":"com.inreii.neutralapp:id/ib_hongtou" , # 红头
                                 "tiehui":"com.inreii.neutralapp:id/ib_tiehui", # 铁灰
                                 "mohui":"com.inreii.neutralapp:id/rl_mohui1", # 墨灰
                                 "rongyan":"com.inreii.neutralapp:id/ib_rongyan", # 熔岩
                                 "gaocaihong":"com.inreii.neutralapp:id/ib_gaocaihong", # 高彩虹
                                 "caihong":"com.inreii.neutralapp:id/ib_caihong", # 彩虹
                                 "heire":"com.inreii.neutralapp:id/ib_heire", # 黑热
                                 "baire":"com.inreii.neutralapp:id/baire_mode_button", # 白热
                                 "tiehong":"com.inreii.neutralapp:id/ib_tiehong" # 铁红
                              }

    @staticmethod
    def swipe_pallete_row_up(driver, view_ele: WebElement):
        """
        向上滑动色板栏
        :param driver:
        :param view:
        :return:
        """
        # 确定色板栏横坐标（屏幕是横过来的）
        axis_x = view_ele.location['x'] + view_ele.size['width'] - 100

        # 向上滑动
        driver.swipe(axis_x, view_ele.size['height'] * 0.75, axis_x, view_ele.size['height'] * 0.25)

    @staticmethod
    def swipe_pallete_row_down(driver, view_ele: WebElement):
        """
        向下滑动色板栏
        :param driver:
        :param view:
        :return:
        """
        # 确定色板栏横坐标（屏幕是横过来的）
        axis_x = view_ele.location['x'] + view_ele.size['width'] - 100

        # 向下滑动
        driver.swipe(axis_x, view_ele.size['height'] * 0.25, axis_x, view_ele.size['height'] * 0.75)

    @staticmethod
    def choose_palette(wait, driver, view: WebElement, palette: str) -> None:
        """
        选择色板
        :param driver:
        :param palette_name:
        :param wait:
        :return:
        """
        left_count = 0
        while True:
            try:
                # 找到具体色板元素
                palette_ele: WebElement = wait.until \
                    (method=EC.presence_of_element_located \
                        (locator=(By.ID, Pallete.PALLETE[palette])))
                # 选择色板
                palette_ele.click()
                print(f"--------已选择{palette}色板--------")
                break
            # 没找到向下滑
            except (NoSuchElementException, TimeoutException, InvalidElementStateException):
                Pallete.swipe_pallete_row_down(driver,view)
                left_count += 1
                if left_count == 3:
                    assert False, f"--------找不到{palette}色板--------"
