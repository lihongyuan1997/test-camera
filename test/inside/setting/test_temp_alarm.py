import allure, time
from page.outside import device
from page.inside import view
from page.inside.setting import setting, temp_alarm

class TestTempAlarm:

    @allure.epic("inside")
    @allure.feature("setting")
    @allure.story("temp_alarm")
    def test_click_high_temp_alarm(self):
        """
        测试点击高温报警开关
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

        # 进入温度告警页面
        setting.enter_temp_alarm(self.wait)

        # 获取高温告警开关状态
        high_temp_alarm_status_before: bool = temp_alarm.get_high_temp_alarm_status(self.wait)

        # 点击高温报警开关
        temp_alarm.click_high_temp_alarm(self.wait)

        # 再次获取高温告警开关状态
        high_temp_alarm_status_after: bool = temp_alarm.get_high_temp_alarm_status(self.wait)

        # 判断开关状态是否改变
        assert high_temp_alarm_status_before != high_temp_alarm_status_after, "高温报警开关状态改变失败"

    @allure.epic("inside")
    @allure.feature("setting")
    @allure.story("temp_alarm")
    def test_click_low_temp_alarm(self):
        """
        测试点击低温报警开关
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

        # 进入温度告警页面
        setting.enter_temp_alarm(self.wait)

        # 获取低温告警开关状态
        low_temp_alarm_status_before: bool = temp_alarm.get_low_temp_alarm_status(self.wait)

        # 点击低温报警开关
        temp_alarm.click_low_temp_alarm(self.wait)

        # 再次获取低温告警开关状态
        low_temp_alarm_status_after: bool = temp_alarm.get_low_temp_alarm_status(self.wait)

        # 判断开关状态是否改变
        assert low_temp_alarm_status_before != low_temp_alarm_status_after, "低温报警开关状态改变失败"

    @allure.epic("inside")
    @allure.feature("setting")
    @allure.story("temp_alarm")
    def test_click_alarm_sound(self):
        """
        测试点击报警声音开关
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

        # 进入温度告警页面
        setting.enter_temp_alarm(self.wait)

        # 获取报警声音开关状态
        alarm_sound_status_before: bool = temp_alarm.get_alarm_sound_status(self.wait)

        # 点击报警声音开关
        temp_alarm.click_alarm_sound(self.wait)

        # 再次获取报警声音开关状态
        alarm_sound_status_after: bool = temp_alarm.get_alarm_sound_status(self.wait)

        # 判断报警声音开关状态是否改变
        assert alarm_sound_status_before != alarm_sound_status_after, "报警声音开关状态改变失败"