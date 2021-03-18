# -*- coding: utf-8 -*-
# @Author  : lidonghui
import yaml
import allure
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from conftest import root_log


class BasePage:
    def __init__(self, driver: WebDriver):
        # 参数替换
        self._params = {}
        # 删除前的元素列表
        _elelist1 = []
        # 删除后的元素列表
        _elelist2 = []
        # 定义初始错误次数
        self._error_num = 0
        # 定义最大失败次数
        self._max_num = 3
        self.driver = driver
        # 定义黑名单
        self.black_list = [('xpath', '//*[@resource-id="com.tencent.wework:id/gu_"]')]

    def find(self, by, locator=None):
        try:
            root_log.info(f'find: by={by}, locator={locator}')
            elem = self.driver.find_element(by, locator)
            self._error_num = 0
            return elem
        except Exception as e:
            root_log.info("未找到元素")
            # 未找到元素时截图
            self.driver.get_screenshot_as_file('../test_case/result/tmp.png')
            allure.attach.file('../testcase/result/tmp.png', attachment_type=allure.attachment_type.PNG)
            # 判断失败次数是否大于最大错误次数
            if self._error_num > self._max_num:
                self._error_num = 0
                # 大于直接抛出异常
                raise e
            # 小于继续循环
            self._error_num += 1
            # 黑名单处理
            for black in self.black_list:
                eles = self.finds(*black)
                if len(eles) > 0:
                    eles[0].click()
                    return self.find(by, locator)
            raise e

    def finds(self, by, locator=None):
        return self.driver.find_elements(by, locator)

    def find_click(self, by, locator=None):
        return self.driver.find_element(by, locator).click()

    def steps(self, path):
        with open(path, encoding="UTF-8") as f:
            steps: list[dict] = yaml.safe_load(f)
            for step in steps:
                if "by" in step.keys():
                    element = self.find(step["by"], step["locator"])
                if "action" in step.keys():
                    if "click" == step["action"]:
                        element.click()
                    if "send" == step["action"]:
                        content: str = step["value"]
                        for param in self._params:
                            content = content.replace("{%s}" % param, self._params[param])
                        element.send_keys(content)

    def swip_click(self, text):
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 f'text("{text}").instance(0));').click()
