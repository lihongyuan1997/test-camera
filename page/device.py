from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, InvalidElementStateException

def enter_camera(wait) -> None:
    """
    进入插件
    :return:
    """
    camera: WebElement = wait.until \
        (method=EC.presence_of_element_located \
            (locator=(By.XPATH, "//androidx.recyclerview.widget.RecyclerView[@resource-id='com.inreii.neutralapp:id/devList']/android.widget.RelativeLayout")))
    camera.click()