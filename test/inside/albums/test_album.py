import time

import pytest

from page.inside import albums
from page.inside.albums import album
from page.inside.view import View
from page.outside import startup, device

from selenium.common import *

class TestAlbum:
    @pytest.mark.inside
    @pytest.mark.album
    def test_exist_photo_edit_photos(self, driver, wait):
        """
        测试存在照片时，点击右上角编辑按钮后，预期显示选中图片按钮
        :param driver:
        :param wait:
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

        # 点击右上角编辑按钮
        album.edit_photos(wait)

        # 判断是否显示多选照片按钮
        try:
            album.get_day_check_button(wait)
        except (TimeoutException, NoSuchElementException, StaleElementReferenceException, InvalidElementStateException):
            assert False,'右上角编辑照片功能失效'

    @pytest.mark.inside
    @pytest.mark.album
    def test_no_photo_edit_photos(self, driver, wait):
        """
        测试不存在照片时，点击右上角编辑按钮后，预期没有反应
        :param driver:
        :param wait:
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

        # 进入内部相册
        View.enter_albums(wait)

        # 进入相册页面
        albums.enter_album(wait)

        # 点击右上角编辑按钮
        album.edit_photos(wait)

        # 判断是否显示多选照片按钮
        try:
            album.get_day_check_button(wait)
            assert False, '没有照片时不应该出现多选按钮'
        except (TimeoutException, NoSuchElementException, StaleElementReferenceException, InvalidElementStateException):
            pass

    @pytest.mark.inside
    @pytest.mark.album
    @pytest.mark.parametrize(argnames='number', argvalues=[5])
    def test_delete_photo(self,driver,wait,number):
        """
        测试删除照片/视频
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
        View.take_photo(wait, number)

        # 进入内部相册
        View.enter_albums(wait)

        # 进入相册页面
        albums.enter_album(wait)

        # 点击右上角编辑按钮
        album.edit_photos(wait)


class TestCollectPhoto:
    @pytest.mark.inside
    @pytest.mark.album
    @pytest.mark.collect
    @pytest.mark.parametrize(argnames = 'number', argvalues=[10])
    def test_collect_photo(self, driver, wait, number):
        """
        测试照片收藏是否成功
        :param number:
        :return:
        """