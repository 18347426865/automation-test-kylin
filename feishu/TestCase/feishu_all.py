#!/usr/bin/python3
# coding=utf-8

###################
# Author: Yanrui Hu
# Date: 2022-06-01
# Platform: Kylin Desktop V10 SP1
# Description: 测试飞书所有的测试用例
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
rootdir = f"{testcasedir}/../../"  # 此变量表示 项目根目录的路径

sys.path.append(kylinautoguidir)
sys.path.append(rootdir)


import libs.untils.functions as fn   # NOQA: E402
import libs.untils.composite as com  # NOQA: E402
import feishu.TestCase.search as se                 # NOQA: E402
import feishu.TestCase.pin_chat as pc               # NOQA: E402
import feishu.TestCase.send_file as sf              # NOQA: E402
import feishu.TestCase.send_image as si             # NOQA: E402
import feishu.TestCase.create_group as cg           # NOQA: E402
import feishu.TestCase.delete_group as dg           # NOQA: E402
import feishu.TestCase.send_message as sm           # NOQA: E402
import feishu.TestCase.send_richtext as sr          # NOQA: E402
import feishu.TestCase.deal_with_later as dwl       # NOQA: E402
import feishu.TestCase.message_notification as mn   # NOQA: E402


class TestFeishu(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        """
        在所有测试用例执行前执行一次
        """
        print('飞书 测试环境初始化...')

        # 删除可能存在的文件
        os.system(f"rm -rf {testcasedir}/../Outputs/screenshots")
        os.system(f"rm -f feishu_test.*")

        # 创建截图文件的保存目录
        fn.mkdir(f"{testcasedir}/../Outputs/screenshots")

        # 启动应用
        fn.start_app('xdotool exec /usr/bin/bytedance-feishu-stable')
        time.sleep(5)  # 等待窗口的响应

        # 截图用于测试， 对应 self.send_img_path
        fn.screenshot_window('feishu_test.png', filepath='~')

        # 生成文件用于测试， 对应 self.send_file_path
        os.system(f"echo 'test!!' > ~/feishu_test.txt")

    @classmethod
    def tearDownClass(cls) -> None:
        """
        在所有测试用例执行后执行
        """
        print('飞书 测试环境清理...')
        # 关闭应用
        res = fn.key_input('alt+F4')
        assert res == True, '关闭"飞书"失败'
        fn.close_app('/usr/bin/bytedance-feishu-stable')
        time.sleep(5)

        # 删除文件
        # os.system(f'rm -rf {testcasedir}/../Outputs/screenshots')
        # 在测试结束之后删除图片会导致难以定位运行时的bug, 所以最好是在测试开始时清理图片

    def setUp(self) -> None:
        """
        每个测试用例执行前执行
        """
        # 下面的变量是所有的测试用例需要用到的参数
        self.group_name = '测试专用'  # 测试时的群聊名称
        self.type_ = '群组'
        self.send_img_path = '~/feishu_test.png'
        self.send_file_path = '~/feishu_test.txt'
        self.message = 'Hello World!'
        self.title = '测试标题'
        self.text = '测试正文'

    def tearDown(self) -> None:
        """
        每个测试用例执行完后执行
        """
        # fn.key_input('Escape')  # 关闭可能的提示窗口
        pass

    def test_01_create_group(self):
        """
        创建群聊
        """
        print('开始执行 create_group 测试用例')
        cg.create_group(group_name=self.group_name)

    def test_02_pin_group(self):
        """
        置顶群聊
        """
        print('开始执行 pin_group 测试用例')
        pc.pin_group(chat_name=self.group_name)

    def test_03_unpin_group(self):
        """
        取消置顶群聊
        """
        print('开始执行 unpin_group 测试用例')
        pc.unpin_group(chat_name=self.group_name)

    def test_04_add_deal_with_later(self):
        """
        添加到稍后处理
        """
        print('开始执行 add_deal_with_later 测试用例')
        dwl.add_deal_with_later(chat_name=self.group_name)

    def test_05_remove_deal_with_later(self):
        """
        从稍后处理中移除
        """
        print('开始执行 remove_deal_with_later 测试用例')
        dwl.remove_deal_with_later(chat_name=self.group_name)

    def test_06_disable_message_notification(self):
        """
        关闭消息通知
        """
        print('开始执行 disable_message_notification 测试用例')
        mn.disable_message_notification(chat_name=self.group_name)

    def test_07_enable_message_notification(self):
        """
        开启消息通知
        """
        print('开始执行 enable_message_notification 测试用例')
        mn.enable_message_notification(chat_name=self.group_name)

    def test_08_search_group(self):
        """
        搜索群聊
        """
        print('开始执行 search_group 测试用例')
        se.search(content=self.group_name, type_=self.type_)

    def test_09_send_message(self):
        """
        发送消息
        """
        print('开始执行 send_message 测试用例')
        sm.send_message(self.group_name, message=self.message)

    def test_10_send_richtext(self):
        """
        发送富文本
        """
        print('开始执行 send_richtext 测试用例')
        sr.send_richtext(self.group_name, title=self.title, text=self.text)

    def test_11_send_image(self):
        """
        发送图片
        """
        print('开始执行 send_image 测试用例')
        si.send_image(self.group_name, self.send_img_path)

    def test_12_send_file(self):
        """
        发送文件
        """
        print('开始执行 send_file 测试用例')
        sf.send_file(self.group_name, self.send_file_path)

    def test_13_delete_group(self):
        """
        删除群聊
        """
        print('开始执行 delete_group 测试用例')
        dg.delete_group(group_name=self.group_name)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestFeishu))

    runner = TestRunner(suite, filename='report2.html', report_dir=f'{testcasedir}/../Outputs/reports',
                        title='飞书 测试报告', tester='Yanrui Hu', templates=2,
                        desc='测试飞书 所有的测试用例')
    runner.run()
