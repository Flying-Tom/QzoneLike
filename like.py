import time
import os
import logging
from shutil import which
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import undetected_chromedriver as uc


def init_logger():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
    os.makedirs("log", exist_ok=True)
    logging.info("Start logging")


def install_chrome():
    if which("google-chrome") is None:
        logging.info("Install chrome")
        os.system(
            "wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb")
        os.system("sudo apt install ./google-chrome-stable_current_amd64.deb -y")
    else:
        logging.info("Chrome already installed")


def init_driver():
    options = uc.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-setuid-sandbox")
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('blink-settings=imagesEnabled=false')
    options.set_capability("detach", True)
    driver = uc.Chrome(options=options, version_main=98)
    return driver


def terminate_chrome():
    try:
        val = os.system(
            "kill -9 $(ps aux | grep [c]hrome | tr -s ' '| cut -d ' ' -f 2)")
        if val >> 8 == 2:
            raise Exception("No running chrome instance now")
    except Exception as e:
        logging.info(str(e))


def login_qzone(driver):

    driver.get("https://qzone.qq.com/")
    driver.switch_to.frame("login_frame")
    driver.get_screenshot_as_file(r"log/screenshot.png")
    try:
        logging.info("等待扫描二维码")
        element = WebDriverWait(driver, timeout=120).until(EC.presence_of_element_located((By.ID, "tab_menu_friend")))
        driver.find_element(by=By.ID, value="tab_menu_friend").click()
    except TimeoutException:
        logging.info("登录超时")
    logging.info("登录成功")
    time.sleep(3)


def exec_script(driver):
    logging.info("执行脚本")
    with open("script/like.js", "r") as f:
        lines = f.readlines()
        code = "".join(lines)
        driver.execute_script(code)
        f.close()

    while True:
        driver.get_screenshot_as_file(r"log/screenshot.png")
        time.sleep(600)


init_logger()
install_chrome()
terminate_chrome()

driver = init_driver()
login_qzone(driver)
exec_script(driver)
