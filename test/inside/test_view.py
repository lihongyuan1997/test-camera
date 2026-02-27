import time
import pytest, allure
import pytest_check as check
from appium.webdriver import WebElement
from selenium.common import NoSuchElementException, InvalidElementStateException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utility import *
from page.outside import  startup, device, gallery
from page.inside.albums import *
from page.inside.view import View, MeasureTempTool, ImageSetting, Pallete

@allure.epic("inside")
@allure.feature("view")
class TestView:
    """
    测试取景、拍照、录像、跳转到其他页面等功能
    """
    data = read_csv_by_dict('data/take_photo_data.csv')
    take_photo_count = []
    for d in data:
        take_photo_count.append(d['count'])

    def test_view_show(self, driver, wait):
        """
        测试取景器是否显示
        :return: 
        """
        # 进入插件
        device.enter_camera(wait)

        # 如果弹框需要授权APP访问camera+，点击允许
        View.admit_access(wait)

        # 找到取景器元素
        View.get_view_element(wait)

    @allure.story("page_switch")
    def test_enter_inside_setting(self, driver, wait):
        """
        测试从取景器跳转到内部设置页面
        :return:
        """
        # 进入插件
        device.enter_camera(wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        View.admit_access(wait)

        # 找到取景器元素
        View.get_view_element(wait)

        # 进入设置页面
        View.enter_setting(wait)

        # 判断是否进入设置成功
        try:
            setting: WebElement = wait.until \
                (method=EC.presence_of_element_located \
                    (locator=(By.ID, "com.inreii.neutralapp:id/title_content")))
            assert setting.text == "Settings", "设置页面名称错误，进入设置页面失败"
        except (NoSuchElementException, InvalidElementStateException, TimeoutException):
            assert False, "未找到设置页面名称元素，进入设置页面失败"

    @allure.story("page_switch")
    def test_enter_inside_albums(self, driver, wait):
        """
        测试从取景器跳转到相册
        :return:
        """
        # 进入插件
        device.enter_camera(wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        View.admit_access(wait)

        # 找到取景器元素
        View.get_view_element(wait)

        # 进入相册
        View.enter_albums(wait)

        # 判断是否进入相册成功
        try:
            album: WebElement = wait.until \
                (method=EC.presence_of_element_located \
                    (locator=(By.ID, "com.inreii.neutralapp:id/title_content")))
            assert album.text == "Albums", "相册页面名称错误，进入相册页面失败"
        except (NoSuchElementException, InvalidElementStateException, TimeoutException):
            assert False, "未找到相册页面名称元素，进入相册页面失败"

    @pytest.mark.parametrize(argnames='n', argvalues=take_photo_count)
    def test_take_photo_check_inside(self, n, driver, wait):
        """
        测试拍摄n张照片，内部相册是否生成照片成功
        :return:
        """
        # 进入插件
        device.enter_camera(wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        View.admit_access(wait)

        # 找到取景器元素
        View.get_view_element(wait)

        time.sleep(5)

        # 进入内部相册
        View.enter_albums(wait)
        enter_album(wait)

        # 获取拍摄前的照片/视频数量
        files_number_before = album.get_files_number(driver, wait)
        print_diy(f'拍摄前的照片/视频数量: {files_number_before}')

        # 返回取景页面
        back_last_page(wait)

        # 拍摄n张照片
        View.take_photo(wait, int(n))

        # 进入内部相册界面
        View.enter_albums(wait)
        enter_album(wait)

        # 获取拍摄后的照片/视频数量
        files_number_after = album.get_files_number(driver, wait)
        print_diy(f'拍摄后的照片/视频数量: {files_number_after}')

        assert files_number_after == files_number_before + int(n), '照片存在拍摄失败的情况'

    @pytest.mark.parametrize(argnames='n, t', argvalues=[(5, 5)])
    def test_take_video_check_inside(self, n: int, t: int, driver, wait):
        """
        测试拍摄n段视频，内部相册是否生成视频成功
        :return:
        """
        # 进入插件
        device.enter_camera(wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        View.admit_access(wait)

        #找到取景器元素
        View.get_view_element(wait)

        # 进入内部相册
        View.enter_albums(wait)
        albums.enter_album(wait)

        print("-------------------------------------------------【拍摄前】-------------------------------------------------")

        # 找到相册里拍摄前第一个文件，如果存在，获取标题；如果不存在，设置标题为空
        latest_file: WebElement | None = albums.album.get_latest_file(wait, driver)
        if latest_file:
            # 进入文件详情
            latest_file.click()
            latest_file_title: str = albums.album.get_title(wait)
            # 返回相册界面
            back_last_page(wait)
        else:
            latest_file_title: str = ''

        # 返回取景页面
        back_last_page(wait)

        # 拍摄n段视频，每段视频t秒
        View.take_video(wait, n, t)

        print("-------------------------------------------------------【拍摄后】--------------------------------------------------------")

        # 等待3s进入相册界面
        time.sleep(3)

        # 进入内部相册界面
        View.enter_albums(wait)
        albums.enter_album(wait)

        # 如果拍摄前至少存在一个文件，则找到拍摄后相册里前n+1文件; 否则找到前n个文件
        if latest_file_title:
            after_files_titles: list[str] = albums.album.get_all_titles(wait, driver, n + 1)
            print("拍摄后的相册里的所有文件标题：", after_files_titles)
            expr: bool = after_files_titles[-1] == latest_file_title and len(set(after_files_titles)) == len(after_files_titles) == n + 1
            assert expr, '视频拍摄存在失败，或者内部相册存储视频存在失败'
        else:
            after_files_titles: list[str] = albums.album.get_all_titles(wait, driver, n)
            print("拍摄后的相册里的所有文件标题：", after_files_titles)
            expr: bool = len(set(after_files_titles)) == len(after_files_titles) == n
            assert expr, '视频拍摄存在失败，或者内部相册存储视频存在失败'

    @pytest.mark.parametrize(argnames='n', argvalues=[5])
    def test_take_photo_check_outside(self, n: int, driver, wait):
        """
        测试拍摄n张照片，外部相册是否生成照片成功
        :return:
        """
        print("--------------------------------------【拍摄前】---------------------------------------")

        # 进入外壳相册
        startup.enter_gallery(wait)
        gallery.enter_album(wait)

        # 找到相册里拍摄前第一个文件，如果存在，获取标题；如果不存在，设置标题为空
        latest_file: WebElement | None = gallery.album.get_latest_file(wait, driver)
        if latest_file:
            # 进入第一个文件详情
            latest_file.click()
            latest_file_title: str = gallery.photo.get_title(wait)
            # 返回相册界面
            back_last_page(wait)
        else:
            latest_file_title: str = ''

        # 进入设备页面
        startup.enter_device(wait)

        # 进入插件
        device.enter_camera(wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        View.admit_access(wait)

        # 找到取景器元素
        View.get_view_element(wait)

        # 拍摄n张照片
        View.take_photo(wait, n)

        print("---------------------------------------【拍摄后】--------------------------------------")

        # 返回外壳界面
        View.back_shell(wait)

        # 进入外壳相册界面
        startup.enter_gallery(wait)
        gallery.enter_album(wait)

        # 如果拍摄前至少存在一个文件，则找到拍摄后相册里前n+1文件; 否则找到前n个文件
        if latest_file_title:
            after_files_titles: list[str] = gallery.album.get_all_titles(wait, driver, n + 1)
            print("拍摄后的相册里的所有文件标题：", after_files_titles)
            expr: bool = after_files_titles[-1] == latest_file_title and len(set(after_files_titles)) == len(
                after_files_titles) == n + 1
            assert expr, '照片拍摄存在失败，或者外壳相册存储照片存在失败'
        else:
            after_files_titles: list[str] = gallery.album.get_all_titles(wait, driver, n)
            print("拍摄后的相册里的所有文件标题：", after_files_titles)
            expr: bool = len(set(after_files_titles)) == len(after_files_titles) == n
            assert expr, '照片拍摄存在失败，或者外壳相册存储照片存在失败'

    @pytest.mark.parametrize(argnames='n, t', argvalues=[(5, 5)])
    def test_take_video_check_outside(self, n: int, t: int, driver, wait):
        """
        测试拍摄n段视频，外部相册是否生成视频成功
        :return:
        """
        print("--------------------------------------【拍摄前】---------------------------------------")

        # 进入外壳相册
        startup.enter_gallery(wait)

        # 找到相册里拍摄前第一个文件，如果存在，获取标题；如果不存在，设置标题为空
        latest_file: WebElement | None = gallery.album.get_latest_file(wait, driver)
        if latest_file:
            # 进入第一个文件详情
            latest_file.click()
            latest_file_title: str = gallery.photo.get_title(wait)
            # 返回相册界面
            back_last_page(wait)
        else:
            latest_file_title: str = ''

        # 进入设备页面
        startup.enter_device(wait)

        # 进入插件
        device.enter_camera(wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        View.admit_access(wait)

        # 找到取景器元素
        View.get_view_element(wait)

        # 拍摄n段视频
        View.take_video(wait, n, t)

        print("---------------------------------------【拍摄后】--------------------------------------")

        # 返回外壳界面
        View.back_shell(wait)

        # 进入外壳相册界面
        startup.enter_gallery(wait)

        # 如果拍摄前至少存在一个文件，则找到拍摄后相册里前n+1文件; 否则找到前n个文件
        if latest_file_title:
            after_files_titles: list[str] = gallery.album.get_all_titles(wait, driver, n + 1)
            print("拍摄后的相册里的所有文件标题：", after_files_titles)
            expr: bool = after_files_titles[-1] == latest_file_title and len(set(after_files_titles)) == len(
                after_files_titles) == n + 1
            assert expr, '视频拍摄存在失败，或者外壳相册存储视频存在失败'
        else:
            after_files_titles: list[str] = gallery.album.get_all_titles(wait, driver, n)
            print("拍摄后的相册里的所有文件标题：", after_files_titles)
            expr: bool = len(set(after_files_titles)) == len(after_files_titles) == n
            assert expr, '视频拍摄存在失败，或者外壳相册存储视频存在失败'

class TestPictureInPicture:
    """
    测试画中画调用及拖动
    """
    @allure.story("picture_in_picture")
    def test_call_picture_in_picture(self, driver, wait):
        """
        测试调用画中画
        :return:
        """
        # 进入插件
        device.enter_camera(wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        View.admit_access(wait)

        # 找到取景器元素
        View.get_view_element(wait)

        # 调用画中画
        View.call_picture_in_picture(driver, wait)

        # 判断画中画是否调用成功
        View.get_picture_in_picture(wait)

    @allure.story("picture_in_picture")
    def test_drag_picture_in_picture(self, driver, wait):
        """
        测试拖动画中画
        :return:
        """
        # 进入插件
        device.enter_camera(wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        View.admit_access(wait)

        # 找到取景器元素
        view_ele = View.get_view_element(wait)

        # 调用画中画
        View.call_picture_in_picture(driver, wait)

        # 获取画中画元素
        pip = View.get_picture_in_picture(wait)

        # 画中画的中心坐标
        pip_x = pip.location['x'] + 0.5 * pip.size['width']
        pip_y = pip.location['y'] + 0.5 * pip.size['height']

        # 取景器的中心坐标
        view_x = view_ele.location['x'] + 0.5 * view_ele.size['width']
        view_y = view_ele.location['y'] + 0.5 * view_ele.size['height']

        # 拖动画中画
        # drag_by_coordinate(driver, pip_x, pip_y, view_x, view_y)
        driver.swipe(pip_x, pip_y, view_x, view_y)

class TestMeasureTemp:
    """
    测试测温工具功能
    """
    @allure.story("measure_temp")
    def test_call_measure_temp_row(self, driver, wait):
        """
        测试调出测温工具栏
        :return:
        """
        # 进入插件
        device.enter_camera(wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        View.admit_access(wait)

        # 找到取景器元素
        View.get_view_element(wait)

        # 点击调用测温工具栏图标
        View.call_measure_temp_tool(wait)

        # 判断各测温工具是否展示
        try:
            MeasureTempTool.get_center_temp_icon(wait)
            MeasureTempTool.get_max_temp_icon(wait)
            MeasureTempTool.get_min_temp_icon(wait)
            MeasureTempTool.get_point_temp_icon(wait)
            MeasureTempTool.get_line_temp_icon(wait)
            MeasureTempTool.get_rectangle_temp_icon(wait)
            MeasureTempTool.get_del_temp_icon(wait)
        except(NoSuchElementException, StaleElementReferenceException, InvalidElementStateException, TimeoutException):
            assert False, "调用测温工具栏失败"

    
    @allure.story("measure_temp")
    def test_show_central_temp(self, driver, wait):
        """
        测试显示中心温度
        :return:
        """
        # 进入插件
        device.enter_camera(wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        View.admit_access(wait)

        # 找到取景器元素
        View.get_view_element(wait)

        # 点击调用测温工具栏图标
        View.call_measure_temp_tool(wait)

        # 获取取景器元素截图
        view_ele: WebElement = View.get_view_element(wait)
        capture_element_screenshot(driver, view_ele)

class TestTempRuler:
    """
    测试等温尺功能
    由于每次测试会默认打开铁红色板和等温尺，所以切换到不支持色板，等温尺会消失，切换到支持色板，等温尺保留
    """
    @allure.story("temp_ruler")
    def test_temp_ruler_default_show(self, driver, wait):
        """
        测试等温尺是否默认被调用
        :return:
        """
        # 进入插件
        device.enter_camera(wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        View.admit_access(wait)

        # 找到取景器元素
        View.get_view_element(wait)

        # 判断等温尺是否被默认调用
        try:
            View.get_temp_ruler(wait)
        except(NoSuchElementException, StaleElementReferenceException, InvalidElementStateException, TimeoutException):
            assert False, "等温尺没有被默认调用"

    
    @allure.story("temp_ruler")
    @allure.suite("bingleng")
    @pytest.mark.bingleng
    def test_temp_ruler_exist_pallete_switch_to_bingleng(self, driver, wait):
        """
        测试等温尺已经被调用，色板切换为冰冷色板，等温尺是否还存在
        :return:
        """
        # 进入插件
        device.enter_camera(wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        View.admit_access(wait)

        # 找到取景器元素
        view_ele = View.get_view_element(wait)

        # 点击展示色板栏
        View.call_palette_row(wait)

        # 向上滑动色板栏
        Pallete.swipe_pallete_row_up(driver, view_ele)

        # 选择冰冷色板
        pallete = "bingleng"
        Pallete.choose_palette(wait, driver, view_ele, pallete)

        # 判断等温尺是否存在
        try:
            View.get_temp_ruler(wait)
            assert False, f"{pallete}色板，等温尺依旧存在"
        except(NoSuchElementException, StaleElementReferenceException, InvalidElementStateException,
               TimeoutException):
            pass

    
    @allure.story("temp_ruler")
    @allure.suite("bingleng")
    @pytest.mark.bingleng
    def test_bingleng_call_temp_ruler(self, driver, wait):
        """
        测试冰冷色板能否调用等温尺，预期不能
        :return:
        """
        # 进入插件
        device.enter_camera(wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        View.admit_access(wait)

        # 找到取景器元素
        view_ele = View.get_view_element(wait)

        # 点击展示色板栏
        View.call_palette_row(wait)

        # 向上滑动色板栏
        Pallete.swipe_pallete_row_up(driver, view_ele)

        # 选择冰冷色板
        pallete = "bingleng"
        Pallete.choose_palette(wait, driver, view_ele, pallete)

        # 点击调用等温尺
        View.call_temp_ruler(wait)

        # 判断等温尺是否调用成功
        try:
            View.get_temp_ruler(wait)
            assert False, f"{pallete}色板调用等温尺成功"
        except(NoSuchElementException, StaleElementReferenceException, InvalidElementStateException,
               TimeoutException):
            pass

    
    @allure.story("temp_ruler")
    @allure.suite("hongtou")
    @pytest.mark.hongtou
    def test_temp_ruler_exist_pallete_switch_to_hongtou(self, driver, wait):
        """
        测试等温尺已经被调用，色板切换为红头色板，等温尺是否还存在
        :return:
        """
        # 进入插件
        device.enter_camera(wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        View.admit_access(wait)

        # 找到取景器元素
        view_ele = View.get_view_element(wait)

        # 点击展示色板栏
        View.call_palette_row(wait)

        # 向上滑动色板栏
        Pallete.swipe_pallete_row_up(driver, view_ele)

        # 选择红头色板
        pallete = "hongtou"
        Pallete.choose_palette(wait, driver, view_ele, pallete)

        # 判断等温尺是否存在
        try:
            View.get_temp_ruler(wait)
            assert False, f"{pallete}色板，等温尺依旧存在"
        except(NoSuchElementException, StaleElementReferenceException, InvalidElementStateException, TimeoutException):
            pass

    
    @allure.story("temp_ruler")
    @allure.suite("hongtou")
    @pytest.mark.hongtou
    def test_hongtou_call_temp_ruler(self, driver, wait):
        """
        测试红头色板能否调用等温尺，预期不能
        :return:
        """
        # 进入插件
        device.enter_camera(wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        View.admit_access(wait)

        # 找到取景器元素
        view_ele = View.get_view_element(wait)

        # 点击展示色板栏
        View.call_palette_row(wait)

        # 向上滑动色板栏
        Pallete.swipe_pallete_row_up(driver, view_ele)

        # 选择红头色板
        pallete = "hongtou"
        Pallete.choose_palette(wait, driver, view_ele, pallete)

        # 点击调用等温尺
        View.call_temp_ruler(wait)

        # 判断等温尺是否调用成功
        try:
            View.get_temp_ruler(wait)
            assert False, f"{pallete}色板调用等温尺成功"
        except(NoSuchElementException, StaleElementReferenceException, InvalidElementStateException,
               TimeoutException):
            pass

    
    @allure.story("temp_ruler")
    @allure.suite("tiehui")
    @pytest.mark.tiehui
    def test_temp_ruler_exist_pallete_switch_to_tiehui(self, driver, wait):
        """
        测试等温尺已经被调用，色板切换为铁灰色板，等温尺是否还存在，预期存在
        :return:
        """
        # 进入插件
        device.enter_camera(wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        View.admit_access(wait)

        # 找到取景器元素
        view_ele = View.get_view_element(wait)

        # 点击展示色板栏
        View.call_palette_row(wait)

        # 向上滑动色板栏
        Pallete.swipe_pallete_row_up(driver, view_ele)

        # 选择铁灰色板
        pallete = "tiehui"
        Pallete.choose_palette(wait, driver, view_ele, pallete)

        # 判断等温尺是否存在
        try:
            View.get_temp_ruler(wait)
        except(NoSuchElementException, StaleElementReferenceException, InvalidElementStateException, TimeoutException):
            assert False, f"{pallete}色板，等温尺不存在"

    
    @allure.story("temp_ruler")
    @allure.suite("tiehui")
    @pytest.mark.tiehui
    def test_tiehui_cancel_call_temp_ruler(self, driver, wait):
        """
        测试铁灰色板能否取消调用等温尺，预期可以
        :return:
        """
        # 进入插件
        device.enter_camera(wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        View.admit_access(wait)

        # 找到取景器元素
        view_ele = View.get_view_element(wait)

        # 点击展示色板栏
        View.call_palette_row(wait)

        # 向上滑动色板栏
        Pallete.swipe_pallete_row_up(driver, view_ele)

        # 选择铁灰色板
        pallete = "tiehui"
        Pallete.choose_palette(wait, driver, view_ele, pallete)

        # 点击取消调用等温尺
        View.call_temp_ruler(wait)

        # 判断等温尺是否取消调用成功
        try:
            View.get_temp_ruler(wait)
            assert False, f"{pallete}色板，取消调用等温尺失败"
        except(NoSuchElementException, StaleElementReferenceException, InvalidElementStateException,
               TimeoutException):
            pass

    
    @allure.story("temp_ruler")
    @allure.suite("tiehui")
    @pytest.mark.tiehui
    def test_tiehui_call_temp_ruler(self, driver, wait):
        """
        测试铁灰色板能否调用等温尺，预期可以
        :return:
        """
        # 进入插件
        device.enter_camera(wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        View.admit_access(wait)

        # 找到取景器元素
        view_ele = View.get_view_element(wait)

        # 点击展示色板栏
        View.call_palette_row(wait)

        # 向上滑动色板栏
        Pallete.swipe_pallete_row_up(driver, view_ele)

        # 选择铁灰色板
        pallete = "tiehui"
        Pallete.choose_palette(wait, driver, view_ele, pallete)

        # 点击取消调用等温尺
        View.call_temp_ruler(wait)

        # 点击调用等温尺
        View.call_temp_ruler(wait)

        # 判断等温尺是否调用成功
        try:
            View.get_temp_ruler(wait)
        except(NoSuchElementException, StaleElementReferenceException, InvalidElementStateException,
               TimeoutException):
            assert False, f"{pallete}色板，调用等温尺失败"

    
    @allure.story("temp_ruler")
    @allure.suite("mohui")
    @pytest.mark.mohui
    def test_temp_ruler_exist_pallete_switch_to_mohui(self, driver, wait):
        """
        测试等温尺已经被调用，色板切换为墨灰色板，等温尺是否还存在，预期存在
        :return:
        """
        # 进入插件
        device.enter_camera(wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        View.admit_access(wait)

        # 找到取景器元素
        view_ele = View.get_view_element(wait)

        # 点击展示色板栏
        View.call_palette_row(wait)

        # 向上滑动色板栏
        Pallete.swipe_pallete_row_up(driver, view_ele)

        # 选择墨灰色板
        pallete = "mohui"
        Pallete.choose_palette(wait, driver, view_ele, pallete)

        # 判断等温尺是否存在
        try:
            View.get_temp_ruler(wait)
        except(NoSuchElementException, StaleElementReferenceException, InvalidElementStateException, TimeoutException):
            assert False, f"{pallete}色板，等温尺不存在"

    
    @allure.story("temp_ruler")
    @allure.suite("mohui")
    @pytest.mark.mohui
    def test_mohui_cancel_call_temp_ruler(self, driver, wait):
        """
        测试墨灰色板能否取消调用等温尺，预期可以
        :return:
        """
        # 进入插件
        device.enter_camera(wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        View.admit_access(wait)

        # 找到取景器元素
        view_ele = View.get_view_element(wait)

        # 点击展示色板栏
        View.call_palette_row(wait)

        # 向上滑动色板栏
        Pallete.swipe_pallete_row_up(driver, view_ele)

        # 选择墨灰色板
        pallete = "mohui"
        Pallete.choose_palette(wait, driver, view_ele, pallete)

        # 点击取消调用等温尺
        View.call_temp_ruler(wait)

        # 判断等温尺是否取消调用成功
        try:
            View.get_temp_ruler(wait)
            assert False, f"{pallete}色板，取消调用等温尺失败"
        except(NoSuchElementException, StaleElementReferenceException, InvalidElementStateException,
               TimeoutException):
            pass

    
    @allure.story("temp_ruler")
    @allure.suite("mohui")
    @pytest.mark.mohui
    def test_mohui_call_temp_ruler(self, driver, wait):
        """
        测试墨灰色板能否调用等温尺，预期可以
        :return:
        """
        # 进入插件
        device.enter_camera(wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        View.admit_access(wait)

        # 找到取景器元素
        view_ele = View.get_view_element(wait)

        # 点击展示色板栏
        View.call_palette_row(wait)

        # 向上滑动色板栏
        Pallete.swipe_pallete_row_up(driver, view_ele)

        # 选择墨灰色板
        pallete = "mohui"
        Pallete.choose_palette(wait, driver, view_ele, pallete)

        # 点击取消调用等温尺
        View.call_temp_ruler(wait)

        # 点击调用等温尺
        View.call_temp_ruler(wait)

        # 判断等温尺是否调用成功
        try:
            View.get_temp_ruler(wait)
        except(NoSuchElementException, StaleElementReferenceException, InvalidElementStateException,
               TimeoutException):
            assert False, f"{pallete}色板，调用等温尺失败"

    
    @allure.story("temp_ruler")
    @allure.suite("gaocaihong")
    @pytest.mark.gaocaihong
    def test_temp_ruler_exist_pallete_switch_to_gaocaihong(self, driver, wait):
        """
        测试等温尺已经被调用，色板切换为高彩虹色板，等温尺是否还存在，预期存在
        :return:
        """
        # 进入插件
        device.enter_camera(wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        View.admit_access(wait)

        # 找到取景器元素
        view_ele = View.get_view_element(wait)

        # 点击展示色板栏
        View.call_palette_row(wait)

        # 向上滑动色板栏
        Pallete.swipe_pallete_row_up(driver, view_ele)

        # 选择高彩虹色板
        pallete = "gaocaihong"
        Pallete.choose_palette(wait, driver, view_ele, pallete)

        # 判断等温尺是否存在
        try:
            View.get_temp_ruler(wait)
        except(NoSuchElementException, StaleElementReferenceException, InvalidElementStateException, TimeoutException):
            assert False, f"{pallete}色板，等温尺不存在"

    
    @allure.story("temp_ruler")
    @allure.suite("gaocaihong")
    @pytest.mark.gaocaihong
    def test_gaocaihong_cancel_call_temp_ruler(self, driver, wait):
        """
        测试高彩虹色板能否取消调用等温尺，预期可以
        :return:
        """
        # 进入插件
        device.enter_camera(wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        View.admit_access(wait)

        # 找到取景器元素
        view_ele = View.get_view_element(wait)

        # 点击展示色板栏
        View.call_palette_row(wait)

        # 向上滑动色板栏
        Pallete.swipe_pallete_row_up(driver, view_ele)

        # 选择高彩虹色板
        pallete = "gaocaihong"
        Pallete.choose_palette(wait, driver, view_ele, pallete)

        # 点击取消调用等温尺
        View.call_temp_ruler(wait)

        # 判断等温尺是否取消调用成功
        try:
            View.get_temp_ruler(wait)
            assert False, f"{pallete}色板，取消调用等温尺失败"
        except(NoSuchElementException, StaleElementReferenceException, InvalidElementStateException,
               TimeoutException):
            pass

    
    @allure.story("temp_ruler")
    @allure.suite("gaocaihong")
    @pytest.mark.gaocaihong
    def test_gaocaihong_call_temp_ruler(self, driver, wait):
        """
        测试高彩虹色板能否调用等温尺，预期可以
        :return:
        """
        # 进入插件
        device.enter_camera(wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        View.admit_access(wait)

        # 找到取景器元素
        view_ele = View.get_view_element(wait)

        # 点击展示色板栏
        View.call_palette_row(wait)

        # 向上滑动色板栏
        Pallete.swipe_pallete_row_up(driver, view_ele)

        # 选择高彩虹色板
        pallete = "gaocaihong"
        Pallete.choose_palette(wait, driver, view_ele, pallete)

        # 点击取消调用等温尺
        View.call_temp_ruler(wait)

        # 点击调用等温尺
        View.call_temp_ruler(wait)

        # 判断等温尺是否调用成功
        try:
            View.get_temp_ruler(wait)
        except(NoSuchElementException, StaleElementReferenceException, InvalidElementStateException,
               TimeoutException):
            assert False, f"{pallete}色板，调用等温尺失败"

    
    @allure.story("temp_ruler")
    @allure.suite("caihong")
    @pytest.mark.caihong
    def test_temp_ruler_exist_pallete_switch_to_caihong(self, driver, wait):
        """
        测试等温尺已经被调用，色板切换为彩虹色板，等温尺是否还存在，预期存在
        :return:
        """
        # 进入插件
        device.enter_camera(wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        View.admit_access(wait)

        # 找到取景器元素
        view_ele = View.get_view_element(wait)

        # 点击展示色板栏
        View.call_palette_row(wait)

        # 向上滑动色板栏
        Pallete.swipe_pallete_row_up(driver, view_ele)

        # 选择彩虹色板
        pallete = "caihong"
        Pallete.choose_palette(wait, driver, view_ele, pallete)

        # 判断等温尺是否存在
        try:
            View.get_temp_ruler(wait)
        except(NoSuchElementException, StaleElementReferenceException, InvalidElementStateException, TimeoutException):
            assert False, f"{pallete}色板，等温尺不存在"

    
    @allure.story("temp_ruler")
    @allure.suite("caihong")
    @pytest.mark.caihong
    def test_caihong_cancel_call_temp_ruler(self, driver, wait):
        """
        测试彩虹色板能否取消调用等温尺，预期可以
        :return:
        """
        # 进入插件
        device.enter_camera(wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        View.admit_access(wait)

        # 找到取景器元素
        view_ele = View.get_view_element(wait)

        # 点击展示色板栏
        View.call_palette_row(wait)

        # 向上滑动色板栏
        Pallete.swipe_pallete_row_up(driver, view_ele)

        # 选择彩虹色板
        pallete = "caihong"
        Pallete.choose_palette(wait, driver, view_ele, pallete)

        # 点击取消调用等温尺
        View.call_temp_ruler(wait)

        # 判断等温尺是否取消调用成功
        try:
            View.get_temp_ruler(wait)
            assert False, f"{pallete}色板，取消调用等温尺失败"
        except(NoSuchElementException, StaleElementReferenceException, InvalidElementStateException,
               TimeoutException):
            pass

    
    @allure.story("temp_ruler")
    @allure.suite("caihong")
    @pytest.mark.caihong
    def test_caihong_call_temp_ruler(self, driver, wait):
        """
        测试彩虹色板能否调用等温尺，预期可以
        :return:
        """
        # 进入插件
        device.enter_camera(wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        View.admit_access(wait)

        # 找到取景器元素
        view_ele = View.get_view_element(wait)

        # 点击展示色板栏
        View.call_palette_row(wait)

        # 向上滑动色板栏
        Pallete.swipe_pallete_row_up(driver, view_ele)

        # 选择彩虹色板
        pallete = "caihong"
        Pallete.choose_palette(wait, driver, view_ele, pallete)

        # 点击取消调用等温尺
        View.call_temp_ruler(wait)

        # 点击调用等温尺
        View.call_temp_ruler(wait)

        # 判断等温尺是否调用成功
        try:
            View.get_temp_ruler(wait)
        except(NoSuchElementException, StaleElementReferenceException, InvalidElementStateException,
               TimeoutException):
            assert False, f"{pallete}色板，调用等温尺失败"

    
    @allure.story("temp_ruler")
    @allure.suite("heire")
    @pytest.mark.heire
    def test_temp_ruler_exist_pallete_switch_to_heire(self, driver, wait):
        """
        测试等温尺已经被调用，色板切换为黑热色板，等温尺是否还存在
        :return:
        """
        # 进入插件
        device.enter_camera(wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        View.admit_access(wait)

        # 找到取景器元素
        view_ele = View.get_view_element(wait)

        # 点击展示色板栏
        View.call_palette_row(wait)

        # 向上滑动色板栏
        Pallete.swipe_pallete_row_up(driver, view_ele)

        # 选择黑热色板
        pallete = "heire"
        Pallete.choose_palette(wait, driver, view_ele, pallete)

        # 判断等温尺是否存在
        try:
            View.get_temp_ruler(wait)
            assert False, f"{pallete}色板，等温尺依旧存在"
        except(NoSuchElementException, StaleElementReferenceException, InvalidElementStateException,
               TimeoutException):
            pass

    
    @allure.story("temp_ruler")
    @allure.suite("heire")
    @pytest.mark.heire
    def test_heire_call_temp_ruler(self, driver, wait):
        """
        测试黑热色板能否调用等温尺，预期不能
        :return:
        """
        # 进入插件
        device.enter_camera(wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        View.admit_access(wait)

        # 找到取景器元素
        view_ele = View.get_view_element(wait)

        # 点击展示色板栏
        View.call_palette_row(wait)

        # 向上滑动色板栏
        Pallete.swipe_pallete_row_up(driver, view_ele)

        # 选择黑热色板
        pallete = "heire"
        Pallete.choose_palette(wait, driver, view_ele, pallete)

        # 点击调用等温尺
        View.call_temp_ruler(wait)

        # 判断等温尺是否调用成功
        try:
            View.get_temp_ruler(wait)
            assert False, f"{pallete}色板调用等温尺成功"
        except(NoSuchElementException, StaleElementReferenceException, InvalidElementStateException,
               TimeoutException):
            pass

    
    @allure.story("temp_ruler")
    @allure.suite("baire")
    @pytest.mark.baire
    def test_temp_ruler_exist_pallete_switch_to_baire(self, driver, wait):
        """
        测试等温尺已经被调用，色板切换为白热色板，等温尺是否还存在
        :return:
        """
        # 进入插件
        device.enter_camera(wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        View.admit_access(wait)

        # 找到取景器元素
        view_ele = View.get_view_element(wait)

        # 点击展示色板栏
        View.call_palette_row(wait)

        # 向上滑动色板栏
        Pallete.swipe_pallete_row_up(driver, view_ele)

        # 选择白热色板
        pallete = "baire"
        Pallete.choose_palette(wait, driver, view_ele, pallete)

        # 判断等温尺是否存在
        try:
            View.get_temp_ruler(wait)
            assert False, f"{pallete}色板，等温尺依旧存在"
        except(NoSuchElementException, StaleElementReferenceException, InvalidElementStateException,
               TimeoutException):
            pass

    
    @allure.story("temp_ruler")
    @allure.suite("baire")
    @pytest.mark.baire
    def test_baire_call_temp_ruler(self, driver, wait):
        """
        测试白热色板能否调用等温尺，预期不能
        :return:
        """
        # 进入插件
        device.enter_camera(wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        View.admit_access(wait)

        # 找到取景器元素
        view_ele = View.get_view_element(wait)

        # 点击展示色板栏
        View.call_palette_row(wait)

        # 向上滑动色板栏
        Pallete.swipe_pallete_row_up(driver, view_ele)

        # 选择白热色板
        pallete = "baire"
        Pallete.choose_palette(wait, driver, view_ele, pallete)

        # 点击调用等温尺
        View.call_temp_ruler(wait)

        # 判断等温尺是否调用成功
        try:
            View.get_temp_ruler(wait)
            assert False, f"{pallete}色板调用等温尺成功"
        except(NoSuchElementException, StaleElementReferenceException, InvalidElementStateException,
               TimeoutException):
            pass

    
    @allure.story("temp_ruler")
    @allure.suite("tiehong")
    @pytest.mark.tiehong
    def test_temp_ruler_exist_pallete_switch_to_tiehong(self, driver, wait):
        """
        测试等温尺已经被调用，色板切换为铁红色板，等温尺是否还存在，预期存在
        :return:
        """
        # 进入插件
        device.enter_camera(wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        View.admit_access(wait)

        # 找到取景器元素
        view_ele = View.get_view_element(wait)

        # 点击展示色板栏
        View.call_palette_row(wait)

        # 向上滑动色板栏
        Pallete.swipe_pallete_row_up(driver, view_ele)

        # 选择铁红色板
        pallete = "tiehong"
        Pallete.choose_palette(wait, driver, view_ele, pallete)

        # 判断等温尺是否存在
        try:
            View.get_temp_ruler(wait)
        except(NoSuchElementException, StaleElementReferenceException, InvalidElementStateException, TimeoutException):
            assert False, f"{pallete}色板，等温尺不存在"

    
    @allure.story("temp_ruler")
    @allure.suite("tiehong")
    @pytest.mark.tiehong
    def test_tiehong_cancel_call_temp_ruler(self, driver, wait):
        """
        测试铁红色板能否取消调用等温尺，预期可以
        :return:
        """
        # 进入插件
        device.enter_camera(wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        View.admit_access(wait)

        # 找到取景器元素
        view_ele = View.get_view_element(wait)

        # 点击展示色板栏
        View.call_palette_row(wait)

        # 向上滑动色板栏
        Pallete.swipe_pallete_row_up(driver, view_ele)

        # 选择铁红色板
        pallete = "tiehong"
        Pallete.choose_palette(wait, driver, view_ele, pallete)

        # 点击取消调用等温尺
        View.call_temp_ruler(wait)

        # 判断等温尺是否取消调用成功
        try:
            View.get_temp_ruler(wait)
            assert False, f"{pallete}色板，取消调用等温尺失败"
        except(NoSuchElementException, StaleElementReferenceException, InvalidElementStateException,
               TimeoutException):
            pass

    
    @allure.story("temp_ruler")
    @allure.suite("tiehong")
    @pytest.mark.tiehong
    def test_tiehong_call_temp_ruler(self, driver, wait):
        """
        测试铁红色板能否调用等温尺，预期可以
        :return:
        """
        # 进入插件
        device.enter_camera(wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        View.admit_access(wait)

        # 找到取景器元素
        view_ele = View.get_view_element(wait)

        # 点击展示色板栏
        View.call_palette_row(wait)

        # 向上滑动色板栏
        Pallete.swipe_pallete_row_up(driver, view_ele)

        # 选择铁红色板
        pallete = "tiehong"
        Pallete.choose_palette(wait, driver, view_ele, pallete)

        # 点击取消调用等温尺
        View.call_temp_ruler(wait)

        # 点击调用等温尺
        View.call_temp_ruler(wait)

        # 判断等温尺是否调用成功
        try:
            View.get_temp_ruler(wait)
        except(NoSuchElementException, StaleElementReferenceException, InvalidElementStateException,
               TimeoutException):
            assert False, f"{pallete}色板，调用等温尺失败"
    
class TestImageSetting:
    """
    测试图像设置功能
    """
    @allure.story("image_setting")
    def test_call_img_setting_row(self, driver, wait):
        """
        测试调出图像工具栏
        :return:
        """
        # 进入插件
        device.enter_camera(wait)

        # 如果弹框需要授权APP访问camera+，点击允许
        View.admit_access(wait)

        # 找到取景器元素
        View.get_view_element(wait)

        # 点击调用图像工具栏图标
        View.call_img_setting(wait)

        # 判断各图像工具是否展示
        try:
            ImageSetting.get_brightness_icon(wait)
            ImageSetting.get_contrast_icon(wait)
            ImageSetting.get_xuanzhuan_icon(wait)
            ImageSetting.get_jingxiang_icon(wait)
        except(NoSuchElementException, InvalidElementStateException, StaleElementReferenceException, TimeoutException):
            assert False, "调用图像工具栏失败"

    
    @allure.story("image_setting")
    def test_call_brightness_bar(self, driver, wait):
        """
        测试调出亮度栏
        :return:
        """
        # 进入插件
        device.enter_camera(wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        View.admit_access(wait)

        # 找到取景器元素
        View.get_view_element(wait)

        # 点击调用图像工具栏图标
        View.call_img_setting(wait)

        # 点击调用亮度栏
        ImageSetting.click_brightness_icon(wait)

        # 判断亮度栏是否调出
        try:
            ImageSetting.get_brightness_contrast_bar(wait)
        except(NoSuchElementException, StaleElementReferenceException, InvalidElementStateException, TimeoutException):
            assert False, "亮度栏调出失败"

    
    @allure.story("image_setting")
    def test_call_contrast_bar(self, driver, wait):
        """
        测试调出对比度栏
        :return:
        """
        # 进入插件
        device.enter_camera(wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        View.admit_access(wait)

        # 找到取景器元素
        View.get_view_element(wait)

        # 点击调用图像工具栏图标
        View.call_img_setting(wait)

        # 点击调用对比度栏
        ImageSetting.click_contrast_icon(wait)

        # 判断对比度栏是否调出
        try:
            ImageSetting.get_brightness_contrast_bar(wait)
        except(NoSuchElementException, StaleElementReferenceException, InvalidElementStateException, TimeoutException):
            assert False, "对比度栏调出失败"

class TestPallete:
    """
    测试色板功能
    """
    @allure.story("pallete")
    def test_call_palette_row(self, driver, wait):
        """
        测试调出色板栏
        :return:
        """
        # 进入插件
        device.enter_camera(wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        View.admit_access(wait)

        # 找到取景器元素
        view_ele = View.get_view_element(wait)

        # 展示色板栏
        View.call_palette_row(wait)

        # 向上滑动色板栏
        Pallete.swipe_pallete_row_up(driver, view_ele)

        # 判断色板栏是否展示成功
        for key,value in Pallete.PALLETE.items():
            Pallete.choose_palette(wait, driver, view_ele, key)