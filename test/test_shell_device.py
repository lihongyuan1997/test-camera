import pytest
import allure
from appium.webdriver import WebElement
from selenium.common import NoSuchElementException, InvalidElementStateException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from page import shell_device, inside_view, common_utils

class TestShellDevice:

    @allure.epic("shell")
    @allure.feature("device")
    def test_enter_camera(self):
        """
        测试从外壳进入插件
        :return:
        """
        # 点击进入插件
        shell_device.enter_camera(self.wait)

        # 确认是否进入插件成功
        inside_view.find_view_element(self.wait)