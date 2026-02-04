class DeviceContext:
    """
    获取设备属性，如屏幕尺寸
    """
    @classmethod
    def init(cls, driver):
        """
        初始化类属性
        :param driver:
        :return:
        """
        cls.WIDTH = driver.get_window_size()['width']
        cls.HEIGHT = driver.get_window_size()['height']