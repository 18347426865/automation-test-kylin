#!/usr/bin/python3
# coding=utf-8

###################
# Author: Zizhi Ma
# Date: 2022-05-24
# Platform: Kylin Desktop V10 SP1
# Description: 测试奇安信网神终端管理系统 的继续扫描功能
# Warning: 如果OCR服务崩溃，过往的测量数据只能用于特定的场景
# 分辨率：1920*1080, 字体设置为默认的11号
# Version: 1.0
###################

import os
import sys
import time

os.environ['DISPLAY'] = ':0'  # 设置此参数以使得在远程连接情况下运行该文件而不报错
testcasedir = os.path.dirname(__file__)
kylinautoguidir = f"{testcasedir}/../../kylinautogui"
sys.path.append(kylinautoguidir)

import libs.untils.functions as fn  # NOQA: E402
import libs.untils.composite as com  # NOQA: E402


def prepare():
    """
    继续扫描的准备工作(立即扫描后暂停)
    Parameters:None
    Returns: None
    """
    # 创建截图文件的保存目录，
    fn.mkdir(f"{testcasedir}/../Outputs/screenshots")

    # 启动应用
    fn.start_app('xdotool exec qaxtray --show')
    time.sleep(5)  # 等待窗口的响应

    # 点击“病毒查杀”
    com.click_string_in_window('病毒查杀', fuzzy=True)
    time.sleep(2)

    # 点击“立即扫描”
    com.click_string_in_window('立即扫描', fuzzy=True)
    time.sleep(15)

    # 点击“暂停”
    com.click_string_in_window('暂停', fuzzy=True)
    time.sleep(2)


def continue_scan():
    """
    继续扫描
    Parameters: None
    Returns: None
    """
    # 点击“继续扫描”
    com.click_string_in_window('继续扫描', fuzzy=True)
    time.sleep(5)

    # 验证是否成功继续扫描，界面是否出现“取消扫描”字样
    pos = com.get_string_coordinate_in_window('取消扫描', fuzzy=True)
    assert pos != {}, '继续扫描失败'
    print('继续扫描功能成功使用')


if __name__ == '__main__':
    prepare()

    continue_scan()
