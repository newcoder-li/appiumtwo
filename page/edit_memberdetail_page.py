# -*- coding: utf-8 -*-
# @Author  : lidonghui
from page.base_page import BasePage
from page.modify_memberdetail_page import ModifyMemberdetailPage


class EditMemberdetailPage(BasePage):
    def goto_modify_memberinfotmaion_page(self):
        self.steps("../data/memberdetail_step.yaml")
        return ModifyMemberdetailPage(self.driver)