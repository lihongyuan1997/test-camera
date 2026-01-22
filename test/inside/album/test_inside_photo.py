from selenium.webdriver.remote.webelement import WebElement
from selenium.common import NoSuchElementException, InvalidElementStateException, TimeoutException, StaleElementReferenceException
import time
import allure
import utility
from page.inside import view, albums
from page.inside.albums import photo
from page.outside import startup, device, gallery

class TestInsidePhoto:

    @allure.epic("inside")
    @allure.feature("photo")
    def test_inside_photo_generate_report_inside_check(self):
        """
        测试内部照片生成报告后，内部是否存在报告
        :return:
        """
        # 进入插件
        device.enter_camera(self.wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        view.admit_access(self.wait)

        # 等取景器加载完毕
        time.sleep(10)

        # 拍摄照片
        view.take_photo(self.wait, 1)

        # 进入内部相册
        view.enter_albums(self.wait)

        # 进入报告页面
        albums.enter_report(self.wait)

        # 生成报告前---获取所有报告标题
        all_report_titles_before: list[str] = albums.report.get_all_reports(self.wait, self.driver)
        print("生成报告前内部所有报告标题：", all_report_titles_before)

        # 进入相册页面
        albums.enter_album(self.wait)

        # 找到第一张照片
        first_photo: WebElement = albums.album.find_latest_file(self.wait, self.driver)

        # 进入第一张照片
        first_photo.click()

        # 生成报告
        photo.click_generate_report(self.wait)

        # 确认生成报告
        photo.confirm_generate_report(self.wait)

        # 返回相册页面
        utility.back_last_page(self.wait)

        # 进入报告页面
        albums.enter_report(self.wait)

        # 生成报告后---再次获取所有报告标题
        all_report_titles_after: list[str] = albums.report.get_all_reports(self.wait, self.driver)
        print("生成报告后内部所有报告标题：", all_report_titles_after)

        # 判断报告是否生成成功
        if all_report_titles_before is None:
            assert len(all_report_titles_after) == 1, "生成内部报告失败"
        else:
            assert len(all_report_titles_after) == len(all_report_titles_before) + 1, "生成内部报告失败"

    @allure.epic("inside")
    @allure.feature("photo")
    def test_inside_photo_generate_report_outside_check(self):
        """
        测试内部照片生成报告后，外部是否存在报告
        :return:
        """
        print("----------------------------------------------------------------生成报告前-------------------------------------------------------------")

        # 进入外壳报告页面
        startup.enter_gallery(self.wait)
        albums.enter_report(self.wait)

        # 获取所有报告标题
        all_report_titles_before: list[str] = gallery.report.get_all_reports(self.wait, self.driver)
        print("生成报告前外部所有报告标题：", all_report_titles_before)

        # 进入设备页面
        startup.enter_device(self.wait)

        # 进入插件
        device.enter_camera(self.wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        view.admit_access(self.wait)

        # 等取景器加载完毕
        time.sleep(10)

        # 拍摄照片
        view.take_photo(self.wait, 1)

        # 进入内部相册
        view.enter_albums(self.wait)

        # 进入相册页面
        albums.enter_album(self.wait)

        # 找到第一张照片
        first_photo: WebElement = albums.album.find_latest_file(self.wait, self.driver)

        # 进入第一张照片
        first_photo.click()

        # 生成报告
        photo.click_generate_report(self.wait)

        # 确认生成报告
        photo.confirm_generate_report(self.wait)

        print("----------------------------------------------------------------生成报告后-------------------------------------------------------------")

        # 返回相册页面
        utility.back_last_page(self.wait)

        # 返回取景器页面
        utility.back_last_page(self.wait)

        # 返回外壳界面
        view.back_shell(self.wait)

        # 进入外壳报告页面
        startup.enter_gallery(self.wait)
        gallery.enter_report(self.wait)

        # 获取所有报告标题
        all_report_titles_after: list[str] = gallery.report.get_all_reports(self.wait, self.driver)
        print("生成报告后外部所有报告标题：", all_report_titles_after)

        # 判断报告是否生成成功
        if all_report_titles_before is None:
            assert len(all_report_titles_after) == 1, "生成外部报告失败"
        else:
            assert len(all_report_titles_after) == len(all_report_titles_before) + 1, "生成外部报告失败"

    @allure.epic("inside")
    @allure.feature("photo")
    def test_enter_analysis(self):
        """
        测试是否能进入离线分析
        :return:
        """
        # 进入设备页面
        startup.enter_device(self.wait)

        # 进入插件
        device.enter_camera(self.wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        view.admit_access(self.wait)

        # 等取景器加载完毕
        time.sleep(10)

        # 拍摄照片
        view.take_photo(self.wait, 1)

        # 进入内部相册
        view.enter_albums(self.wait)

        # 进入相册页面
        albums.enter_album(self.wait)

        # 找到第一张照片
        first_photo: WebElement = albums.album.find_latest_file(self.wait, self.driver)

        # 进入第一张照片
        first_photo.click()

        # 进入离线分析
        photo.enter_analysis(self.wait)

        # 判断是否显示色板栏、发射率、点、线、框、文本框、清除图标
        try:
            photo.get_pallete_icon(self.wait)
        except (NoSuchElementException, InvalidElementStateException, TimeoutException, StaleElementReferenceException):
            assert False, "找不到色板栏图标，进入离线分析失败"

        try:
            photo.get_emissivity_icon(self.wait)
        except (NoSuchElementException, InvalidElementStateException, TimeoutException, StaleElementReferenceException):
            assert False, "找不到发射率图标，进入离线分析失败"

        try:
            photo.get_point_icon(self.wait)
        except (NoSuchElementException, InvalidElementStateException, TimeoutException, StaleElementReferenceException):
            assert False, "找不到点标注图标，进入离线分析失败"

        try:
            photo.get_line_icon(self.wait)
        except (NoSuchElementException, InvalidElementStateException, TimeoutException, StaleElementReferenceException):
            assert False, "找不到线标注图标，进入离线分析失败"

        try:
            photo.get_rectangle_icon(self.wait)
        except (NoSuchElementException, InvalidElementStateException, TimeoutException, StaleElementReferenceException):
            assert False, "找不到框标注图标，进入离线分析失败"

        try:
            photo.get_textbox_icon(self.wait)
        except (NoSuchElementException, InvalidElementStateException, TimeoutException, StaleElementReferenceException):
            assert False, "找不到文本框图标，进入离线分析失败"

        try:
            photo.get_clear_icon(self.wait)
        except (NoSuchElementException, InvalidElementStateException, TimeoutException, StaleElementReferenceException):
            assert False, "找不到清除图标，进入离线分析失败"

    @allure.epic("inside")
    @allure.feature("photo")
    def test_call_thermal_ruler(self):
        """
        测试能否调用等温尺
        :return:
        """
        # 进入设备页面
        startup.enter_device(self.wait)

        # 进入插件
        device.enter_camera(self.wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        view.admit_access(self.wait)

        # 等取景器加载完毕
        time.sleep(10)

        # 拍摄照片
        view.take_photo(self.wait, 1)

        # 进入内部相册
        view.enter_albums(self.wait)

        # 进入相册页面
        albums.enter_album(self.wait)

        # 找到第一张照片
        first_photo: WebElement = albums.album.find_latest_file(self.wait, self.driver)

        # 进入第一张照片
        first_photo.click()

        # 调用等温尺
        photo.call_thermal_ruler(self.wait)

        # 判断是否显示等温尺
        try:
            photo.get_thermal_ruler(self.wait)
        except (NoSuchElementException, InvalidElementStateException, TimeoutException, StaleElementReferenceException):
            assert False, "找不到等温尺，调用等温尺失败"