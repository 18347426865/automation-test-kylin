#!/usr/bin/python3
# coding=utf-8

###################
# Author: Jianguo Yang
# Date: 2022-05-26
# Platform: Kylin Desktop V10 SP1
# Description: 测试百度网盘的文件复制到功能
# Warning: 如果OCR服务崩溃，过往的测量数据只能用于特定的场景
# 分辨率：1920*1080, 字体设置为默认的11号
# Version: 1.0
###################

import os
import sys
import time

os.environ['DISPLAY'] = ':0'  # 设置此参数以使得在远程连接情况下运行该文件而不报错
testcasedir = os.path.dirname(__file__)  # 此变量表示 TestCase 目录的路径
kylinautoguidir = f"{testcasedir}/../../kylinautogui"  # 不同的文件..的个数可能不一样
rootdir = f"{testcasedir}/../../"  # 此变量表示 feishu 目录的路径

sys.path.append(kylinautoguidir)
sys.path.append(rootdir)

import libs.untils.functions as fn  # NOQA: E402
import libs.untils.paddleocr as ocr  # NOQA: E402
import libs.untils.composite as com  # NOQA: E402
import baidunetdisk.TestCase.test_create as tc  # NOQA: E402


def test_copy(file_name: str, myfile: str):

    # 新建所需文件
    tc.test_create(file_name=myfile)
    tc.test_create(file_name=file_name)

    # 选中被复制的文件
    com.click_string_in_window(file_name, fuzzy=True, option=3)
    time.sleep(3)

    # 选择复制到
    com.click_string_in_window('复制到', fuzzy=True)
    time.sleep(3)

    # 选择复制文件位置
    com.click_string_in_window(myfile, fuzzy=True)
    time.sleep(3)

    # 确认复制
    com.click_string_in_window('复制到此', fuzzy=True)
    time.sleep(3)

    # 打开文件位置
    com.click_string_in_window(myfile, fuzzy=True)
    time.sleep(3)

    # 验证复制文件成功
    pos = com.get_string_coordinate_in_window(file_name)
    assert pos != {}, '复制成功'
    print('百度网盘复制文件成功')


if __name__ == '__main__':

    # 启动应用
    res = fn.start_app('xdotool exec /opt/baidunetdisk/baidunetdisk')

    time.sleep(10)  # 等待窗口的响应

    test_copy(file_name="测试", myfile="银河")
