#!/usr/bin/python3
# coding=utf-8

###################
# Author: Zizhi Ma
# Date: 2022-06-08
# Platform: Kylin Desktop V10 SP1
# Description: 奇安信网神终端管理系统 测试样例串联所用的函数
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


def return_to_main_page():
    """
    用于快速、全盘扫描中结束扫描并点击重新扫描回到主页面
    Parameters:None
    Returns: None
    """
    time.sleep(10)

    # 点击“取消扫描”
    com.click_string_in_window('取消扫描', fuzzy=True)
    time.sleep(2)

    # 点击“终止扫描”
    com.click_string_in_window('终止扫描', fuzzy=True)
    time.sleep(2)

    # 点击“重新扫描”
    com.click_string_in_window('重新扫描', fuzzy=True)
    time.sleep(3)


def return_to_main_page_sd():
    """
    用于自定义扫描中结束扫描并回到主页面
    Parameters:None
    Returns: None
    """
    time.sleep(5)

    # 点击“重新扫描”
    com.click_string_in_window('重新扫描', fuzzy=True)
    time.sleep(3)


def close_current_window():
    """
    用于删除信任扩展名后回到首页
    Parameters:None
    Returns: None
    """
    # 快捷键直接退出窗口
    fn.key_input('alt+F4')
