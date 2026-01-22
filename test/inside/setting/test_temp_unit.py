import allure, time, easyocr
from page.outside import device
from page.inside import view
from page.inside.setting import setting, temp_unit

class TestTempUnit:

    @allure.epic("inside")
    @allure.feature("setting")
    @allure.story("temp_unit")
    def test_choose_celsius(self):
        """
        测试选择单位为℃
        :return:
        """
        # 进入插件
        device.enter_camera(self.wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        view.admit_access(self.wait)

        # 等取景器加载完毕
        time.sleep(10)

        # 进入设置页面
        view.enter_setting(self.wait)

        # 进入温度单位页面

        setting.enter_temp_unit(self.wait)

        # 选择温度单位为℃
        temp_unit.choose_celsius(self.wait)


