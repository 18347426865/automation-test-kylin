#!/usr/bin/python3
# coding=utf-8

###################
# Author: Zizhi Ma
# Date: 2022-05-26
# Platform: Kylin Desktop V10 SP1
# Description: 测试奇安信网神终端管理系统 的全盘扫描功能
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
    全盘扫描的准备工作(进入病毒查杀界面)
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


def whole_disk_scan():
    """
    全盘扫描
    Parameters: None
    Returns: None
    """
    window_pos = fn.get_active_window_position()

    # 获取“全盘扫描”文字坐标
    pos = com.get_string_coordinate_in_window('全盘扫描')
    time.sleep(1)
    print(f'全盘扫描文字的坐标是{pos}')

    # 定位全盘扫描对应图案的坐标
    xlabel = window_pos[0] + pos[0]
    ylabel = window_pos[1] + pos[1] - 60
    print(xlabel, ylabel)

    # 将鼠标移动至全盘扫描对应的图案
    res = fn.mouse_move_absolute(xlabel, ylabel)
    assert res == True, '鼠标移动失败'
    time.sleep(3)

    # 点击全盘扫描对应的图案
    res = fn.mouse_click('left')
    assert res == True, '鼠标点击失败'
    time.sleep(10)

    # 验证是否成功进入快速扫描，界面上会出现“正在”（扫描，检查）字样
    # 以上sleep时间较长以防止因电脑性能造成的功能启动慢
    pos = com.get_string_coordinate_in_window('正在', fuzzy=True)
    assert pos != {}, '进入全盘扫描失败'
    print('全盘扫描功能启动成功')


if __name__ == '__main__':
    prepare()

    whole_disk_scan()
