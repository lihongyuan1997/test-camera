import allure
import time
from page.outside import device
from page.inside import view, setting


class TestSetting:
    @allure.epic("inside")
    @allure.feature("setting")
    def test_auto_shutter(self):
        """
        测试开关自动快门
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

        # 获取自动快门开关状态
        auto_shutter_status_before: bool = setting.get_auto_shutter_status(self.wait)

        # 点击自动快门开关
        setting.click_auto_shutter(self.wait)

        # 获取点击之后的自动快门开关状态
        auto_shutter_status_after: bool = setting.get_auto_shutter_status(self.wait)

        # 比较点击前后的自动快门开关状态
        assert auto_shutter_status_before != auto_shutter_status_after, "自动快门开关状态改变失败"

    @allure.epic("inside")
    @allure.feature("setting")
    def test_time_watermark(self):
        """
        测试开关时间水印
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

        # 获取时间水印开关状态
        time_watermark_status_before: bool = setting.get_time_watermark_status(self.wait)

        # 点击时间水印开关
        setting.click_time_watermark(self.wait)

        # 获取点击之后的时间水印开关状态
        time_watermark_status_after: bool = setting.get_time_watermark_status(self.wait)

        # 比较点击前后的时间水印开关状态
        assert time_watermark_status_before != time_watermark_status_after, "时间水印开关状态改变失败"

    @allure.epic("inside")
    @allure.feature("setting")
    def test_microphone(self):
        """
        测试开关麦克风
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

        # 获取麦克风开关状态
        microphone_status_before: bool = setting.get_microphone_status(self.wait)

        # 点击麦克风开关
        setting.click_microphone(self.wait)

        # 获取点击之后的麦克风开关状态
        microphone_status_after: bool = setting.get_microphone_status(self.wait)

        # 比较点击前后的麦克风开关状态
        assert microphone_status_before != microphone_status_after, "麦克风开关状态改变失败"