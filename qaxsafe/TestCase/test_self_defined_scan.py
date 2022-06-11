#!/usr/bin/python3
# coding=utf-8

###################
# Author: Zizhi Ma
# Date: 2022-05-26
# Platform: Kylin Desktop V10 SP1
# Description: 测试奇安信网神终端管理系统 的自定义扫描功能
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
    自定义扫描的准备工作
    Parameters:None
    Returns: None
    """
    os.system("mkdir ~/testqax")

    # 创建截图文件的保存目录，
    fn.mkdir(f"{testcasedir}/../Outputs/screenshots")

    # 启动应用
    fn.start_app('xdotool exec qaxtray --show')
    time.sleep(5)  # 等待窗口的响应

    # 点击“病毒查杀”
    com.click_string_in_window('病毒查杀', fuzzy=True)
    time.sleep(2)


def self_defined_scan():
    """
    自定义扫描
    Parameters: None
    Returns: None
    """
    window_pos = fn.get_active_window_position()

    # 获取“自定义扫描”文字坐标
    pos = com.get_string_coordinate_in_window('自定义扫描')
    time.sleep(1)
    print(f'自定义扫描文字的坐标是{pos}')

    # 定位自定义扫描对应图案的坐标
    xlabel = window_pos[0] + pos[0]
    ylabel = window_pos[1] + pos[1] - 60
    print(xlabel, ylabel)

    # 将鼠标移动至自定义扫描对应的图案
    res = fn.mouse_move_absolute(xlabel, ylabel)
    assert res == True, '鼠标移动失败'
    time.sleep(3)

    # 点击自定义扫描对应的图案
    res = fn.mouse_click('left')
    assert res == True, '鼠标点击失败'
    time.sleep(2)
    fn.get_active_window_info()

    # 输入制定的样例位置
    fn.input_string("~/testqax")
    time.sleep(1)

    # 点击回车键
    fn.key_input('Return')
    time.sleep(3)

    # 验证是否成功进入快速扫描，界面上会出现‘扫描’（完成）字样
    # 以上sleep时间较短，因为创建的文件夹为空，扫描立即完成
    pos = com.get_string_coordinate_in_window('扫描', fuzzy=True)
    assert pos != {}, '进入自定义扫描失败'
    print('自定义扫描功能启动成功')


def recover():
    """
    自定义扫描测试后复原系统断点
    Parameters: None
    Returns: None
    """
    os.system("rm -rf ~/testqax")


if __name__ == '__main__':
    prepare()

    self_defined_scan()

    recover()
