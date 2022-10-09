import json
import logging
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


env_dist = os.environ
config = env_dist.get("config")
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

url = r'https://yqtb.nwpu.edu.cn/wx/ry/jrsb.jsp'
#driver_path = ChromeDriverManager().install()  #暂时不生效作保留
chrome_options = Options()
chrome_options.add_argument('--headless')  #窗口不显示
#service = Service((ChromeDriverManager().install()))
#service = Service("C:\Program Files\Google\Chrome\Application\chromedriver.exe");


def run(username: str, password: str):
    #driver = webdriver.Chrome(service, options=chrome_options)
    driver = webdriver.Chrome('/usr/bin/chromedriver')
    driver.get(url)
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="vue_main"]/div[2]/div[3]/div/div[2]/div[3]/div/div/div[1]/ul/li[3]').click()
    time.sleep(1)
    username_element = driver.find_element(By.ID, 'username')
    username_element.send_keys(username)
    password_element = driver.find_element(By.ID, 'password')
    password_element.send_keys(password)
    time.sleep(1)
    driver.find_element(By.NAME, 'button').click()
    time.sleep(5)
    #driver.switch_to.window(driver.window_handles[-1])  # ? 窗口切换

    js = 'go_sub();document.querySelector("label.weui-cell.weui-cell_active.weui-check__label").click();savefx()'
    driver.execute_script(js)
    '''
    driver.find_element(By.XPATH, '//*[@id="rbxx_div"]/div[17]').click()  #同下
    #driver.find_element(By.XPATH, '//*[@id="rbxx_div"]/div[27]').click()# 点击提交填报信息
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="qrxx_div"]/div[2]/div[11]').click()  #点击已核实以上数据
    #driver.find_element(By.XPATH, '//*[@id="qrxx_div"]/div[2]/div[26]').click()  # 点击已核实以上数据
    driver.find_element(By.XPATH, '//*[@id="save_div"]').click()  # 点击确认提交
    #driver.find_element(By.XPATH, '//*[@id="save_div"]').click()  # 点击确认提交
    '''
    time.sleep(2)
    driver.close()
    logger.info(f'{username} 已完成填报')


def yqtb(students: list):
    print(students)
    logger.info('开始执行填报...')
    for username, password in students:
        run(username, password)
    logger.info('填报执行完毕')


if __name__ == '__main__':
    students = json.loads(config)
    logger.info(f'加载的用户列表: {[username for username, _ in students]}')
    yqtb(students)
