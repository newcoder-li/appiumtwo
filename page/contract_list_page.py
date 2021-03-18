# -*- coding: utf-8 -*-
# @Author  : lidonghui
from conftest import root_log
from page.base_page import BasePage
from page.member_detail_page import MemberDetailPage


class ContractListPage(BasePage):
    def goto_search(self, name):
        root_log.info(f"输入用户名{name}，获取删除前结果数量")
        self._params['name'] = name
        self.steps('../data/contract_list_step.yaml')
        # 获取查找列表元素
        self._elelist1 = self.finds('xpath', '//*[@text="联系人"]/../..//*[@resource-id="com.tencent.wework:id/avi"]')
        return self._elelist1


    def goto_memberinfo(self):
        root_log.info("点击第一个成员，进入联系人详情页")
        if len(self._elelist1) > 0:
            self._elelist1[0].click()
        return MemberDetailPage(self.driver)