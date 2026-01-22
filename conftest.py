from appium.webdriver import Remote
from appium.options.common.base import AppiumOptions
from selenium.webdriver.support.ui import WebDriverWait
import pytest

@pytest.fixture(autouse=True)
def camera_plus_driver(request):
    """
    启动webdriver，设置元素加载前等待时间
    :return:
    """
    appium_server_url = 'http://localhost:4723'

    # 设置连接camera_plus参数
    camera_plus_capabilities = {
        "platformName": "Android",
        "appium:automationName": "uiautomator2",
        "appium:deviceName": "Android",
        "appium:appPackage": "com.inreii.neutralapp",
        "appium:appActivity": ".frame.SplashActivity",
        "appium:noReset": False, # 每次测试都自动重启软件
        "autoGrantPermissions": True,  # 自动授予系统权限
    }

    options: AppiumOptions = AppiumOptions()
    options.load_capabilities(camera_plus_capabilities)

    # 设置webdriver,打开camera_plus界面
    driver = Remote(command_executor=appium_server_url, options=options)
    request.cls.driver = driver
    request.cls.wait = WebDriverWait(driver=driver, timeout=10)

    yield

    driver.quit()
