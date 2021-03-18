# -*- coding: utf-8 -*-
# @Author  : lidonghui
from page.base_page import BasePage


class ModifyMemberdetailPage(BasePage):
    # 删除联系人操作
    def delete_member(self):
        self.steps("../data/delete_member_step.yaml")
        return self

    def get_results(self):
        # root_log.info("获取删除后的结果数量")
        self._elelist2 = self.finds('xpath', '//*[@text="联系人"]/../..//*[@resource-id="com.tencent.wework:id/avi"]')
        return self._elelist2
