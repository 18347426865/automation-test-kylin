#!/usr/bin/python3
# coding=utf-8

###################
# Author: Yanrui Hu
# Date: 2022-06-01
# Platform: Kylin Desktop V10 SP1
# Description: 测试WPS Office的表格 (et) 所有的测试用例
# Warning: 如果OCR服务崩溃，过往的测量数据只能用于特定的场景
# 分辨率：1920*1080, 字体设置为默认的11号
# Version: 1.0
###################


from unittestreport import TestRunner
import unittest
import os
import sys
import time


os.environ['DISPLAY'] = ':0'  # 设置此参数以使得在远程连接情况下运行该文件而不报错
testcasedir = os.path.dirname(__file__)  # 此变量表示 TestCase 目录的路径
kylinautoguidir = f"{testcasedir}/../../../kylinautogui"  # 不同的文件..的个数可能不一样
wpsofficedir = f"{testcasedir}/../.."  # 此变量表示 wpsoffice 目录的路径

sys.path.append(kylinautoguidir)
sys.path.append(wpsofficedir)


import libs.untils.functions as fn   # NOQA: E402
import libs.untils.composite as com  # NOQA: E402
import et.TestCase.et_create as et_create      # NOQA: E402
import et.TestCase.et_save_as as et_save_as    # NOQA: E402


class TestEt(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        """
        在所有测试用例执行前执行
        """
        print('WPS 表格 测试环境初始化...')

        # 删除文件
        os.system(f'rm -rf {testcasedir}/../Outputs/screenshots')
        os.system(f'rm ~/文档/*.et')
        os.system(f'rm ~/文档/*.xlsx')

        # 创建截图文件的保存目录，
        fn.mkdir(f"{testcasedir}/../Outputs/screenshots")

        # 启动应用
        res = fn.start_app('xdotool exec /usr/bin/et')
        assert res == True, 'WPS 表格 启动失败'
        time.sleep(8)  # 等待窗口的响应

        # 点击"我的文档"
        com.click_string_in_window('我的文档')
        time.sleep(2)

    @classmethod
    def tearDownClass(cls) -> None:
        """
        在所有测试用例执行后执行
        """
        print('WPS 表格 测试环境清理...')
        # 关闭应用
        res = fn.key_input('alt+F4')
        assert res == True, '关闭WPS表格失败'
        fn.close_app('/usr/bin/et')
        time.sleep(5)

        os.system(f'rm ~/文档/*.et')
        os.system(f'rm ~/文档/*.xlsx')

    def setUp(self) -> None:
        """
        每个测试用例执行前执行
        """
        self.filename = "TESTFILE.et"
        self.newfilename = 'TESTFILE.xlsx'
        self.inputdata = 'helloworld'

    def tearDown(self) -> None:
        """
        每个测试用例执行完后执行
        """
        fn.key_input('ctrl+w')  # 关闭标签页
        time.sleep(2)

    def test_01_create(self):
        """
        新建et表格文件
        """
        print('开始执行 create 测试用例')
        et_create.create_file(self.filename, self.inputdata)

    def test_02_save_as(self):
        """
        将et表格文件保存为xlsx文件
        """
        print('开始执行 save_as 测试用例')
        et_save_as.save_as_file(filename=self.filename,
                                newfilename=self.newfilename)


if __name__ == '__main__':
    suite = unittest.TestSuite()

    suite.addTest(unittest.makeSuite(TestEt))

    runner = TestRunner(suite, filename='report2.html', report_dir=f'{testcasedir}/../Outputs/reports',
                        title='WPS 表格 测试报告', tester='Yanrui Hu', templates=2,
                        desc='测试WPS Office的表格 (et) 所有的测试用例')
    runner.run()
