#!/usr/bin/env python3
import minium
import time

class SearchTest(minium.MiniTest):
        
    def test_search_page_info(self):
        self.app.navigate_to("/pages/searchpage/searchpage")
        time.sleep(1)
        self.page.data = {'save_data':'面膜'}
        topNode = self.page.get_element("view[class='sousuo']")
        topNode.click()
        time.sleep(1)
        path = self.page.path
        self.assertEqual(path,'/shoppages/shop/shop')
        print(path,'path')