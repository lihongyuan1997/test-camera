import allure
from page.inside import view
from page import device


class TestDevice:

    @allure.epic("shell")
    @allure.feature("device")
    def test_enter_camera(self):
        """
        测试从外壳进入插件
        :return:
        """
        # 点击进入插件
        device.enter_camera(self.wait)

        # 确认是否进入插件成功
        view.find_view_element(self.wait)