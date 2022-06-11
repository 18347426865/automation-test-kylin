#!/usr/bin/python3
# coding=utf-8

###################
# Author: Zizhi Ma
# Date: 2022-05-24
# Platform: Kylin Desktop V10 SP1
# Description: 测试奇安信网神终端管理系统 的暂停扫描功能
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
    暂停扫描的准备工作(进入立即扫描)
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


def suspend_scan():
    """
    暂停扫描
    Parameters: None
    Returns: None
    """

    # 点击“暂停”
    com.click_string_in_window('暂停', fuzzy=True)
    time.sleep(5)

    # 验证是否成功暂停扫描，界面出现‘继续扫描’提示字样
    pos = com.get_string_coordinate_in_window('继续扫描', fuzzy=True)
    assert pos != {}, '没有暂停成功'
    print('暂停功能成功使用')


if __name__ == '__main__':
    prepare()

    suspend_scan()
