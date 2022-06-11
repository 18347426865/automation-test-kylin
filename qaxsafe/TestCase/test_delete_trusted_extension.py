#!/usr/bin/python3
# coding=utf-8

###################
# Author: Zizhi Ma
# Date: 2022-05-28
# Platform: Kylin Desktop V10 SP1
# Description: 测试奇安信网神终端管理系统 的删除信任扩展名功能
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
    删除信任扩展名的准备工作(添加信任扩展名)
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
    window_pos = fn.get_active_window_position()

    #  line 51-69 是点击信任区的方法，由于检测时信任区隔离区鉴定区三块文字间隔过近
    #  导致这九个字被鉴定为一块区域，string=‘信任区’时
    #  get_string-coordinate_in_window获取的是‘信任区隔离区鉴定区’整块的中间位置，并点击
    #  所以正常调用时会点击到中间的鉴定区
    #  于是，我们采用定位九个字中间位置，并左移鼠标一段距离定位‘信任区’三个字，并点击的方法

    # 获取“信任区”文字坐标（实际获取了“信任区隔离区鉴定区”的中心坐标）
    pos = com.get_string_coordinate_in_window('信任区', fuzzy=True)
    time.sleep(1)
    print(f'信任区隔离区鉴定区文字的坐标是{pos}')

    # 定位信任区文字的中心坐标
    xlabel = window_pos[0] + pos[0] - 40
    ylabel = window_pos[1] + pos[1]
    print(xlabel, ylabel)

    # 将鼠标移动至信任区的位置
    res = fn.mouse_move_absolute(xlabel, ylabel)
    assert res == True, '鼠标移动失败'
    time.sleep(3)

    # 点击
    res = fn.mouse_click('left')
    assert res == True, '鼠标点击失败'
    time.sleep(2)


def delete_trusted_extension():
    """
    添加信任区文件
    Parameters: None
    Returns: None
    """
    fn.get_active_window_info()
    window_pos = fn.get_active_window_position()

    # 点击“添加扩展名”
    com.click_string_in_window('添加扩展名', fuzzy=True)
    time.sleep(2)

    # 输入“doc”
    fn.input_string("doc")
    time.sleep(2)

    # 点击“确定”
    com.click_string_in_window('确定', fuzzy=True)
    time.sleep(2)

    # line 88-105,选中".doc"对应的提示框
    pos = com.get_string_coordinate_in_window('doc', fuzzy=True)
    time.sleep(1)
    print(f'.doc的坐标是{pos}')

    # 定位".doc"对应提示框的中心坐标
    xlabel = window_pos[0] + pos[0] - 30
    ylabel = window_pos[1] + pos[1]
    print(xlabel, ylabel)

    # 将鼠标移动至该提示框的位置
    res = fn.mouse_move_absolute(xlabel, ylabel)
    assert res == True, '鼠标移动失败'
    time.sleep(3)

    # 点击
    res = fn.mouse_click('left')
    assert res == True, '鼠标点击失败'
    time.sleep(2)

    # line 108-125,选中"添加扩展名"下方的"删除"
    pos = com.get_string_coordinate_in_window('添加扩展名')
    time.sleep(1)
    print(f'添加扩展名的坐标是{pos}')

    # 定位"添加扩展名"文字的中心坐标
    xlabel = window_pos[0] + pos[0]
    ylabel = window_pos[1] + pos[1] + 70
    print(xlabel, ylabel)

    # 将鼠标移动至该提示框的位置
    res = fn.mouse_move_absolute(xlabel, ylabel)
    assert res == True, '鼠标移动失败'
    time.sleep(2)

    # 点击
    res = fn.mouse_click('left')
    assert res == True, '鼠标点击失败'
    time.sleep(2)

    # 验证是否成功删除，即界面上不再有添加的‘doc’扩展名
    pos = com.get_string_coordinate_in_window('doc', fuzzy=True)
    assert pos == {}, '删除信任扩展名失败'
    print('删除信任扩展名成功')


if __name__ == '__main__':
    prepare()

    delete_trusted_extension()
