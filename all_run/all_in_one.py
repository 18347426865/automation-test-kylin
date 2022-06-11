#!/usr/bin/python3
# coding=utf-8

###################
# Author: Jianguo Ynag
# Date: 2022-06-01
# Platform: Kylin Desktop V10 SP1
# Description: 测试五个应用的所有测试用例
# Warning: 如果OCR服务崩溃，过往的测量数据只能用于特定的场景
# 分辨率：1920*1080, 设置为默认的11号
# Version: 1.0
###################


from unittestreport import TestRunner
import unittest
import os
import sys


os.environ['DISPLAY'] = ':0'  # 设置此参数以使得在远程连接情况下运行该文件而不报错
testcasedir = os.path.dirname(__file__)  # 此变量表示 all_run 目录的路径
rootdir = f"{testcasedir}/.."  # 此变量表示项目根目录的路径
sys.path.append(rootdir)

import kylinautogui.libs.untils.functions as fn   # NOQA: E402
import kylinautogui.libs.untils.composite as com  # NOQA: E402

from feishu.TestCase.feishu_all import TestFeishu                   # NOQA: E402
from qaxsafe.TestCase.qaxsafe_all import TestQaxsafe                # NOQA: E402
from baidunetdisk.TestCase.baidunetdisk_all import TestBaidunetdisk  # NOQA: E402
from kdesktop.Testcase.kdesktop_all import TestKdesktop             # NOQA: E402

from wpsoffice.et.TestCase.et_all import TestEt                     # NOQA: E402
from wpsoffice.wpp.TestCase.wpp_all import TestWpp                  # NOQA: E402
from wpsoffice.wps.TestCase.wps_all import TestWps                  # NOQA: E402
from wpsoffice.wpspdf.TestCase.wpspdf_all import TestWpspdf         # NOQA: E402

if __name__ == '__main__':

    print('所有五个应用的测试环境的初始化...')

    # 清理(可能的)历史截图文件
    os.system(f'rm -rf {testcasedir}/../Outputs/screenshots/')

    # 创建截图文件的保存目录，
    fn.mkdir(f"{testcasedir}/../Outputs/screenshots")

    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestEt))
    suite.addTest(unittest.makeSuite(TestWpp))
    suite.addTest(unittest.makeSuite(TestWps))
    suite.addTest(unittest.makeSuite(TestWpspdf))
    suite.addTest(unittest.makeSuite(TestQaxsafe))
    suite.addTest(unittest.makeSuite(TestFeishu))
    suite.addTest(unittest.makeSuite(TestKdesktop))
    suite.addTest(unittest.makeSuite(TestBaidunetdisk))

    runner = TestRunner(suite, filename='report2.html', report_dir=f'{rootdir}/Outputs/reports',
                        title='所有应用的测试报告', tester='Yanrui Hu', templates=2,
                        desc='测试五个应用所有测试用例')

    # 执行测试
    runner.run()
