import time
import pytest, allure
from appium.webdriver import WebElement
from selenium.common import NoSuchElementException, InvalidElementStateException, TimeoutException, \
    StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import common_utils
import page.inside.albums
from page.outside import  startup, device, gallery
from page.inside import view, albums
from page.inside.view import MeasureTempTool, ImageSetting, TempRuler, Pallete


class TestView:

    @allure.epic("inside")
    @allure.feature("view")
    def test_call_measure_temp_row(self):
        """
        测试调出测温工具栏
        :return:
        """
        # 进入插件
        device.enter_camera(self.wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        view.judge_alert(self.wait)

        # 等取景器加载完毕
        time.sleep(10)

        # 点击调用测温工具栏图标
        MeasureTempTool.click_call_measure_temp_tool_icon(self.wait)

        # 判断各测温工具是否展示
        try:
            MeasureTempTool.get_center_temp_icon(self.wait)
            MeasureTempTool.get_max_temp_icon(self.wait)
            MeasureTempTool.get_min_temp_icon(self.wait)
            MeasureTempTool.get_point_temp_icon(self.wait)
            MeasureTempTool.get_line_temp_icon(self.wait)
            MeasureTempTool.get_rectangle_temp_icon(self.wait)
            MeasureTempTool.get_del_temp_icon(self.wait)
        except(NoSuchElementException, StaleElementReferenceException, InvalidElementStateException, TimeoutException):
            assert False, "调用测温工具栏失败"

    @allure.epic("inside")
    @allure.feature("view")
    def test_call_temp_ruler_bar(self):
        """
        测试调用等温尺是否成功
        :return:
        """
        # 进入插件
        device.enter_camera(self.wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        view.judge_alert(self.wait)

        # 等取景器加载完毕
        time.sleep(10)

        # 点击调用等温尺
        TempRuler.click_call_temp_ruler_icon(self.wait)

        # 判断等温尺是否调用成功
        try:
            TempRuler.get_temp_ruler_bar(self.wait)
        except(NoSuchElementException, StaleElementReferenceException, InvalidElementStateException, TimeoutException):
            assert False, "等温尺调用失败"

    @allure.epic("inside")
    @allure.feature("view")
    @allure.story("image_setting")
    def test_call_img_setting_row(self):
        """
        测试调出图像工具栏
        :return:
        """
        # 进入插件
        device.enter_camera(self.wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        view.judge_alert(self.wait)

        # 等取景器加载完毕
        time.sleep(10)

        # 点击调用图像工具栏图标
        ImageSetting.click_call_img_set_icon(self.wait)

        # 判断各图像工具是否展示
        try:
            ImageSetting.get_brightness_icon(self.wait)
            ImageSetting.get_contrast_icon(self.wait)
            ImageSetting.get_xuanzhuan_icon(self.wait)
            ImageSetting.get_jingxiang_icon(self.wait)
        except(NoSuchElementException, InvalidElementStateException, StaleElementReferenceException, TimeoutException):
            assert False, "调用图像工具栏失败"

    @allure.epic("inside")
    @allure.feature("view")
    @allure.story("image_setting")
    def test_call_brightness_bar(self):
        """
        测试调出亮度栏
        :return:
        """
        # 进入插件
        device.enter_camera(self.wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        view.judge_alert(self.wait)

        # 等取景器加载完毕
        time.sleep(10)

        # 点击调用图像工具栏图标
        ImageSetting.click_call_img_set_icon(self.wait)

        # 点击调用亮度栏
        ImageSetting.click_brightness_icon(self.wait)

        # 判断亮度栏是否调出
        try:
            ImageSetting.get_brightness_contrast_bar(self.wait)
        except(NoSuchElementException, StaleElementReferenceException, InvalidElementStateException, TimeoutException):
            assert False, "亮度栏调出失败"

    @allure.epic("inside")
    @allure.feature("view")
    @allure.story("image_setting")
    def test_call_contrast_bar(self):
        """
        测试调出对比度栏
        :return:
        """
        # 进入插件
        device.enter_camera(self.wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        view.judge_alert(self.wait)

        # 等取景器加载完毕
        time.sleep(10)

        # 点击调用图像工具栏图标
        ImageSetting.click_call_img_set_icon(self.wait)

        # 点击调用对比度栏
        ImageSetting.click_contrast_icon(self.wait)

        # 判断对比度栏是否调出
        try:
            ImageSetting.get_brightness_contrast_bar(self.wait)
        except(NoSuchElementException, StaleElementReferenceException, InvalidElementStateException, TimeoutException):
            assert False, "对比度栏调出失败"

    @allure.epic("inside")
    @allure.feature("view")
    def test_call_palette_row(self):
        """
        测试调出色板栏
        :return:
        """
        # 进入插件
        device.enter_camera(self.wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        view.judge_alert(self.wait)

        # 等取景器加载完毕
        time.sleep(10)

        # 展示色板栏
        Pallete.display_palette_row(self.wait)

        # 判断色板栏是否展示成功
        try:
            Pallete.get_hongtou_palette(self.wait)
        except:
            assert False, "调用色板栏失败"

    @allure.epic("inside")
    @allure.feature("view")
    @pytest.mark.parametrize(argnames='n', argvalues=[5])
    def test_generate_inside_photo(self, n: int):
        """
        测试拍摄n张照片是否成功
        :return:
        """
        # 进入插件
        device.enter_camera(self.wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        view.judge_alert(self.wait)

        # 等取景器加载完毕
        time.sleep(10)

        # 进入内部相册
        view.enter_albums(self.wait)
        albums.enter_album(self.wait)

        print("--------------------------------------【拍摄前】---------------------------------------")

        # 找到相册里拍摄前第一个文件，如果存在，获取标题；如果不存在，设置标题为空
        latest_file: WebElement | None = albums.album.find_latest_file(self.wait, self.driver)
        if latest_file:
            # 进入第一个文件详情
            latest_file.click()
            latest_file_title: str = albums.photo.find_file_title(self.wait)
            # 返回相册界面
            common_utils.back_last_page(self.wait)
        else:
            latest_file_title: str = ''

        # 返回取景页面
        common_utils.back_last_page(self.wait)

        # 拍摄n张照片
        view.take_photo(self.wait, n)

        print("---------------------------------------【拍摄后】--------------------------------------")

        # 进入内部相册界面
        view.enter_albums(self.wait)
        albums.enter_album(self.wait)

        # 如果拍摄前至少存在一个文件，则找到拍摄后相册里前n+1文件; 否则找到前n个文件
        if latest_file_title:
            after_files_titles: list[str] = albums.album.find_files_titles(self.wait, self.driver, n + 1)
            print("拍摄后的相册里的所有文件标题：", after_files_titles)
            expr: bool = after_files_titles[-1] == latest_file_title and len(set(after_files_titles)) == len(after_files_titles) == n + 1
            assert expr, '照片拍摄存在失败，或者内部相册存储照片存在失败'
        else:
            after_files_titles: list[str] = albums.album.find_files_titles(self.wait, self.driver, n)
            print("拍摄后的相册里的所有文件标题：", after_files_titles)
            expr: bool = len(set(after_files_titles)) == len(after_files_titles) == n
            assert expr, '照片拍摄存在失败，或者内部相册存储照片存在失败'

    @allure.epic("inside")
    @allure.feature("view")
    @pytest.mark.parametrize(argnames='n, t', argvalues=[(5, 5)])
    def test_generate_inside_video(self, n: int, t: int):
        """
        测试录制视频是否成功
        :return:
        """
        # 进入插件
        device.enter_camera(self.wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        view.judge_alert(self.wait)

        #等取景器加载完毕
        time.sleep(10)

        # 进入内部相册
        view.enter_albums(self.wait)
        albums.enter_album(self.wait)

        print("-------------------------------------------------【拍摄前】-------------------------------------------------")

        # 找到相册里拍摄前第一个文件，如果存在，获取标题；如果不存在，设置标题为空
        latest_file: WebElement | None = albums.album.find_latest_file(self.wait, self.driver)
        if latest_file:
            # 进入文件详情
            latest_file.click()
            latest_file_title: str = albums.album.find_file_title(self.wait)
            # 返回相册界面
            common_utils.back_last_page(self.wait)
        else:
            latest_file_title: str = ''

        # 返回取景页面
        common_utils.back_last_page(self.wait)

        # 拍摄n段视频，每段视频t秒
        view.take_video(self.wait, n, t)

        print("-------------------------------------------------------【拍摄后】--------------------------------------------------------")

        # 等待3s进入相册界面
        time.sleep(3)

        # 进入内部相册界面
        view.enter_albums(self.wait)
        albums.enter_album(self.wait)

        # 如果拍摄前至少存在一个文件，则找到拍摄后相册里前n+1文件; 否则找到前n个文件
        if latest_file_title:
            after_files_titles: list[str] = albums.album.find_files_titles(self.wait, self.driver, n + 1)
            print("拍摄后的相册里的所有文件标题：", after_files_titles)
            expr: bool = after_files_titles[-1] == latest_file_title and len(set(after_files_titles)) == len(after_files_titles) == n + 1
            assert expr, '视频拍摄存在失败，或者内部相册存储视频存在失败'
        else:
            after_files_titles: list[str] = albums.album.find_files_titles(self.wait, self.driver, n)
            print("拍摄后的相册里的所有文件标题：", after_files_titles)
            expr: bool = len(set(after_files_titles)) == len(after_files_titles) == n
            assert expr, '视频拍摄存在失败，或者内部相册存储视频存在失败'

    @allure.epic("inside")
    @allure.feature("view")
    @pytest.mark.parametrize(argnames='n', argvalues=[5])
    def test_generate_outside_photo(self, n: int):
        """
        测试内部取景器拍照后，外部相册有对应照片生成
        :return:
        """
        print("--------------------------------------【拍摄前】---------------------------------------")

        # 进入外壳相册
        startup.enter_gallery(self.wait)
        gallery.enter_album(self.wait)

        # 找到相册里拍摄前第一个文件，如果存在，获取标题；如果不存在，设置标题为空
        latest_file: WebElement | None = gallery.album.find_latest_file(self.wait, self.driver)
        if latest_file:
            # 进入第一个文件详情
            latest_file.click()
            latest_file_title: str = gallery.photo.find_file_title(self.wait)
            # 返回相册界面
            common_utils.back_last_page(self.wait)
        else:
            latest_file_title: str = ''

        # 进入设备页面
        startup.enter_device(self.wait)

        # 进入插件
        device.enter_camera(self.wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        view.judge_alert(self.wait)

        # 等取景器加载完毕
        time.sleep(10)

        # 拍摄n张照片
        view.take_photo(self.wait, n)

        print("---------------------------------------【拍摄后】--------------------------------------")

        # 返回外壳界面
        view.back_shell(self.wait)

        # 进入外壳相册界面
        startup.enter_gallery(self.wait)
        gallery.enter_album(self.wait)

        # 如果拍摄前至少存在一个文件，则找到拍摄后相册里前n+1文件; 否则找到前n个文件
        if latest_file_title:
            after_files_titles: list[str] = gallery.album.find_files_titles(self.wait, self.driver, n + 1)
            print("拍摄后的相册里的所有文件标题：", after_files_titles)
            expr: bool = after_files_titles[-1] == latest_file_title and len(set(after_files_titles)) == len(
                after_files_titles) == n + 1
            assert expr, '照片拍摄存在失败，或者外壳相册存储照片存在失败'
        else:
            after_files_titles: list[str] = gallery.album.find_files_titles(self.wait, self.driver, n)
            print("拍摄后的相册里的所有文件标题：", after_files_titles)
            expr: bool = len(set(after_files_titles)) == len(after_files_titles) == n
            assert expr, '照片拍摄存在失败，或者外壳相册存储照片存在失败'

    @allure.epic("inside")
    @allure.feature("view")
    @pytest.mark.parametrize(argnames='n, t', argvalues=[(5, 5)])
    def test_generate_outside_video(self, n: int, t: int):
        """
        测试内部取景器录像后，外部相册有对应视频生成
        :return:
        """
        print("--------------------------------------【拍摄前】---------------------------------------")

        # 进入外壳相册
        startup.enter_gallery(self.wait)

        # 找到相册里拍摄前第一个文件，如果存在，获取标题；如果不存在，设置标题为空
        latest_file: WebElement | None = gallery.album.find_latest_file(self.wait, self.driver)
        if latest_file:
            # 进入第一个文件详情
            latest_file.click()
            latest_file_title: str = gallery.photo.find_file_title(self.wait)
            # 返回相册界面
            common_utils.back_last_page(self.wait)
        else:
            latest_file_title: str = ''

        # 进入设备页面
        startup.enter_device(self.wait)

        # 进入插件
        device.enter_camera(self.wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        view.judge_alert(self.wait)

        # 等取景器加载完毕
        time.sleep(10)

        # 拍摄n段视频
        view.take_video(self.wait, n, t)

        print("---------------------------------------【拍摄后】--------------------------------------")

        # 返回外壳界面
        view.back_shell(self.wait)

        # 进入外壳相册界面
        startup.enter_gallery(self.wait)

        # 如果拍摄前至少存在一个文件，则找到拍摄后相册里前n+1文件; 否则找到前n个文件
        if latest_file_title:
            after_files_titles: list[str] = gallery.album.find_files_titles(self.wait, self.driver, n + 1)
            print("拍摄后的相册里的所有文件标题：", after_files_titles)
            expr: bool = after_files_titles[-1] == latest_file_title and len(set(after_files_titles)) == len(
                after_files_titles) == n + 1
            assert expr, '视频拍摄存在失败，或者外壳相册存储视频存在失败'
        else:
            after_files_titles: list[str] = gallery.album.find_files_titles(self.wait, self.driver, n)
            print("拍摄后的相册里的所有文件标题：", after_files_titles)
            expr: bool = len(set(after_files_titles)) == len(after_files_titles) == n
            assert expr, '视频拍摄存在失败，或者外壳相册存储视频存在失败'

    @allure.epic("inside")
    @allure.feature("view")
    def test_enter_inside_setting(self):
        """
        测试从取景器跳转到内部设置页面
        :return:
        """
        # 进入插件
        device.enter_camera(self.wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        view.judge_alert(self.wait)

        # 等取景器加载完毕
        time.sleep(10)

        # 进入设置页面
        view.enter_setting(self.wait)

        # 判断是否进入设置成功
        try:
            setting: WebElement = self.wait.until \
                (method=EC.presence_of_element_located \
                    (locator=(By.ID, "com.inreii.neutralapp:id/title_content")))
            assert setting.text == "Settings", "设置页面名称错误，进入设置页面失败"
        except (NoSuchElementException, InvalidElementStateException, TimeoutException):
            assert False, "未找到设置页面名称元素，进入设置页面失败"

    def test_enter_inside_albums(self):
        """
        测试从取景器跳转到相册
        :return:
        """
        # 进入插件
        device.enter_camera(self.wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        view.judge_alert(self.wait)

        # 等取景器加载完毕
        time.sleep(10)

        # 进入相册
        view.enter_albums(self.wait)

        # 判断是否进入相册成功
        try:
            album: WebElement = self.wait.until \
                (method=EC.presence_of_element_located \
                    (locator=(By.ID, "com.inreii.neutralapp:id/title_content")))
            assert album.text == "Albums", "相册页面名称错误，进入相册页面失败"
        except (NoSuchElementException, InvalidElementStateException, TimeoutException):
            assert False, "未找到相册页面名称元素，进入相册页面失败"