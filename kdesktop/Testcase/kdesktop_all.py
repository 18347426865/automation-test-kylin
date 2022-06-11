#!/usr/bin/python3
# coding=utf-8

###################
# Author: Ziyu Lu
# Date: 2022-06-01
# Platform: Kylin Desktop V10 SP1
# Description: 测试金山文档所有的测试用例
# Warning: 如果OCR服务崩溃，过往的测量数据只能用于特定的场景
# 分辨率：1920*1200, 字体设置为默认的11号
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
import kdesktop.Testcase.test_upload as up  # NOQA: E402
import kdesktop.Testcase.test_recover as re  # NOQA: E402
import kdesktop.Testcase.test_delete as de  # NOQA: E402
import kdesktop.Testcase.test_mkdir as md  # NOQA: E402
import kdesktop.Testcase.test_copy as co  # NOQA: E402
import kdesktop.Testcase.test_star as st  # NOQA: E402
import kdesktop.Testcase.test_change as ch  # NOQA: E402
import kdesktop.Testcase.test_search as se  # NOQA: E402
import kdesktop.Testcase.test_newmind as nm  # NOQA: E402
import kdesktop.Testcase.test_newppt as np  # NOQA: E402
import kdesktop.Testcase.test_newexcel as ne  # NOQA: E402
import kdesktop.Testcase.test_newdoc as nd  # NOQA: E402


class TestKdesktop(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        """
        在所有测试用例执行前执行一次
        """
        print('金山文档 测试环境初始化...')

        # 删除可能存在的文件
        os.system(f"rm -rf {testcasedir}/../Outputs/screenshots/")

        # 创建截图文件的保存目录
        fn.mkdir(f"{testcasedir}/../Outputs/screenshots")

        # 启动应用
        res = fn.start_app(
            'xdotool exec /opt/apps/cn.kdocs.kdesktop/files/bin/kdesktop')
        time.sleep(5)  # 等待窗口的响应

        window_id = fn.get_active_window_id()

        # 提前设置窗口位置和大小，要不然ocr识别不到
        fn.move_window(window_id, 0, 0)
        fn._set_window_size(window_id, 1200, 900)

        cls.doc_name = 'DOC'+time.strftime('%Y%m%d%H%M%S', time.localtime())
        cls.excel_name = 'EXCEL'+time.strftime('%Y%m%d%H%M%S', time.localtime())
        cls.ppt_name = 'PPT'+time.strftime('%Y%m%d%H%M%S', time.localtime())
        cls.mind_name = 'MIND'+time.strftime('%Y%m%d%H%M%S', time.localtime())
        cls.star_name = cls.mind_name
        cls.mkdir_name = 'DIR'+time.strftime('%Y%m%d%H%M%S', time.localtime())  # 新建文件夹的名称
        cls.del_name1 = cls.mind_name
        cls.rec_name1 = cls.mind_name
        cls.upfile_name = 'UP'+time.strftime('%Y%m%d%H%M%S', time.localtime())
        cls.copy_file_name = cls.mind_name  # 被复制的文件是什么?
        cls.dest_dir = cls.mkdir_name   # 复制到哪里?

    @classmethod
    def tearDownClass(cls) -> None:
        """
        在所有测试用例执行后执行
        """
        print('金山文档 测试环境清理...')
        # 关闭应用
        res = fn.key_input('alt+F4')
        assert res == True, '关闭"金山文档"失败'
        fn.close_app('/opt/apps/cn.kdocs.kdesktop/files/bin/kdesktop')

    def setUp(self) -> None:

        fn.click_location(50, 30)  # 点击首页标签
        time.sleep(4)

        # 回到 最近
        leftbar_region = [0, 0, 300, 720]
        com.click_string_in_window_region(leftbar_region, '最近')
        time.sleep(4)

        # 刷新
        fn.key_input('F5')
        time.sleep(4)

    def test_01_newdoc(self):
        """
        新建文档
        """
        print('开始执行 newdoc 测试用例')
        nd.new_doc(self.doc_name)

    def test_02_newexcel(self):
        """
        新建表格
        """
        print('开始执行 newexcel 测试用例')
        ne.new_excel(self.excel_name)

    def test_03_newppt(self):
        """
        新建ppt
        """
        print('开始执行 newppt 测试用例')
        np.new_ppt(self.ppt_name)

    def test_04_newmind(self):
        """
        新建思维导图
        """
        print('开始执行 newmind 测试用例')
        nm.new_mind(self.mind_name)

    def test_05_search(self):
        """
        测试搜索
        """
        print('开始执行 search 测试用例')
        se.search(self.mind_name)

    def test_06_change(self):
        """
        测试换一批
        """
        print('开始执行 change 测试用例')
        ch.change()

    def test_07_star(self):
        """
        测试星标
        """
        print('开始执行 star 测试用例')
        st.star(self.star_name)

    def test_08_delete(self):
        """
        测试删除
        """
        print('开始执行 delete 测试用例')
        de.delete(self.del_name1)

    def test_09_recover(self):
        """
        测试恢复
        """
        print('开始执行 recover 测试用例')
        re.recover(self.rec_name1)

    def test_10_mkdir(self):
        """
        测试新建文件夹
        """
        print('开始执行 mkdir 测试用例')
        md.mkdir(self.mkdir_name)

    def test_11_upload(self):
        """
        测试上传
        """
        print('开始执行 upload 测试用例')
        up.upload(self.upfile_name)

    def test_12_copy(self):
        """
        测试复制
        """
        print('开始执行 copy 测试用例')
        co.copy(self.copy_file_name, self.dest_dir)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestKdesktop))

    runner = TestRunner(suite, filename='report.html', report_dir=f'{testcasedir}/../Outputs/reports',
                        title='金山文档 测试报告', tester='Ziyu Lu', templates=2,
                        desc='测试金山文档 所有的测试用例')
    runner.run()
