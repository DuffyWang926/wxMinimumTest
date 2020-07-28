#!/usr/bin/env python3
import minium
import time

class FirstTest(minium.MiniTest):
    # def test_get_system_info(self):
    #     sys_info = self.app.call_wx_method("getSystemInfo")
    #     self.assertIn("SDKVersion", sys_info.result.result)
    
    def test_get_search_info(self):
        self.page.get_element("input[class='serinput']").click()
        time.sleep(1)
        path = self.page.path
        self.assertEqual(path,'/pages/searchpage/searchpage')
        print(path,'path')
        
        