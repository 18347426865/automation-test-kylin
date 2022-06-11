#!/usr/bin/python3
# coding=utf-8

###################
# Author: Zizhi Ma
# Date: 2022-05-26
# Platform: Kylin Desktop V10 SP1
# Description: 测试奇安信网神终端管理系统 的重新扫描功能
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
    重新扫描的准备工作
    Parameters:None
    Returns: None
    """
    # 创建截图文件的保存目录，
    fn.mkdir(f"{testcasedir}/../Outputs/screenshots")

    # 启动应用
    fn.start_app('xdotool exec qaxtray --show')
    time.sleep(5)

    # 点击“病毒查杀”
    com.click_string_in_window('病毒查杀', fuzzy=True)
    time.sleep(2)

    # 点击“立即扫描”
    com.click_string_in_window('立即扫描', fuzzy=True)
    time.sleep(5)

    # 点击“取消扫描”
    com.click_string_in_window('取消扫描', fuzzy=True)
    time.sleep(5)

    # 点击“终止扫描”
    com.click_string_in_window('终止扫描', fuzzy=True)
    time.sleep(2)


def restart_scan():
    """
    重新扫描
    Parameters: None
    Returns: None
    """
    # 点击“重新扫描”
    com.click_string_in_window('重新扫描', fuzzy=True)
    time.sleep(5)

    # 验证是否跳转到主页面,界面会提醒‘上次扫描’字样
    pos = com.get_string_coordinate_in_window('上次扫描', fuzzy=True)
    assert pos != {}, '跳转失败，重新扫描功能出现问题'
    print('重新扫描功能成功使用')


if __name__ == '__main__':
    prepare()

    restart_scan()
