#!/usr/bin/python3
# coding=utf-8

###################
# Author: Jianguo Yang
# Date: 2022-05-26
# Platform: Kylin Desktop V10 SP1
# Description: 测试百度网盘的从回收站恢复文件功能
# Warning: 如果OCR服务崩溃，过往的测量数据只能用于特定的场景
# 分辨率：1920*1080, 字体设置为默认的11号
# Version: 1.0
###################

import os
from re import S
import sys
import time

os.environ['DISPLAY'] = ':0'  # 设置此参数以使得在远程连接情况下运行该文件而不报错
testcasedir = os.path.dirname(__file__)
kylinautoguidir = f"{testcasedir}/../../kylinautogui"
sys.path.append(kylinautoguidir)

import libs.untils.functions as fn  # NOQA: E402
import libs.untils.paddleocr as ocr  # NOQA: E402
import libs.untils.composite as com  # NOQA: E402


def test_recover(file_name: str):

    # 选中要恢复的文件，右键
    com.click_string_in_window(file_name, fuzzy=True, option=3)
    time.sleep(3)

    # 点击还原
    com.click_string_in_window('还原', fuzzy=True)
    time.sleep(3)

    # 确定还原
    com.click_string_in_window('确定', fuzzy=True)
    time.sleep(3)

    # 回到全部文件
    com.click_string_in_window('全部文件', fuzzy=True)
    time.sleep(3)


if __name__ == '__main__':

    # 启动应用
    res = fn.start_app('xdotool exec /opt/baidunetdisk/baidunetdisk')

    time.sleep(5)  # 等待窗口的响应

    test_recover(file_name="测试")
