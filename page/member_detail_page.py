# -*- coding: utf-8 -*-
# @Author  : lidonghui
from page.base_page import BasePage
from page.edit_memberdetail_page import EditMemberdetailPage


class MemberDetailPage(BasePage):
    def goto_setup_memberdetail_page(self):
        self.steps("../data/setup_memberdetail_step.yaml")
        return EditMemberdetailPage(self.driver)