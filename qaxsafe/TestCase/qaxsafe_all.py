#!/usr/bin/python3
# coding=utf-8

###################
# Author: Zizhi Ma
# Date: 2022-06-08
# Platform: Kylin Desktop V10 SP1
# Description: 测试奇安信网神终端系统所有的测试用例
# Warning: 如果OCR服务崩溃，过往的测量数据只能用于特定的场景
# 分辨率：1920*1080, 字体设置为默认的11号(在其他分辨率下应该也可以正常测试，奇安信网神终端系统窗口大小不变即可)
# Version: 1.0
###################
from unittestreport import TestRunner
import unittest
import os
import sys
import time


os.environ['DISPLAY'] = ':0'  # 设置此参数以使得在远程连接情况下运行该文件而不报错
testcasedir = os.path.dirname(__file__)  # 此变量表示 TestCase 目录的路径
kylinautoguidir = f"{testcasedir}/../../kylinautogui"  # 不同的文件..的个数可能不一样
rootdir = f"{testcasedir}/../../"  # 此变量表示 项目根目录的路径

sys.path.append(kylinautoguidir)
sys.path.append(rootdir)
import libs.untils.functions as fn   # NOQA: E402
import qaxsafe.TestCase.connect_testcase as con_test  # NOQA: E402
import qaxsafe.TestCase.test_immediate_scan as imm_scan  # NOQA: E402
import qaxsafe.TestCase.test_suspend_scan as sus_scan  # NOQA: E402
import qaxsafe.TestCase.test_continue_scan as con_scan  # NOQA: E402
import qaxsafe.TestCase.test_cancel_scan as can_scan  # NOQA: E402
import qaxsafe.TestCase.test_restart_scan as res_scan  # NOQA: E402
import qaxsafe.TestCase.test_fast_scan as fas_scan  # NOQA: E402
import qaxsafe.TestCase.test_whole_disk_scan as who_scan  # NOQA: E402
import qaxsafe.TestCase.test_self_defined_scan as sel_scan  # NOQA: E402
import qaxsafe.TestCase.test_add_trusted_file as add_file  # NOQA: E402
import qaxsafe.TestCase.test_add_trusted_extension as add_ext  # NOQA: E402
import qaxsafe.TestCase.test_delete_trusted_extension as del_ext  # NOQA: E402
import qaxsafe.TestCase.test_examine_security_log as exa_sec  # NOQA: E402


class TestQaxsafe(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        """
        在所有测试用例执行前执行一次
        """
        # 创建测试文件testMZZ.txt和文件夹testMZZ
        os.system("touch ~/testqax.txt")
        os.system("mkdir ~/testqax")

        print('奇安信网神终端管理系统 测试环境初始化...')

        # 删除可能存在的文件
        os.system(f"rm -rf {testcasedir}/../Outputs/screenshots/")

        # 创建截图文件的保存目录
        fn.mkdir(f"{testcasedir}/../Outputs/screenshots")

        # 启动应用
        fn.start_app('xdotool exec qaxtray --show')
        time.sleep(5)  # 等待窗口的响应

    @classmethod
    def tearDownClass(cls) -> None:
        """
        在所有测试用例执行后执行
        """
        print('奇安信网神终端管理系统 测试环境清理...')
        # 关闭应用
        res = fn.key_input('alt+F4')
        assert res == True, '关闭"奇安信网神终端管理系统"失败'
        fn.close_app('qaxtray')

        # 删除测试文件和文件夹
        os.system("rm -rf ~/testqax.txt")
        os.system("rm -rf ~/testqax")

        # 删除截图文件
        # os.system(f'rm -rf {testcasedir}/../Outputs/screenshots/*')
        # 在测试结束之后删除图片会导致难以定位运行时的bug, 所以最好是在测试开始时清理图片

    def setUp(self) -> None:
        """
        每个测试用例执行前执行
        """
        pass

    def tearDown(self) -> None:
        """
        每个测试用例执行完后执行
        """
        # fn.key_input('Escape')  # 关闭可能的提示窗口
        pass

    def test_01_immediate_scan(self):
        """
        立即扫描
        """
        print('开始执行 test_immediate_scan 测试用例')
        imm_scan.immediate_scan()

    def test_02_suspend_scan(self):
        """
        暂停扫描
        """
        print('开始执行 test_suspend_scan 测试用例')
        sus_scan.suspend_scan()

    def test_03_continue_scan(self):
        """
        继续扫描
        """
        print('开始执行 test_continue_scan 测试用例')
        con_scan.continue_scan()

    def test_04_cancel_scan(self):
        """
        取消扫描
        """
        print('开始执行 test_cancel_scan 测试用例')
        can_scan.cancel_scan()

    def test_05_restart_scan(self):
        """
        重新扫描
        """
        print('开始执行 test_restart_scan 测试用例')
        res_scan.restart_scan()

    def test_06_fast_scan(self):
        """
        快速扫描
        """
        print('开始执行 test_fast_scan 测试用例')
        fas_scan.fast_scan()
        con_test.return_to_main_page()

    def test_07_whole_disk_scan(self):
        """
        全盘扫描
        """
        print('开始执行 test_whole_disk_scan 测试用例')
        who_scan.whole_disk_scan()
        con_test.return_to_main_page()

    def test_08_self_defined_scan(self):
        """
        自定义扫描
        """
        print('开始执行 test_self_defined_scan 测试用例')
        sel_scan.self_defined_scan()
        con_test.return_to_main_page_sd()

    def test_09_add_trusted_file(self):
        """
        添加信任区文件
        """
        print('开始执行 test_add_trusted_file 测试用例')
        add_file.add_trusted_file()

    def test_10_add_trusted_extension(self):
        """
        添加信任区扩展名
        """
        print('开始执行 test_add_trusted_extension 测试用例')
        add_ext.add_trusted_extension()

    def test_11_delete_trusted_extension(self):
        """
        删除信任区扩展名
        """
        print('开始执行 test_delete_trusted_extension 测试用例')
        del_ext.delete_trusted_extension()
        con_test.close_current_window()

    def test_12_examine_security_log(self):
        """
        查看安全日志
        """
        print('开始执行 test_examine_security_log 测试用例')
        exa_sec.examine_security_log()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestQaxsafe))

    runner = TestRunner(suite, filename='report2.html', report_dir=f'{testcasedir}/../Outputs/reports',
                        title='奇安信网神终端管理系统 测试报告', tester='Zizhi Ma', templates=2,
                        desc='测试奇安信网神终端管理系统 所有的测试用例')
    runner.run()
