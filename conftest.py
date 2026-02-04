from appium.webdriver import Remote
from appium.options.common.base import AppiumOptions
from selenium.webdriver.support.ui import WebDriverWait
import pytest
from device_context import DeviceContext
from devices import DEVICES
# 使用request.cls将driver, wait动态注入类属性
# @pytest.fixture(scope='session', autouse=True)
# def create_driver(request):
#     """
#     创建webdriver，设置元素加载前等待时间
#     :return:
#     """
#     appium_server_url = 'http://localhost:4723'
#
#     # 设置连接camera_plus参数
#     camera_plus_capabilities = {
#         "platformName": "Android",
#         "appium:automationName": "uiautomator2",
#         "appium:deviceName": "Android",
#         "appium:appPackage": "com.inreii.neutralapp",
#         "appium:appActivity": ".frame.SplashActivity",
#         "appium:noReset": False, # 每次测试都自动重启软件
#         "autoGrantPermissions": True,  # 自动授予系统权限
#     }
#
#     options: AppiumOptions = AppiumOptions()
#     options.load_capabilities(camera_plus_capabilities)
#
#     # 获取webdriver
#     driver = Remote(command_executor=appium_server_url, options=options)
#     request.cls.driver = driver
#     request.cls.wait = WebDriverWait(driver=driver, timeout=10)
#
#     # 将屏幕尺寸赋给全局类属性
#     DeviceContext.init(driver)
#
#     yield
#
#     driver.quit()

@pytest.fixture(scope='session', params=DEVICES)
def driver(request):
    """
    创建webdriver
    :return:
    """
    device = request.param

    appium_server_url = f'http://localhost:{device['appium_port']}'

    # 设置连接camera_plus参数
    camera_plus_capabilities = {
        "platformName": "Android",
        "udid": device['udid'],
        "systemPort": device['system_port'],
        "automationName": "uiautomator2",
        "deviceName": "Android",
        "appPackage": "com.inreii.neutralapp",
        "appActivity": ".frame.SplashActivity",
        "noReset": False, # 每次测试都自动重启软件
        "autoGrantPermissions": True,  # 自动授予系统权限
    }

    options: AppiumOptions = AppiumOptions()
    options.load_capabilities(camera_plus_capabilities)

    # 获取webdriver
    driver = Remote(command_executor=appium_server_url, options=options)

    yield driver

    driver.quit()

@pytest.fixture(scope='session')
def wait(driver):
    """
    创建WebDriverWait，设置找到元素前等待时间
    :param driver:
    :return:
    """
    return WebDriverWait(driver=driver, timeout=10)

@pytest.fixture(scope='session', autouse=True)
def init_device(driver):
    """
    将屏幕尺寸赋给全局类属性
    :param driver:
    :return:
    """
    DeviceContext.init(driver)