#!/usr/bin/python3
# coding=utf-8

###################
# Author: Jianguo Yang
# Date: 2022-06-01
# Platform: Kylin Desktop V10 SP1
# Description: 测试百度网盘所有的测试用例
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
kylinautoguidir = f"{testcasedir}/../../kylinautogui"  # 不同的文件..的个数可能不一样
rootdir = f"{testcasedir}/../../"  # 此变量表示 feishu 目录的路径

sys.path.append(kylinautoguidir)
sys.path.append(rootdir)

import libs.untils.functions as fn   # NOQA: E402
import libs.untils.composite as com  # NOQA: E402
import baidunetdisk.TestCase.test_login as li  # NOQA: E402
import baidunetdisk.TestCase.test_create as tc  # NOQA: E402
import baidunetdisk.TestCase.test_download as td  # NOQA: E402
import baidunetdisk.TestCase.test_rename as tn  # NOQA: E402
import baidunetdisk.TestCase.test_upload as tu  # NOQA: E402
import baidunetdisk.TestCase.test_copy as ty  # NOQA: E402
import baidunetdisk.TestCase.test_move as tm  # NOQA: E402
import baidunetdisk.TestCase.test_delete as te  # NOQA: E402
import baidunetdisk.TestCase.test_recover as tr  # NOQA: E402
import baidunetdisk.TestCase.test_search as ts  # NOQA: E402
import baidunetdisk.TestCase.test_share as th  # NOQA: E402
import baidunetdisk.TestCase.test_logout as tl  # NOQA: E402


class TestBaidunetdisk(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        """
        在所有测试用例执行前执行一次
        """
        print('百度网盘 测试环境初始化...')

        # 删除可能存在的文件
        os.system(f"rm -rf {testcasedir}/../Outputs/screenshots/")

        # 创建截图文件的保存目录
        fn.mkdir(f"{testcasedir}/../Outputs/screenshots")

        # 启动应用
        fn.start_app('xdotool exec /opt/baidunetdisk/baidunetdisk')
        time.sleep(15)  # 等待窗口的响应

    @classmethod
    def tearDownClass(cls) -> None:
        """
        在所有测试用例执行后执行
        """
        print('百度网盘 测试环境清理...')
        # 关闭应用
        res = fn.key_input('alt+F4')
        assert res == True, '关闭"百度网盘"失败'
        fn.close_app('/opt/baidunetdisk/baidunetdisk')

    def setUp(self) -> None:
        """
        每个测试用例执行前执行
        """
        self.create_name = "mytest"  # 新建文件，下载文件，重命名文件
        self.newname = "newtest"  # 重命名文件
        self.copy_path = "银河"    # 复制，移动文件的路径名
        self.move_path = "abc"    # 移动文件路径名
        self.upload_name = "UPLOAD"  # 上传文件名
        self.operate_name = "测试"    # 复制，移动，删除，恢复
        self.key_name = "ab"  # 搜索关键字
        self.share_name = "abc" # 搜索，分享
        self.logout_user = "183*****86552" # 退出登录
        self.login_user = "18347426865"  # 登录用户名
        self.login_pwd = "111213yjg"    # 登录密码

    def tearDown(self) -> None:
        """
        每个测试用例执行完后执行
        """
        pass

    @unittest.skip("跳过登录")
    def test_01_baidunetdisk_login(self):
        """
        百度网盘登录功能
        """
        print('开始执行 test_login 测试用例')
        li.test_login(user=self.login_user, pwd=self.login_pwd)

    def test_02_baidunetdisk_create(self):
        """
        百度网盘新建文件功能
        """
        print('开始执行 test_login 测试用例')
        tc.test_create(file_name=self.create_name)

    def test_03_baidunetdisk_download(self):
        """
        百度网盘下载文件功能
        """
        print('开始执行 test_download 测试用例')
        td.test_download(file_name=self.create_name)

    def test_04_baidunetdisk_rename(self):
        """
        百度网盘重命名功能
        """
        print('开始执行 test_rename 测试用例')
        tn.test_rename(old_name=self.create_name, new_name=self.newname)

    def test_05_baidunetdisk_upload(self):
        """
        百度网盘上传文件功能
        """
        print('开始执行 test_upload 测试用例')
        tu.test_upload(upfile_name=self.upload_name)

    def test_06_baidunetdisk_copy(self):
        """
        百度网盘复制文件功能
        """
        print('开始执行 test_copy 测试用例')
        ty.test_copy(file_name=self.operate_name, myfile=self.copy_path)

    def test_07_baidunetdisk_move(self):
        """
        百度网盘文件移动功能
        """
        print('开始执行 test_move 测试用例')
        tm.test_move(file_name=self.operate_name,
                     myfile=self.move_path, path=self.copy_path)

    def test_08_baidunetdisk_delete(self):
        """
        百度网盘文件删除功能
        """
        print('开始执行 test_delete 测试用例')
        te.test_delete(file_name=self.operate_name)

    def test_09_baidunetdisk_recover(self):
        """
        百度网盘文件恢复功能
        """
        print('开始执行 test_recover 测试用例')
        tr.test_recover(file_name=self.operate_name)

    def test_10_baidunetdisk_search(self):
        """
        百度网盘文件搜索功能
        """
        print('开始执行 test_search 测试用例')
        ts.test_search(name=self.key_name, file_name=self.share_name)

    def test_11_baidunetdisk_search(self):
        """
        百度网盘文件分享功能
        """
        print('开始执行 test_share 测试用例')
        th.test_share(file_name=self.share_name)

    @unittest.skip("跳过退出登录")
    def test_12_baidunetdisk_logout(self):
        """
        百度网盘退出登录功能
        """
        print('开始执行 test_logout 测试用例')
        tl.test_logout(user=self.logout_user)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestBaidunetdisk))

    runner = TestRunner(suite, filename='report.html', report_dir=f'{testcasedir}/../Outputs/reports',
                        title='百度网盘 测试报告', tester='杨建国', templates=2,
                        desc='测试百度网盘 所有的测试用例')
    runner.run()
