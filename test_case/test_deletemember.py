# -*- coding: utf-8 -*-
# @Author  : lidonghui
from time import sleep


from page.start import Start


class TestDeleteMember:
    def setup(self):
        self.start = Start()

    def test_deletemember(self):
        search_page = self.start.goto_main().goto_contract_list_page()
        # 获取删除成员前结果页同名成员列表
        searchlist1 = search_page.goto_search("laoli2")
        # 执行删除操作
        delete_page = search_page.goto_memberinfo().goto_setup_memberdetail_page().goto_modify_memberinfotmaion_page().delete_member()
        sleep(3)
        # 获取删除成员后结果页同名成员列表
        searchlist2 = delete_page.get_results()
        assert len(searchlist1)-len(searchlist2) == 1

