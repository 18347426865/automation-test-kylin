#!/usr/bin/python3
# coding=utf-8

###################
# Author: Ziyu Lu
# Date: 2022-05-17
# Platform: Kylin Desktop V10 SP1
# Description: 测试金山文档文档的星标功能
# Warning: 如果OCR服务崩溃，过往的测量数据只能用于特定的场景
# 分辨率：1920*1200, 字体设置为默认的11号
# Version: 1.0
###################


import os
import sys
import time

os.environ['DISPLAY'] = ':0'  # 设置此参数以使得在远程连接情况下运行该文件而不报错
sys.path.append('../../kylinautogui')
import libs.untils.functions as fn  # NOQA: E402
import libs.untils.composite as com  # NOQA: E402


def star(doc_name: str) -> None:
    """
    星标一个文档
    :param1: 文件名称
    """
    doclist_region = [230, 160, 910, 670]
    # 在文档列表中右击文档
    com.click_string_in_window_region(doclist_region, doc_name, option=3)
    time.sleep(4)

    com.click_string_in_window_region(doclist_region, '星标')
    time.sleep(4)

    fn.key_input('F5')
    time.sleep(4)

    # 在文档列表中右击文档
    com.click_string_in_window_region(doclist_region, doc_name, option=3)
    time.sleep(4)

    com.click_string_in_window_region(doclist_region, '取消星标')
    time.sleep(4)

    fn.key_input('F5')
    time.sleep(4)

    print(f'{sys._getframe().f_code}  (*^▽^*)测试完成！\n')


def prepare():
    """
    准备工作
    """
    # 创建截图文件的保存目录，
    fn.mkdir("../Outputs/screenshots")

    # 启动应用
    fn.start_app(
        'xdotool exec /opt/apps/cn.kdocs.kdesktop/files/bin/kdesktop')
    time.sleep(4)

    # 获取窗口id
    window_id = fn.get_active_window_id()

    # 提前设置窗口位置和大小，要不然ocr识别不到
    fn.move_window(window_id, 0, 0)
    fn._set_window_size(window_id, 1200, 900)

    fn.click_location(50, 30)  # 点击首页标签
    time.sleep(4)


if __name__ == '__main__':
    prepare()

    star(doc_name='MIMIM')
