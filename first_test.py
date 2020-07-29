#!/usr/bin/env python3
import unittest
import minium
import time
# from searchTest.search_test import SearchTest

class FirstTest(minium.MiniTest):
    # def test_get_system_info(self):
    #     sys_info = self.app.call_wx_method("getSystemInfo")
    #     self.assertIn("SDKVersion", sys_info.result.result)
    
    def test1_get_search_info(self):
        self.page.get_element("input[class='serinput']").click()
        time.sleep(1)
        path = self.page.path
        self.assertEqual(path,'/pages/searchpage/searchpage')

    def test2_banner_info(self):
        self.app.switch_tab("/pages/index/index")
        self.page.get_element("image[class='slide-image']").click()
        time.sleep(1)
        path = self.page.path
        self.assertEqual(path,'/shoppages/shopother/shopother')

# if __name__ == '__main__':
#     suite = unittest.TestSuite()
#     suite.addTest(FirstTest('test_get_search_info'))
#     suite.addTest(SearchTest)
#     runner = unittest.TextTestRunner()
#     runner.run(suite)