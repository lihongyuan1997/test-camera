import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, InvalidElementStateException
import allure, pytest

import common_utils
import page.inside.albums
from page.inside import view, albums
from page.outside import startup, device, gallery


class TestPhoto:

    @allure.epic("inside")
    @allure.feature("photo")
    def test_generate_inside_report(self):
        """
        测试生成内部报告是否成功
        :return:
        """
        # 进入插件
        device.enter_camera(self.wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        view.judge_alert(self.wait)

        # 等取景器加载完毕
        time.sleep(10)

        # 拍摄照片
        view.take_photo(self.wait, 1)

        # 进入内部相册
        view.enter_albums(self.wait)

        # 进入报告页面
        page.inside.albums.enter_report(self.wait)

        print("----------------------------------------------------------------生成报告前-------------------------------------------------------------")

        # 获取所有报告标题
        all_report_titles_before: list[str] = albums.report.get_all_reports(self.wait, self.driver)
        print("生成报告前内部所有报告标题：", all_report_titles_before)

        # 进入相册页面
        page.inside.albums.enter_album(self.wait)

        # 找到第一张照片
        first_photo: WebElement = albums.album.find_latest_file(self.wait, self.driver)

        # 进入第一张照片
        first_photo.click()

        # 生成报告
        albums.photo.click_generate_report(self.wait)

        # 确认生成报告
        albums.photo.confirm_generate_report(self.wait)

        print("----------------------------------------------------------------生成报告后-------------------------------------------------------------")

        # 返回相册页面
        common_utils.back_last_page(self.wait)

        # 进入报告页面
        page.inside.albums.enter_report(self.wait)

        # 获取所有报告标题
        all_report_titles_after: list[str] = albums.report.get_all_reports(self.wait, self.driver)
        print("生成报告后内部所有报告标题：", all_report_titles_after)

        # 判断报告是否生成成功
        if all_report_titles_before is None:
            assert len(all_report_titles_after) == 1, "生成内部报告失败"
        else:
            assert len(all_report_titles_after) == len(all_report_titles_before) + 1, "生成内部报告失败"

    @allure.epic("inside")
    @allure.feature("photo")
    def test_generate_outside_report(self):
        """
        测试生成外部报告是否成功
        :return:
        """
        print("----------------------------------------------------------------生成报告前-------------------------------------------------------------")

        # 进入外壳报告页面
        startup.enter_gallery(self.wait)
        page.inside.albums.enter_report(self.wait)

        # 获取所有报告标题
        all_report_titles_before: list[str] = gallery.report.get_all_reports(self.wait, self.driver)
        print("生成报告前外部所有报告标题：", all_report_titles_before)

        # 进入设备页面
        startup.enter_device(self.wait)

        # 进入插件
        device.enter_camera(self.wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        view.judge_alert(self.wait)

        # 等取景器加载完毕
        time.sleep(10)

        # 拍摄照片
        view.take_photo(self.wait, 1)

        # 进入内部相册
        view.enter_albums(self.wait)

        # 进入相册页面
        page.inside.albums.enter_album(self.wait)

        # 找到第一张照片
        first_photo: WebElement = albums.album.find_latest_file(self.wait, self.driver)

        # 进入第一张照片
        first_photo.click()

        # 生成报告
        albums.photo.click_generate_report(self.wait)

        # 确认生成报告
        albums.photo.confirm_generate_report(self.wait)

        print("----------------------------------------------------------------生成报告后-------------------------------------------------------------")

        # 返回相册页面
        common_utils.back_last_page(self.wait)

        # 返回取景器页面
        common_utils.back_last_page(self.wait)

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
