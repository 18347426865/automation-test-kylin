#!/usr/bin/python3
# coding=utf-8

###################
# Author: Yanrui Hu
# Date: 2022-06-01
# Platform: Kylin Desktop V10 SP1
# Description: 测试WPS Office的 所有测试用例
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
wpsofficedir = f"{testcasedir}/.."  # 此变量表示 wpsoffice 目录的路径
kylinautoguidir = f"{testcasedir}/../../kylinautogui"  # 不同的文件..的个数可能不一样
sys.path.append(wpsofficedir)
sys.path.append(kylinautoguidir)

from wps.TestCase.wps_all    import TestWps     # NOQA: E402
from wpspdf.TestCase.wpspdf_all import TestWpspdf  # NOQA: E402
from et.TestCase.et_all     import TestEt      # NOQA: E402
from wpp.TestCase.wpp_all    import TestWpp     # NOQA: E402

import libs.untils.functions as fn              # NOQA: E402
import libs.untils.composite as com             # NOQA: E402

# 暂时是样板代码, 或许用不上
# class TestWpsAll(unittest.TestCase):
#     """
#     测试WPS Office的 所有测试用例
#     """
#     @classmethod
#     def setUpClass(cls) -> None:
#         """
#         在所有测试用例执行前执行
#         """
#         print('WPS Office 测试环境初始化...')

#     @classmethod
#     def tearDownClass(cls) -> None:
#         """
#         在所有测试用例执行后执行
#         """
#         print('WPS Office 测试环境清理...')

#     def setUp(self) -> None:
#         """
#         每个测试用例执行前执行
#         """
#         pass

#     def tearDown(self) -> None:
#         """
#         每个测试用例执行完后执行
#         """
#         pass


if __name__ == '__main__':
    print('WPS Office 测试环境初始化...')
    # 清理(可能的)历史截图文件
    os.system(f'rm -rf {testcasedir}/../Outputs/screenshots/')

    # 创建截图文件的保存目录，
    fn.mkdir(f"{testcasedir}/../Outputs/screenshots")

    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestEt))
    suite.addTest(unittest.makeSuite(TestWpp))
    suite.addTest(unittest.makeSuite(TestWps))
    suite.addTest(unittest.makeSuite(TestWpspdf))

    runner = TestRunner(suite, filename='report2.html', report_dir=f'{wpsofficedir}/Outputs/reports',
                        title='WPS Office 测试报告', tester='Yanrui Hu', templates=2,
                        desc='测试WPS Office的 所有测试用例')
    runner.run()
