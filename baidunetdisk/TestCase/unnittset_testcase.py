#!/usr/bin/python3
# coding=utf-8

###################
# Author: Jianguo Yang
# Date: 2022-05-29
# Platform: Kylin Desktop V10 SP1
# Description: 测试12条测试用例并输出报告
# Warning: 如果OCR服务崩溃，过往的测量数据只能用于特定的场景
# 分辨率：1920*1080, 字体设置为默认的11号
# Version: 1.0
###################

from unittestreport import TestRunner
import unittest
import os
import sys
import requests
import base64
import json
import pprint
import cv2

os.environ['DISPLAY'] = ':0'  # 设置此参数以使得在远程连接情况下运行该文件而不报错
testcasedir = os.path.dirname(__file__)
kylinautoguidir = f"{testcasedir}/../../kylinautogui"
sys.path.append(kylinautoguidir)

import libs.untils.functions as fn  # NOQA: E402
import libs.untils.paddleocr as ocr # NOQA: E402
import libs.untils.composite as com # NOQA: E402

# 百度网盘登录功能
class Test_Login(unittest.TestCase):

    def setUp(self):
        os.system('python -u test_login.py')
    
    def test_string_exist(self):
        """
        百度网盘登录功能
        """
        print('正在进行识别结果检测，正在逐个检查“待识别项”')
        scanner_set = {'会员中心'}
        for i in scanner_set:
            self.assertTrue(com.screenshot_window_and_ocr(i,fuzzy=True))
        else:
            print('检测完成, 所有的待检测字符均出现')


# 百度网盘创建新文件夹功能
class Test_Create(unittest.TestCase):

    def setUp(self):
        os.system('python -u test_create.py')
        
    def test_string_exist(self):
        """
        百度网盘创建新文件夹
        """
        print('正在进行识别结果检测，正在逐个检查“待识别项”')
        scanner_set = {'mytest'}
        for i in scanner_set:
            self.assertTrue(com.screenshot_window_and_ocr(i,fuzzy=True))
        else:
            print('检测完成, 所有的待检测字符均出现')


# 百度网盘删除文件功能
class Test_Delete(unittest.TestCase):

    def setUp(self):
        os.system('python -u test_delete.py')
        
    def test_string_exist(self):
        """
        百度网盘删除文件
        """
        print('正在进行识别结果检测，正在逐个检查“待识别项”')
        scanner_set = {'newtest'}
        for i in scanner_set:
            self.assertTrue(com.screenshot_window_and_ocr(i,fuzzy=True))
        else:
            print('检测完成, 所有的待检测字符均出现')


# 百度网盘从回收站恢复文件功能
class Test_Recover(unittest.TestCase):

    def setUp(self):
        os.system('python -u test_recover.py')
        
    def test_string_exist(self):
        """
        百度网盘从回收站恢复文件
        """
        print('正在进行识别结果检测，正在逐个检查“待识别项”')
        scanner_set = {'newtest'}
        for i in scanner_set:
            self.assertTrue(com.screenshot_window_and_ocr(i,fuzzy=True))
        else:
            print('检测完成, 所有的待检测字符均出现')


# 百度网盘重命名功能
class Test_Rename(unittest.TestCase):

    def setUp(self):
        os.system('python -u test_rename.py')
        
    def test_string_exist(self):
        """
        百度网盘文件重命名
        """
        print('正在进行识别结果检测，正在逐个检查“待识别项”')
        scanner_set = {'newtest'}
        for i in scanner_set:
            self.assertTrue(com.screenshot_window_and_ocr(i,fuzzy=True))
        else:
            print('检测完成, 所有的待检测字符均出现')


# 百度网盘搜素全部文件
class Test_Search(unittest.TestCase):

    def setUp(self):
        os.system('python -u test_search.py')

    def test_string_exist(self):
        """
        百度网盘搜索文件
        """
        print('正在进行识别结果检测，正在逐个检查“待识别项”')
        scanner_set = {'mysql'}
        for i in scanner_set:
            self.assertTrue(com.screenshot_window_and_ocr(i,fuzzy=True))
        else:
            print('检测完成, 所有的待检测字符均出现')


# 百度网盘复制文件功能
class Test_Copy(unittest.TestCase):

    def setUp(self):
        os.system('python -u test_copy.py')

    def test_string_exist(self):
        """
        百度网盘复制文件到指定位置
        """
        print('正在进行识别结果检测，正在逐个检查“待识别项”')
        scanner_set = {'newtest'}
        for i in scanner_set:
            self.assertTrue(com.screenshot_window_and_ocr(i,fuzzy=True))
        else:
            print('检测完成, 所有的待检测字符均出现')


# 百度网盘文件上传功能
class Test_Upload(unittest.TestCase):

    def setUp(self):
        os.system('python -u test_upload.py')

    def test_string_exist(self):
        """
        百度网盘上传本地文件
        """
        print('正在进行识别结果检测，正在逐个检查“待识别项”')
        scanner_set = {'TestCase'}
        for i in scanner_set:
            self.assertTrue(com.screenshot_window_and_ocr(i,fuzzy=True))
        else:
            print('检测完成, 所有的待检测字符均出现')


# 百度网盘文件移动功能
class Test_Move(unittest.TestCase):

    def setUp(self):
        os.system('python -u test_move.py')

    def test_string_exist(self):
        """
        百度网盘移动文件到指定位置
        """
        print('正在进行识别结果检测，正在逐个检查“待识别项”')
        scanner_set = {'newtest'}
        for i in scanner_set:
            self.assertTrue(com.screenshot_window_and_ocr(i,fuzzy=True))
        else:
            print('检测完成, 所有的待检测字符均出现')


# 百度网盘文件分享功能
class Test_Share(unittest.TestCase):

    def setUp(self):
        os.system('python -u test_share.py')

    def test_string_exist(self):
        """
        百度网盘文件分享
        """
        print('正在进行识别结果检测，正在逐个检查“待识别项”')
        scanner_set = {'复制二维码'}
        for i in scanner_set:
            self.assertTrue(com.screenshot_window_and_ocr(i,fuzzy=True))
        else:
            print('检测完成, 所有的待检测字符均出现')

    def tearDown(self):
        res = fn.close_current_window()
        assert res == 0, '关闭应用失败'


# 测试百度网盘登出功能
class Test_Logout(unittest.TestCase):

    def setUp(self):
        os.system('python -u test_logout.py')

    def test_string_exist(self):
        """
        百度网盘退出登录功能
        """
        print('正在进行识别结果检测，正在逐个检查“待识别项”')
        scanner_set = {'手机号/用户名/邮箱','密码'}
        for i in scanner_set:
            self.assertTrue(com.screenshot_window_and_ocr(i,fuzzy=True))
        else:
            print('检测完成, 所有的待检测字符均出现')

    def tearDown(self):
        res = fn.close_current_window()
        assert res == 0, '关闭应用失败'


# 测试百度网盘下载功能
class Test_Download(unittest.TestCase):

    def setUp(self):
        os.system('python -u test_download.py')
        
    def test_string_exist(self):
        """
        百度网盘文件下载功能
        """
        print('正在进行识别结果检测，正在逐个检查“待识别项”')
        scanner_set = {'mytest'}
        for i in scanner_set:
            self.assertTrue(com.screenshot_window_and_ocr(i,fuzzy=True))
        else:
            print('检测完成, 所有的待检测字符均出现')


if __name__ == '__main__':
    suite = unittest.TestSuite()
    
    # 添加测试用例
    suite.addTest(unittest.makeSuite(Test_Login))
    suite.addTest(unittest.makeSuite(Test_Create))
    suite.addTest(unittest.makeSuite(Test_Download))
    suite.addTest(unittest.makeSuite(Test_Rename))
    suite.addTest(unittest.makeSuite(Test_Upload))
    suite.addTest(unittest.makeSuite(Test_Copy))
    suite.addTest(unittest.makeSuite(Test_Move))
    suite.addTest(unittest.makeSuite(Test_Delete))
    suite.addTest(unittest.makeSuite(Test_Recover))
    suite.addTest(unittest.makeSuite(Test_Search))
    suite.addTest(unittest.makeSuite(Test_Share))
    suite.addTest(unittest.makeSuite(Test_Logout))
    
    # 运行测试用例，生成报告
    runner = TestRunner(suite, tester='杨建国', title='测试报告',
                        desc='百度网盘测试报告', templates=2)

    runner.run()
