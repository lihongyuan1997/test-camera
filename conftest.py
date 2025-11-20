from appium.webdriver import Remote
from appium.options.common.base import AppiumOptions
from selenium.webdriver.support.ui import WebDriverWait
import pytest

@pytest.fixture(autouse=True)
def nocpix_driver(request):
    """
    启动webdriver，设置元素加载前等待时间
    :return:
    """
    appium_server_url = 'http://localhost:4723'

    # 设置连接NOCPIX参数
    nocpix_capabilities = {
        "platformName": "Android",
        "appium:automationName": "uiautomator2",
        "appium:deviceName": "Android",
        "appium:appPackage": "com.inreii.neutralapp",
        "appium:appActivity": ".frame.SplashActivity",
        "appium:noReset": False, # 每次测试都自动重启软件
        "autoGrantPermissions": True,  # 自动授予系统权限
    }

    options: AppiumOptions = AppiumOptions()
    options.load_capabilities(nocpix_capabilities)

    # 设置webdriver,打开nocpix界面
    driver: Remote = Remote(command_executor=appium_server_url, options=options)
    wait: WebDriverWait = WebDriverWait(driver=driver, timeout=10)

    request.cls.driver , request.cls.wait = driver , wait

    yield

    driver.quit()
