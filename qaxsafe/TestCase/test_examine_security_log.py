#!/usr/bin/python3
# coding=utf-8

###################
# Author: Zizhi Ma
# Date: 2022-05-24
# Platform: Kylin Desktop V10 SP1
# Description: 测试奇安信网神终端管理系统 的查看安全日志功能
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
    查看安全日志的准备工作(进入主页面，是否进入病毒查杀页面都可)
    Parameters:None
    Returns: None
    """
    # 创建截图文件的保存目录，
    fn.mkdir(f"{testcasedir}/../Outputs/screenshots")

    # 启动应用
    fn.start_app('xdotool exec qaxtray --show')
    time.sleep(5)  # 等待窗口的响应


def examine_security_log():
    """
    取消扫描
    Parameters: None
    Returns: None
    """
    fn.get_active_window_info()
    window_pos = fn.get_active_window_position()

    # 获取三条杠符号的坐标（实际获取了扫描出的“三-x”的中心坐标）
    pos = com.get_string_coordinate_in_window('三', fuzzy=True)
    time.sleep(1)
    print(f'三-x的坐标是{pos}')

    # 定位三条杠符号的中心坐标
    xlabel = window_pos[0] + pos[0] - 40
    ylabel = window_pos[1] + pos[1]
    print(xlabel, ylabel)

    # 将鼠标移动至该符号的位置
    res = fn.mouse_move_absolute(xlabel, ylabel)
    assert res == True, '鼠标移动失败'
    time.sleep(3)

    # 点击
    res = fn.mouse_click('left')
    assert res == True, '鼠标点击失败'
    time.sleep(2)

    # 点击“安全日志”
    com.click_string_in_window('安全日志', fuzzy=True)
    time.sleep(2)

    # 验证是否成功进入安全日志，界面上是否出现‘清空记录’字样
    pos = com.get_string_coordinate_in_window('清空记录', fuzzy=True)
    assert pos != {}, '进入安全日志失败'
    print('进入安全日志成功')


if __name__ == '__main__':
    prepare()

    examine_security_log()
