import time
from selenium.webdriver.remote.webelement import WebElement
import allure
import utility
from page.inside import view, albums
from page.outside import startup, device, gallery

class TestOutsidePhoto:

    @allure.epic("outside")
    @allure.feature("photo")
    def test_outside_photo_generate_report_inside_check(self):
        """
        测试外部照片生成报告后，内部是否存在报告
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

        print("----------------------------------------------------------------生成报告前-------------------------------------------------------------")

        # 进入内部相册
        view.enter_albums(self.wait)

        # 进入报告页面
        albums.enter_report(self.wait)

        # 生成报告前---获取内部所有报告标题
        all_report_titles_before: list[str] = albums.report.get_all_reports(self.wait, self.driver)
        print("生成报告前内部所有报告标题：", all_report_titles_before)

        # 回到取景器
        utility.back_last_page(self.wait)

        # 回到外壳
        view.back_shell(self.wait)

        print("----------------------------------------------------------------生成报告-------------------------------------------------------------")

        # 进入外壳相册
        startup.enter_gallery(self.wait)
        gallery.enter_album(self.wait)

        # 找到第一张照片
        first_photo: WebElement = gallery.album.find_latest_file(self.wait, self.driver)

        # 进入第一张照片
        first_photo.click()

        # 生成报告
        gallery.photo.click_generate_report(self.wait)

        # 确认生成报告
        gallery.photo.confirm_generate_report(self.wait)

        print("----------------------------------------------------------------生成报告后-------------------------------------------------------------")

        # 返回相册页面
        utility.back_last_page(self.wait)

        # 返回设备页面
        startup.enter_device(self.wait)

        # 进入插件
        device.enter_camera(self.wait)

        # 进入内部相册
        view.enter_albums(self.wait)

        # 进入报告页面
        albums.enter_report(self.wait)

        # 生成报告后---获取内部所有报告标题
        all_report_titles_after: list[str] = gallery.report.get_all_reports(self.wait, self.driver)
        print("生成报告后内部所有报告标题：", all_report_titles_after)

        # 判断报告是否生成成功
        if all_report_titles_before is None:
            assert len(all_report_titles_after) == 1, "生成内部报告失败"
        else:
            assert len(all_report_titles_after) == len(all_report_titles_before) + 1, "生成内部报告失败"

    @allure.epic("outside")
    @allure.feature("photo")
    def test_outside_photo_generate_report_outside_check(self):
        """
        测试外部照片生成报告后，外部是否存在报告
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

        # 返回外壳
        view.back_shell(self.wait)

        # 进入外壳报告页面
        startup.enter_gallery(self.wait)
        gallery.enter_report(self.wait)

        # 生成报告前---获取外部所有报告标题
        all_report_titles_before: list[str] = gallery.report.get_all_reports(self.wait, self.driver)
        print("生成报告前外部所有报告标题：", all_report_titles_before)

        # 进入外壳相册页面
        gallery.enter_album(self.wait)

        # 找到第一张照片
        first_photo: WebElement = gallery.album.find_latest_file(self.wait, self.driver)

        # 进入第一张照片
        first_photo.click()

        # 生成报告
        gallery.photo.click_generate_report(self.wait)

        # 确认生成报告
        gallery.photo.confirm_generate_report(self.wait)

        # 返回外壳相册页面
        utility.back_last_page(self.wait)

        # 进入报告页面
        gallery.enter_report(self.wait)

        # 生成报告后---再次获取外部所有报告标题
        all_report_titles_after: list[str] = gallery.report.get_all_reports(self.wait, self.driver)
        print("生成报告后外部所有报告标题：", all_report_titles_after)

        # 判断报告是否生成成功
        if all_report_titles_before is None:
            assert len(all_report_titles_after) == 1, "生成外部报告失败"
        else:
            assert len(all_report_titles_after) == len(all_report_titles_before) + 1, "生成外部报告失败"
