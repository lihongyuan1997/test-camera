import allure, time, random
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
        view.admit_access(self.wait)

        # 等取景器加载完毕
        view.get_view_element(self.wait)

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
        view.admit_access(self.wait)

        # 等取景器加载完毕
        view.get_view_element(self.wait)

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
        view.admit_access(self.wait)

        # 等取景器加载完毕
        view.get_view_element(self.wait)

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

    @allure.epic("inside")
    @allure.feature("setting")
    @allure.story("temp_alarm")
    def test_input_high_temp_success(self):
        """
        测试输入高温阈值，输入值大于低温阈值，输入成功
        :return:
        """
        # 进入插件
        device.enter_camera(self.wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        view.admit_access(self.wait)

        # 等取景器加载完毕
        view.get_view_element(self.wait)

        # 进入设置页面
        view.enter_setting(self.wait)

        # 进入温度告警页面
        setting.enter_temp_alarm(self.wait)

        # 获取低温阈值
        low_temp_str: str = temp_alarm.get_low_temp(self.wait)

        if low_temp_str.endswith('C') or low_temp_str.endswith('F'):
            low_temp_float: float = float(low_temp_str[:-2])

        if low_temp_str.endswith('K'):
            low_temp_float: float = float(low_temp_str[:-1])

        print("获取到低温阈值: -> ", low_temp_str)

        # 随机生成高温阈值，值高于低温阈值
        high_temp_float: float = round(random.uniform(low_temp_float,450), 1)
        print("随机生成高温阈值: -> ", high_temp_float)

        # 输入高温阈值
        temp_alarm.input_high_temp(self.wait, high_temp_float)

        # 获取输入后的高温阈值
        high_temp_confirm_str: str = temp_alarm.get_high_temp(self.wait)
        print("输入后的高温阈值: -> ", high_temp_confirm_str)

        # 判断高温阈值是否输入成功
        if not (high_temp_confirm_str[:-2] == str(high_temp_float) or high_temp_confirm_str[:-1] == str(high_temp_float)):
            assert False, "高温阈值输入失败"

    @allure.epic("inside")
    @allure.feature("setting")
    @allure.story("temp_alarm")
    def test_input_high_temp_failure(self):
        """
        测试输入高温阈值，输入值小于低温阈值，输入失败
        :return:
        """
        # 进入插件
        device.enter_camera(self.wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        view.admit_access(self.wait)

        # 等取景器加载完毕
        view.get_view_element(self.wait)

        # 进入设置页面
        view.enter_setting(self.wait)

        # 进入温度告警页面
        setting.enter_temp_alarm(self.wait)

        # 获取输入前高温阈值
        high_temp_before_str: str = temp_alarm.get_high_temp(self.wait)
        print("输入前高温阈值: -> ", high_temp_before_str)

        # 获取低温阈值
        low_temp_str: str = temp_alarm.get_low_temp(self.wait)

        if low_temp_str.endswith('C') or low_temp_str.endswith('F'):
            low_temp_float: float = float(low_temp_str[:-2])

        if low_temp_str.endswith('K'):
            low_temp_float: float = float(low_temp_str[:-1])

        print("获取到低温阈值: -> ", low_temp_str)

        # 随机生成高温阈值，值低于低温阈值
        high_temp_float: float = round(random.uniform(-20, low_temp_float), 1)
        print("随机生成高温阈值: -> ", high_temp_float)

        # 输入高温阈值
        temp_alarm.input_high_temp(self.wait, high_temp_float)

        # 获取输入后的高温阈值
        high_temp_confirm_str: str = temp_alarm.get_high_temp(self.wait)
        print("输入后的高温阈值: -> ", high_temp_confirm_str)

        # 判断高温阈值是否输入成功
        if not high_temp_before_str == high_temp_confirm_str:
            assert False, "高温阈值不应该输入成功"

    @allure.epic("inside")
    @allure.feature("setting")
    @allure.story("temp_alarm")
    def test_input_low_temp_success(self):
        """
        测试输入低温阈值，输入值小于高温阈值，输入成功
        :return:
        """
        # 进入插件
        device.enter_camera(self.wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        view.admit_access(self.wait)

        # 等取景器加载完毕
        view.get_view_element(self.wait)

        # 进入设置页面
        view.enter_setting(self.wait)

        # 进入温度告警页面
        setting.enter_temp_alarm(self.wait)

        # 获取高温阈值
        high_temp_str: str = temp_alarm.get_high_temp(self.wait)

        if high_temp_str.endswith('C') or high_temp_str.endswith('F'):
            high_temp_float: float = float(high_temp_str[:-2])

        if high_temp_str.endswith('K'):
            high_temp_float: float = float(high_temp_str[:-1])

        print("获取到高温阈值: -> ", high_temp_str)

        # 随机生成低温阈值，值低于高温阈值
        low_temp_float: float = round(random.uniform(-20, high_temp_float), 1)
        print("随机生成低温阈值: -> ", low_temp_float)

        # 输入低温阈值
        temp_alarm.input_low_temp(self.wait, low_temp_float)

        # 获取输入后的低温阈值
        low_temp_confirm_str: str = temp_alarm.get_low_temp(self.wait)
        print("输入后的低温阈值: -> ", low_temp_confirm_str)

        # 判断低温阈值是否输入成功
        if not (low_temp_confirm_str[:-2] == str(low_temp_float) \
                or low_temp_confirm_str[:-1] == str(low_temp_float)):
            assert False, "低温阈值输入失败"

    @allure.epic("inside")
    @allure.feature("setting")
    @allure.story("temp_alarm")
    def test_input_low_temp_failure(self):
        """
        测试输入低温阈值，输入值高于高温阈值，输入失败
        :return:
        """
        # 进入插件
        device.enter_camera(self.wait)

        # 如果弹框提示授权APP访问camera+，点击允许
        view.admit_access(self.wait)

        # 等取景器加载完毕
        view.get_view_element(self.wait)

        # 进入设置页面
        view.enter_setting(self.wait)

        # 进入温度告警页面
        setting.enter_temp_alarm(self.wait)

        # 获取输入前低温阈值
        low_temp_before_str: str = temp_alarm.get_low_temp(self.wait)
        print("输入前低温阈值: -> ", low_temp_before_str)

        # 获取高温阈值
        high_temp_str: str = temp_alarm.get_high_temp(self.wait)

        if high_temp_str.endswith('C') or high_temp_str.endswith('F'):
            high_temp_float: float = float(high_temp_str[:-2])

        if high_temp_str.endswith('K'):
            high_temp_float: float = float(high_temp_str[:-1])

        print("获取到高温阈值: -> ", high_temp_str)

        # 随机生成低温阈值，温度高于高温阈值
        low_temp_float: float = round(random.uniform(high_temp_float, 450), 1)
        print("随机生成低温阈值: -> ", low_temp_float)

        # 输入低温阈值
        temp_alarm.input_low_temp(self.wait, low_temp_float)

        # 获取输入后的低温阈值
        low_temp_confirm_str: str = temp_alarm.get_low_temp(self.wait)
        print("输入后的低温阈值: -> ", low_temp_confirm_str)

        # 判断低温阈值是否输入成功
        if not low_temp_before_str == low_temp_confirm_str:
            assert False, "低温阈值不应该输入成功"