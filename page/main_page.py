# -*- coding: utf-8 -*-
# @Author  : lidonghui
from page.base_page import BasePage
from page.contract_list_page import ContractListPage


class MainPage(BasePage):
    # 跳转至通讯录页面
    def goto_contract_list_page(self):
        # 模拟弹窗操作
        self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.wework:id/gl6"]').click()
        self.steps('../data/main_step.yaml')
        return ContractListPage(self.driver)