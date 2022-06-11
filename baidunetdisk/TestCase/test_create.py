#!/usr/bin/python3
# coding=utf-8

###################
# Author: Jianguo Yang
# Date: 2022-05-26
# Platform: Kylin Desktop V10 SP1
# Description: 测试百度网盘的新建文件夹功能
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
import libs.untils.paddleocr as ocr  # NOQA: E402
import libs.untils.composite as com  # NOQA: E402


def test_create(file_name: str):

    # 点击新建文件夹
    com.click_string_in_window('新建文件夹', fuzzy=True)
    time.sleep(3)

    # 输入新文件夹名字
    fn.paste_string(file_name)
    time.sleep(3)

    # 确认
    fn.key_input("Return")
    time.sleep(3)

    # 验证创建文件成功
    pos = com.get_string_coordinate_in_window(file_name)
    assert pos != {}, '新建成功'
    print('百度网盘新建文件成功')


if __name__ == '__main__':

    # 启动应用
    res = fn.start_app('xdotool exec /opt/baidunetdisk/baidunetdisk')

    time.sleep(5)  # 等待窗口的响应

    test_create(file_name="mytest")
