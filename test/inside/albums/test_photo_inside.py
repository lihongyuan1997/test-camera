import pytest
from selenium.webdriver.remote.webelement import WebElement
from selenium.common import *
import time
import allure
import utility
from page.inside import albums
from page.inside.view import View, Pallete
from page.inside.albums import photo
from page.inside.albums.photo import Analysis, AnalysisPallete
from page.outside import startup, device, gallery

@allure.epic("inside")
@allure.feature("photo")
@pytest.mark.inside
@pytest.mark.photo
class TestPhotoInside:

    def test_enter_analysis(self, driver, wait):
        """
        测试是否能进入离线分析
        :return:
        """
        # 进入设备页面
        startup.enter_device(wait)

        # 进入插件
        device.enter_camera(wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        View.admit_access(wait)

        # 等取景器加载完毕
        time.sleep(10)

        # 拍摄照片
        View.take_photo(wait, 1)

        # 进入内部相册
        View.enter_albums(wait)

        # 进入相册页面
        albums.enter_album(wait)

        # 找到第一张照片
        first_photo: WebElement = albums.album.get_latest_file(wait, driver)

        # 进入第一张照片
        first_photo.click()

        # 进入离线分析
        photo.enter_analysis(wait)

        # 判断是否显示色板栏、发射率、点、线、框、文本框、清除图标
        try:
            Analysis.get_pallete_icon(wait)
        except (NoSuchElementException, InvalidElementStateException, TimeoutException, StaleElementReferenceException):
            assert False, "找不到色板栏图标，进入离线分析失败"

        try:
            Analysis.get_emissivity_icon(wait)
        except (NoSuchElementException, InvalidElementStateException, TimeoutException, StaleElementReferenceException):
            assert False, "找不到发射率图标，进入离线分析失败"

        try:
            Analysis.get_point_icon(wait)
        except (NoSuchElementException, InvalidElementStateException, TimeoutException, StaleElementReferenceException):
            assert False, "找不到点标注图标，进入离线分析失败"

        try:
            Analysis.get_line_icon(wait)
        except (NoSuchElementException, InvalidElementStateException, TimeoutException, StaleElementReferenceException):
            assert False, "找不到线标注图标，进入离线分析失败"

        try:
            Analysis.get_rectangle_icon(wait)
        except (NoSuchElementException, InvalidElementStateException, TimeoutException, StaleElementReferenceException):
            assert False, "找不到框标注图标，进入离线分析失败"

        try:
            Analysis.get_textbox_icon(wait)
        except (NoSuchElementException, InvalidElementStateException, TimeoutException, StaleElementReferenceException):
            assert False, "找不到文本框图标，进入离线分析失败"

        try:
            Analysis.get_clear_icon(wait)
        except (NoSuchElementException, InvalidElementStateException, TimeoutException, StaleElementReferenceException):
            assert False, "找不到清除图标，进入离线分析失败"

    def test_photo_inside_generate_report_inside_check(self, driver, wait):
        """
        测试内部照片生成报告后，内部是否存在报告
        :return:
        """
        # 进入插件
        device.enter_camera(wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        View.admit_access(wait)

        # 等取景器加载完毕
        View.get_view_element(wait)

        # 拍摄照片
        View.take_photo(wait, 1)

        # 进入内部相册
        View.enter_albums(wait)

        # 进入报告页面
        albums.enter_report(wait)

        # 生成报告前---获取所有报告标题
        print("------------------------------生成报告前，查找所有报告------------------------------")
        all_report_titles_before: list[str] = albums.report.get_all_reports(wait, driver)
        print("生成报告前，内部所有报告标题：", all_report_titles_before)

        # 进入相册页面
        albums.enter_album(wait)

        # 找到第一张照片
        first_photo: WebElement = albums.album.get_latest_file(wait, driver)

        # 进入第一张照片
        first_photo.click()

        # 生成报告
        photo.click_generate_report(wait)

        # 确认生成报告
        photo.confirm_generate_report(wait)

        # 返回相册页面
        utility.back_last_page(wait)

        # 进入报告页面
        albums.enter_report(wait)

        # 生成报告后---再次获取所有报告标题
        print("------------------------------生成报告后，查找所有报告------------------------------")
        all_report_titles_after: list[str] = albums.report.get_all_reports(wait, driver)
        print("生成报告后，内部所有报告标题：", all_report_titles_after)

        # 判断报告是否生成成功
        if all_report_titles_before is None:
            assert len(all_report_titles_after) == 1, "生成内部报告失败"
        else:
            assert len(all_report_titles_after) == len(all_report_titles_before) + 1, "生成内部报告失败"

    def test_photo_inside_generate_report_outside_check(self, driver, wait):
        """
        测试内部照片生成报告后，外部是否存在报告
        :return:
        """
        # 进入外壳报告页面
        startup.enter_gallery(wait)
        albums.enter_report(wait)

        # 获取所有报告标题
        all_report_titles_before: list[str] = gallery.report.get_all_reports(wait, driver)
        print("生成报告前，外部所有报告标题：", all_report_titles_before)

        # 进入设备页面
        startup.enter_device(wait)

        # 进入插件
        device.enter_camera(wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        View.admit_access(wait)

        # 等取景器加载完毕
        View.get_view_element(wait)

        # 拍摄照片
        View.take_photo(wait, 1)

        # 进入内部相册
        View.enter_albums(wait)

        # 进入相册页面
        albums.enter_album(wait)

        # 找到第一张照片
        first_photo: WebElement = albums.album.get_latest_file(wait, driver)

        # 进入第一张照片
        first_photo.click()

        # 生成报告
        photo.click_generate_report(wait)

        # 确认生成报告
        photo.confirm_generate_report(wait)

        # 返回相册页面
        utility.back_last_page(wait)

        # 返回取景器页面
        utility.back_last_page(wait)

        # 返回外壳界面
        View.back_shell(wait)

        # 进入外壳报告页面
        startup.enter_gallery(wait)
        gallery.enter_report(wait)

        # 获取所有报告标题
        all_report_titles_after: list[str] = gallery.report.get_all_reports(wait, driver)
        print("生成报告后，外部所有报告标题：", all_report_titles_after)

        # 判断报告是否生成成功
        if all_report_titles_before is None:
            assert len(all_report_titles_after) == 1, "生成外部报告失败"
        else:
            assert len(all_report_titles_after) == len(all_report_titles_before) + 1, "生成外部报告失败"
    
    @pytest.mark.bingleng
    @pytest.mark.temp_ruler
    def test_no_analysis_bingleng_call_thermal_ruler(self, driver, wait):
        """
        测试原色板为冰冷色板，不进入离线分析，能否调用等温尺，预期失败
        :return:
        """
        # 进入设备页面
        startup.enter_device(wait)

        # 进入插件
        device.enter_camera(wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        View.admit_access(wait)

        # 等取景器加载完毕
        time.sleep(10)
        view_ele = View.get_view_element(wait)

        # 展示色板栏
        View.call_palette_row(wait)

        # 色板栏移动到开头位置
        Pallete.swipe_pallete_row_up(driver, view_ele)

        # 选择冰冷色板
        pallete = 'bingleng'
        Pallete.choose_palette(wait, driver, view_ele, pallete)

        # 拍摄照片
        View.take_photo(wait, 1)

        # 进入内部相册
        View.enter_albums(wait)

        # 进入相册页面
        albums.enter_album(wait)

        # 找到第一张照片
        first_photo: WebElement = albums.album.get_latest_file(wait, driver)

        # 进入第一张照片
        first_photo.click()

        # 调用等温尺
        photo.call_thermal_ruler(wait)

        # 判断是否显示等温尺
        try:
            photo.get_thermal_ruler(wait)
            assert False, f"{pallete}色板可以调用等温尺，用例失败"
        except (NoSuchElementException, InvalidElementStateException, TimeoutException, StaleElementReferenceException):
            pass

    @pytest.mark.hongtou
    @pytest.mark.temp_ruler
    def test_no_analysis_hongtou_call_thermal_ruler(self, driver, wait):
        """
        测试原色板为红头色板，不进入离线分析，能否调用等温尺，预期失败
        :return:
        """
        # 进入设备页面
        startup.enter_device(wait)

        # 进入插件
        device.enter_camera(wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        View.admit_access(wait)

        # 等取景器加载完毕
        time.sleep(10)
        view_ele = View.get_view_element(wait)

        # 展示色板栏
        View.call_palette_row(wait)

        # 色板栏移动到开头位置
        Pallete.swipe_pallete_row_up(driver, view_ele)

        # 选择红头色板
        pallete = 'hongtou'
        Pallete.choose_palette(wait, driver, view_ele, pallete)

        # 拍摄照片
        View.take_photo(wait, 1)

        # 进入内部相册
        View.enter_albums(wait)

        # 进入相册页面
        albums.enter_album(wait)

        # 找到第一张照片
        first_photo: WebElement = albums.album.get_latest_file(wait, driver)

        # 进入第一张照片
        first_photo.click()

        # 调用等温尺
        photo.call_thermal_ruler(wait)

        # 判断是否显示等温尺
        try:
            photo.get_thermal_ruler(wait)
            assert False, f"{pallete}色板可以调用等温尺，用例失败"
        except (NoSuchElementException, InvalidElementStateException, TimeoutException, StaleElementReferenceException):
            pass
    
    @pytest.mark.tiehui
    @pytest.mark.temp_ruler
    def test_no_analysis_tiehui_call_thermal_ruler(self, driver, wait):
        """
        测试原色板为铁灰色板，不进入离线分析，能否调用等温尺，预期成功
        :return:
        """
        # 进入设备页面
        startup.enter_device(wait)

        # 进入插件
        device.enter_camera(wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        View.admit_access(wait)

        # 等取景器加载完毕
        time.sleep(10)
        view_ele = View.get_view_element(wait)

        # 展示色板栏
        View.call_palette_row(wait)

        # 色板栏移动到开头位置
        Pallete.swipe_pallete_row_up(driver, view_ele)

        # 选择铁灰色板
        pallete = 'tiehui'
        Pallete.choose_palette(wait, driver, view_ele, pallete)

        # 拍摄照片
        View.take_photo(wait, 1)

        # 进入内部相册
        View.enter_albums(wait)

        # 进入相册页面
        albums.enter_album(wait)

        # 找到第一张照片
        first_photo: WebElement = albums.album.get_latest_file(wait, driver)

        # 进入第一张照片
        first_photo.click()

        # 调用等温尺
        photo.call_thermal_ruler(wait)

        # 判断是否显示等温尺
        try:
            photo.get_thermal_ruler(wait)
        except (NoSuchElementException, InvalidElementStateException, TimeoutException, StaleElementReferenceException):
            assert False, f"{pallete}色板无法调用等温尺，用例失败"
    
    @pytest.mark.mohui
    @pytest.mark.temp_ruler
    def test_no_analysis_mohui_call_thermal_ruler(self, driver, wait):
        """
        测试原色板为墨灰色板，不进入离线分析，能否调用等温尺，预期成功
        :return:
        """
        # 进入设备页面
        startup.enter_device(wait)

        # 进入插件
        device.enter_camera(wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        View.admit_access(wait)

        # 等取景器加载完毕
        time.sleep(10)
        view_ele = View.get_view_element(wait)

        # 展示色板栏
        View.call_palette_row(wait)

        # 色板栏移动到开头位置
        Pallete.swipe_pallete_row_up(driver, view_ele)

        # 选择墨灰色板
        pallete = 'mohui'
        Pallete.choose_palette(wait, driver, view_ele, pallete)

        # 拍摄照片
        View.take_photo(wait, 1)

        # 进入内部相册
        View.enter_albums(wait)

        # 进入相册页面
        albums.enter_album(wait)

        # 找到第一张照片
        first_photo: WebElement = albums.album.get_latest_file(wait, driver)

        # 进入第一张照片
        first_photo.click()

        # 调用等温尺
        photo.call_thermal_ruler(wait)

        # 判断是否显示等温尺
        try:
            photo.get_thermal_ruler(wait)
        except (NoSuchElementException, InvalidElementStateException, TimeoutException, StaleElementReferenceException):
            assert False, f"{pallete}色板无法调用等温尺，用例失败"

    @pytest.mark.rongyan
    @pytest.mark.temp_ruler
    def test_no_analysis_rongyan_call_thermal_ruler(self, driver, wait):
        """
        测试原色板为熔岩色板，不进入离线分析，能否调用等温尺，预期成功
        :return:
        """
        # 进入设备页面
        startup.enter_device(wait)

        # 进入插件
        device.enter_camera(wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        View.admit_access(wait)

        # 等取景器加载完毕
        time.sleep(10)
        view_ele = View.get_view_element(wait)

        # 展示色板栏
        View.call_palette_row(wait)

        # 色板栏移动到开头位置
        Pallete.swipe_pallete_row_up(driver, view_ele)

        # 选择熔岩色板
        pallete = 'rongyan'
        Pallete.choose_palette(wait, driver, view_ele, pallete)

        # 拍摄照片
        View.take_photo(wait, 1)

        # 进入内部相册
        View.enter_albums(wait)

        # 进入相册页面
        albums.enter_album(wait)

        # 找到第一张照片
        first_photo: WebElement = albums.album.get_latest_file(wait, driver)

        # 进入第一张照片
        first_photo.click()

        # 调用等温尺
        photo.call_thermal_ruler(wait)

        # 判断是否显示等温尺
        try:
            photo.get_thermal_ruler(wait)
        except (NoSuchElementException, InvalidElementStateException, TimeoutException, StaleElementReferenceException):
            assert False, f"{pallete}色板无法调用等温尺，用例失败"
    
    @pytest.mark.gaocaihong
    @pytest.mark.temp_ruler
    def test_no_analysis_gaocaihong_call_thermal_ruler(self, driver, wait):
        """
        测试原色板为高彩虹色板，不进入离线分析，能否调用等温尺，预期成功
        :return:
        """
        # 进入设备页面
        startup.enter_device(wait)

        # 进入插件
        device.enter_camera(wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        View.admit_access(wait)

        # 等取景器加载完毕
        time.sleep(10)
        view_ele = View.get_view_element(wait)

        # 展示色板栏
        View.call_palette_row(wait)

        # 色板栏移动到开头位置
        Pallete.swipe_pallete_row_up(driver, view_ele)

        # 选择高彩虹色板
        pallete = 'gaocaihong'
        Pallete.choose_palette(wait, driver, view_ele, pallete)

        # 拍摄照片
        View.take_photo(wait, 1)

        # 进入内部相册
        View.enter_albums(wait)

        # 进入相册页面
        albums.enter_album(wait)

        # 找到第一张照片
        first_photo: WebElement = albums.album.get_latest_file(wait, driver)

        # 进入第一张照片
        first_photo.click()

        # 调用等温尺
        photo.call_thermal_ruler(wait)

        # 判断是否显示等温尺
        try:
            photo.get_thermal_ruler(wait)
        except (NoSuchElementException, InvalidElementStateException, TimeoutException, StaleElementReferenceException):
            assert False, f"{pallete}色板无法调用等温尺，用例失败"

    @pytest.mark.caihong
    @pytest.mark.temp_ruler
    def test_no_analysis_caihong_call_thermal_ruler(self, driver, wait):
        """
        测试原色板为彩虹色板，不进入离线分析，能否调用等温尺，预期成功
        :return:
        """
        # 进入设备页面
        startup.enter_device(wait)

        # 进入插件
        device.enter_camera(wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        View.admit_access(wait)

        # 等取景器加载完毕
        time.sleep(10)
        view_ele = View.get_view_element(wait)

        # 展示色板栏
        View.call_palette_row(wait)

        # 色板栏移动到开头位置
        Pallete.swipe_pallete_row_up(driver, view_ele)

        # 选择彩虹色板
        pallete = 'caihong'
        Pallete.choose_palette(wait, driver, view_ele, pallete)

        # 拍摄照片
        View.take_photo(wait, 1)

        # 进入内部相册
        View.enter_albums(wait)

        # 进入相册页面
        albums.enter_album(wait)

        # 找到第一张照片
        first_photo: WebElement = albums.album.get_latest_file(wait, driver)

        # 进入第一张照片
        first_photo.click()

        # 调用等温尺
        photo.call_thermal_ruler(wait)

        # 判断是否显示等温尺
        try:
            photo.get_thermal_ruler(wait)
        except (NoSuchElementException, InvalidElementStateException, TimeoutException, StaleElementReferenceException):
            assert False, f"{pallete}色板无法调用等温尺，用例失败"
    
    @pytest.mark.heire
    @pytest.mark.temp_ruler
    def test_no_analysis_heire_call_thermal_ruler(self, driver, wait):
        """
        测试原色板为黑热色板，不进入离线分析，能否调用等温尺，预期失败
        :return:
        """
        # 进入设备页面
        startup.enter_device(wait)

        # 进入插件
        device.enter_camera(wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        View.admit_access(wait)

        # 等取景器加载完毕
        time.sleep(10)
        view_ele = View.get_view_element(wait)

        # 展示色板栏
        View.call_palette_row(wait)

        # 色板栏移动到开头位置
        Pallete.swipe_pallete_row_up(driver, view_ele)

        # 选择黑热色板
        pallete = 'heire'
        Pallete.choose_palette(wait, driver, view_ele, pallete)

        # 拍摄照片
        View.take_photo(wait, 1)

        # 进入内部相册
        View.enter_albums(wait)

        # 进入相册页面
        albums.enter_album(wait)

        # 找到第一张照片
        first_photo: WebElement = albums.album.get_latest_file(wait, driver)

        # 进入第一张照片
        first_photo.click()

        # 调用等温尺
        photo.call_thermal_ruler(wait)

        # 判断是否显示等温尺
        try:
            photo.get_thermal_ruler(wait)
            assert False, f"{pallete}色板可以调用等温尺，用例失败"
        except (NoSuchElementException, InvalidElementStateException, TimeoutException, StaleElementReferenceException):
            pass
    
    @pytest.mark.baire
    @pytest.mark.temp_ruler
    def test_no_analysis_baire_call_thermal_ruler(self, driver, wait):
        """
        测试原色板为白热色板，不进入离线分析，能否调用等温尺，预期失败
        :return:
        """
        # 进入设备页面
        startup.enter_device(wait)

        # 进入插件
        device.enter_camera(wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        View.admit_access(wait)

        # 等取景器加载完毕
        time.sleep(10)
        view_ele = View.get_view_element(wait)

        # 展示色板栏
        View.call_palette_row(wait)

        # 色板栏移动到开头位置
        Pallete.swipe_pallete_row_up(driver, view_ele)

        # 选择白热色板
        pallete = 'baire'
        Pallete.choose_palette(wait, driver, view_ele, pallete)

        # 拍摄照片
        View.take_photo(wait, 1)

        # 进入内部相册
        View.enter_albums(wait)

        # 进入相册页面
        albums.enter_album(wait)

        # 找到第一张照片
        first_photo: WebElement = albums.album.get_latest_file(wait, driver)

        # 进入第一张照片
        first_photo.click()

        # 调用等温尺
        photo.call_thermal_ruler(wait)

        # 判断是否显示等温尺
        try:
            photo.get_thermal_ruler(wait)
            assert False, f"{pallete}色板可以调用等温尺，用例失败"
        except (NoSuchElementException, InvalidElementStateException, TimeoutException, StaleElementReferenceException):
            pass

    @pytest.mark.tiehong
    @pytest.mark.temp_ruler
    def test_no_analysis_tiehong_call_thermal_ruler(self, driver, wait):
        """
        测试原色板为铁红色板，不进入离线分析，能否调用等温尺，预期成功
        :return:
        """
        # 进入设备页面
        startup.enter_device(wait)

        # 进入插件
        device.enter_camera(wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        View.admit_access(wait)

        # 等取景器加载完毕
        time.sleep(10)
        view_ele = View.get_view_element(wait)

        # 展示色板栏
        View.call_palette_row(wait)

        # 色板栏移动到开头位置
        Pallete.swipe_pallete_row_up(driver, view_ele)

        # 选择铁红色板
        pallete = 'tiehong'
        Pallete.choose_palette(wait, driver, view_ele, pallete)

        # 拍摄照片
        View.take_photo(wait, 1)

        # 进入内部相册
        View.enter_albums(wait)

        # 进入相册页面
        albums.enter_album(wait)

        # 找到第一张照片
        first_photo: WebElement = albums.album.get_latest_file(wait, driver)

        # 进入第一张照片
        first_photo.click()

        # 调用等温尺
        photo.call_thermal_ruler(wait)

        # 判断是否显示等温尺
        try:
            photo.get_thermal_ruler(wait)
        except (NoSuchElementException, InvalidElementStateException, TimeoutException, StaleElementReferenceException):
            assert False, f"{pallete}色板无法调用等温尺，用例失败"

@allure.epic("inside")
@allure.feature("photo")
@pytest.mark.inside
@pytest.mark.photo
@pytest.mark.analysis
class TestAnalysis:
    
    @pytest.mark.baire
    @pytest.mark.temp_ruler
    def test_analysis_baire_call_thermal_ruler(self, driver, wait):
        """
        测试进入离线分析，调整色板为白热色板，能否调用等温尺，预期失败
        :return:
        """
        # 进入设备页面
        startup.enter_device(wait)

        # 进入插件
        device.enter_camera(wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        View.admit_access(wait)

        # 等取景器加载完毕
        time.sleep(10)
        view_ele = View.get_view_element(wait)

        # 拍摄照片
        View.take_photo(wait, 1)

        # 进入内部相册
        View.enter_albums(wait)

        # 进入相册页面
        albums.enter_album(wait)

        # 找到第一张照片
        first_photo: WebElement = albums.album.get_latest_file(wait, driver)

        # 进入第一张照片
        first_photo.click()

        # 进入离线分析
        photo.enter_analysis(wait)

        # 获取照片主体元素
        photo_view = photo.get_photo_view(wait)

        # 展示色板栏
        Analysis.call_pallete(wait)

        # 向右滑动到头
        AnalysisPallete.swipe_pallete_row_right(driver,photo_view)

        # 选择白热色板
        pallete = 'baire'
        AnalysisPallete.choose_palette(wait, driver, photo_view, pallete)

        # 调用等温尺
        photo.call_thermal_ruler(wait)

        # 判断是否显示等温尺
        try:
            photo.get_thermal_ruler(wait)
            assert False, f"{pallete}色板可以调用等温尺，用例失败"
        except (NoSuchElementException, InvalidElementStateException, TimeoutException, StaleElementReferenceException):
            pass

    @pytest.mark.heire
    @pytest.mark.temp_ruler
    def test_analysis_heire_call_thermal_ruler(self, driver, wait):
        """
        测试进入离线分析，调整色板为黑热色板，能否调用等温尺，预期失败
        :return:
        """
        # 进入设备页面
        startup.enter_device(wait)

        # 进入插件
        device.enter_camera(wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        View.admit_access(wait)

        # 等取景器加载完毕
        time.sleep(10)
        view_ele = View.get_view_element(wait)

        # 拍摄照片
        View.take_photo(wait, 1)

        # 进入内部相册
        View.enter_albums(wait)

        # 进入相册页面
        albums.enter_album(wait)

        # 找到第一张照片
        first_photo: WebElement = albums.album.get_latest_file(wait, driver)

        # 进入第一张照片
        first_photo.click()

        # 进入离线分析
        photo.enter_analysis(wait)

        # 获取照片主体元素
        photo_view = photo.get_photo_view(wait)

        # 展示色板栏
        Analysis.call_pallete(wait)

        # 向右滑动到头
        AnalysisPallete.swipe_pallete_row_right(driver, photo_view)

        # 选择黑热色板
        pallete = 'heire'
        AnalysisPallete.choose_palette(wait, driver, photo_view, pallete)

        # 调用等温尺
        photo.call_thermal_ruler(wait)

        # 判断是否显示等温尺
        try:
            photo.get_thermal_ruler(wait)
            assert False, f"{pallete}色板可以调用等温尺，用例失败"
        except (NoSuchElementException, InvalidElementStateException, TimeoutException, StaleElementReferenceException):
            pass
    
    @pytest.mark.hongtou
    @pytest.mark.temp_ruler
    def test_analysis_hongtou_call_thermal_ruler(self, driver, wait):
        """
        测试进入离线分析，调整色板为红头色板，能否调用等温尺，预期失败
        :return:
        """
        # 进入设备页面
        startup.enter_device(wait)

        # 进入插件
        device.enter_camera(wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        View.admit_access(wait)

        # 等取景器加载完毕
        time.sleep(10)
        view_ele = View.get_view_element(wait)

        # 拍摄照片
        View.take_photo(wait, 1)

        # 进入内部相册
        View.enter_albums(wait)

        # 进入相册页面
        albums.enter_album(wait)

        # 找到第一张照片
        first_photo: WebElement = albums.album.get_latest_file(wait, driver)

        # 进入第一张照片
        first_photo.click()

        # 进入离线分析
        photo.enter_analysis(wait)

        # 获取照片主体元素
        photo_view = photo.get_photo_view(wait)

        # 展示色板栏
        Analysis.call_pallete(wait)

        # 向右滑动到头
        AnalysisPallete.swipe_pallete_row_right(driver, photo_view)

        # 选择红头色板
        pallete = 'hongtou'
        AnalysisPallete.choose_palette(wait, driver, photo_view, pallete)

        # 调用等温尺
        photo.call_thermal_ruler(wait)

        # 判断是否显示等温尺
        try:
            photo.get_thermal_ruler(wait)
            assert False, f"{pallete}色板可以调用等温尺，用例失败"
        except (NoSuchElementException, InvalidElementStateException, TimeoutException, StaleElementReferenceException):
            pass
    
    @pytest.mark.tiehong
    @pytest.mark.temp_ruler
    def test_analysis_tiehong_call_thermal_ruler(self, driver, wait):
        """
        测试进入离线分析，调整色板为铁红色板，能否调用等温尺，预期成功
        :return:
        """
        # 进入设备页面
        startup.enter_device(wait)

        # 进入插件
        device.enter_camera(wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        View.admit_access(wait)

        # 等取景器加载完毕
        time.sleep(10)
        view_ele = View.get_view_element(wait)

        # 拍摄照片
        View.take_photo(wait, 1)

        # 进入内部相册
        View.enter_albums(wait)

        # 进入相册页面
        albums.enter_album(wait)

        # 找到第一张照片
        first_photo: WebElement = albums.album.get_latest_file(wait, driver)

        # 进入第一张照片
        first_photo.click()

        # 进入离线分析
        photo.enter_analysis(wait)

        # 获取照片主体元素
        photo_view = photo.get_photo_view(wait)

        # 展示色板栏
        Analysis.call_pallete(wait)

        # 向右滑动到头
        AnalysisPallete.swipe_pallete_row_right(driver, photo_view)

        # 选择铁红色板
        pallete = 'tiehong'
        AnalysisPallete.choose_palette(wait, driver, photo_view, pallete)

        # 调用等温尺
        photo.call_thermal_ruler(wait)

        # 判断是否显示等温尺
        try:
            photo.get_thermal_ruler(wait)
        except (NoSuchElementException, InvalidElementStateException, TimeoutException, StaleElementReferenceException):
            assert False, f"{pallete}色板调用等温尺失败，用例失败"
    
    @pytest.mark.gaocaihong
    @pytest.mark.temp_ruler
    def test_analysis_gaocaihong_call_thermal_ruler(self, driver, wait):
        """
        测试进入离线分析，调整色板为高彩虹色板，能否调用等温尺，预期成功
        :return:
        """
        # 进入设备页面
        startup.enter_device(wait)

        # 进入插件
        device.enter_camera(wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        View.admit_access(wait)

        # 等取景器加载完毕
        time.sleep(10)
        view_ele = View.get_view_element(wait)

        # 拍摄照片
        View.take_photo(wait, 1)

        # 进入内部相册
        View.enter_albums(wait)

        # 进入相册页面
        albums.enter_album(wait)

        # 找到第一张照片
        first_photo: WebElement = albums.album.get_latest_file(wait, driver)

        # 进入第一张照片
        first_photo.click()

        # 进入离线分析
        photo.enter_analysis(wait)

        # 获取照片主体元素
        photo_view = photo.get_photo_view(wait)

        # 展示色板栏
        Analysis.call_pallete(wait)

        # 向右滑动到头
        AnalysisPallete.swipe_pallete_row_right(driver, photo_view)

        # 选择高彩虹色板
        pallete = 'gaocaihong'
        AnalysisPallete.choose_palette(wait, driver, photo_view, pallete)

        # 调用等温尺
        photo.call_thermal_ruler(wait)

        # 判断是否显示等温尺
        try:
            photo.get_thermal_ruler(wait)
        except (NoSuchElementException, InvalidElementStateException, TimeoutException, StaleElementReferenceException):
            assert False, f"{pallete}色板调用等温尺失败，用例失败"
    
    @pytest.mark.caihong
    @pytest.mark.temp_ruler
    def test_analysis_caihong_call_thermal_ruler(self, driver, wait):
        """
        测试进入离线分析，调整色板为彩虹色板，能否调用等温尺，预期成功
        :return:
        """
        # 进入设备页面
        startup.enter_device(wait)

        # 进入插件
        device.enter_camera(wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        View.admit_access(wait)

        # 等取景器加载完毕
        time.sleep(10)
        view_ele = View.get_view_element(wait)

        # 拍摄照片
        View.take_photo(wait, 1)

        # 进入内部相册
        View.enter_albums(wait)

        # 进入相册页面
        albums.enter_album(wait)

        # 找到第一张照片
        first_photo: WebElement = albums.album.get_latest_file(wait, driver)

        # 进入第一张照片
        first_photo.click()

        # 进入离线分析
        photo.enter_analysis(wait)

        # 获取照片主体元素
        photo_view = photo.get_photo_view(wait)

        # 展示色板栏
        Analysis.call_pallete(wait)

        # 向右滑动到头
        AnalysisPallete.swipe_pallete_row_right(driver, photo_view)

        # 选择彩虹色板
        pallete = 'caihong'
        AnalysisPallete.choose_palette(wait, driver, photo_view, pallete)

        # 调用等温尺
        photo.call_thermal_ruler(wait)

        # 判断是否显示等温尺
        try:
            photo.get_thermal_ruler(wait)
        except (NoSuchElementException, InvalidElementStateException, TimeoutException, StaleElementReferenceException):
            assert False, f"{pallete}色板调用等温尺失败，用例失败"
    
    @pytest.mark.tiehui
    @pytest.mark.temp_ruler
    def test_analysis_tiehui_call_thermal_ruler(self, driver, wait):
        """
        测试进入离线分析，调整色板为铁灰色板，能否调用等温尺，预期成功
        :return:
        """
        # 进入设备页面
        startup.enter_device(wait)

        # 进入插件
        device.enter_camera(wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        View.admit_access(wait)

        # 等取景器加载完毕
        time.sleep(10)

        # 拍摄照片
        View.take_photo(wait, 1)

        # 进入内部相册
        View.enter_albums(wait)

        # 进入相册页面
        albums.enter_album(wait)

        # 找到第一张照片
        first_photo: WebElement = albums.album.get_latest_file(wait, driver)

        # 进入第一张照片
        first_photo.click()

        # 进入离线分析
        photo.enter_analysis(wait)

        # 获取照片主体元素
        photo_view = photo.get_photo_view(wait)

        # 展示色板栏
        Analysis.call_pallete(wait)

        # 向右滑动到头
        AnalysisPallete.swipe_pallete_row_right(driver, photo_view)

        # 选择铁灰色板
        pallete = 'tiehui'
        AnalysisPallete.choose_palette(wait, driver, photo_view, pallete)

        # 调用等温尺
        photo.call_thermal_ruler(wait)

        # 判断是否显示等温尺
        try:
            photo.get_thermal_ruler(wait)
        except (NoSuchElementException, InvalidElementStateException, TimeoutException, StaleElementReferenceException):
            assert False, f"{pallete}色板调用等温尺失败，用例失败"