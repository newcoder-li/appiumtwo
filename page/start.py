# -*- coding: utf-8 -*-
# @Author  : lidonghui
from appium import webdriver

from page.main_page import MainPage


class Start:
    def __init__(self):
        desired_caps = {
            'platformName': 'Android',
            'appPackage': 'com.tencent.wework',
            'appActivity': '.launch.WwMainActivity',
            # 不清空缓存启动app
            'noReset': 'true'
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        # 隐式等待3s
        self.driver.implicitly_wait(3)

    def goto_main(self):
        return MainPage(self.driver)