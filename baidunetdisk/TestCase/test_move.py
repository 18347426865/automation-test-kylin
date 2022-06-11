#!/usr/bin/python3
# coding=utf-8

###################
# Author: Jianguo Yang
# Date: 2022-05-26
# Platform: Kylin Desktop V10 SP1
# Description: 测试百度网盘的移动文件功能
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


def test_move(file_name: str, myfile: str, path: str):

    # 新建所需移动的文件
    tc.test_create(myfile)

    # 选中要移动的文件
    com.click_string_in_window(file_name, fuzzy=True, option=3)
    time.sleep(3)

    # 选择移动
    com.click_string_in_window('移动到', fuzzy=True)
    time.sleep(4)

    # 选择要移动的位置
    com.click_string_in_window(path, fuzzy=True)
    time.sleep(3)

    # 选择要移动的位置
    com.click_string_in_window(myfile, fuzzy=True)
    time.sleep(3)

    # 点击移动
    com.click_string_in_window('移动到此', fuzzy=True)
    time.sleep(3)

    # 打开英语目录
    com.click_string_in_window(myfile, fuzzy=True)
    time.sleep(3)

    # 验证文件移动成功
    pos = com.get_string_coordinate_in_window(file_name)
    assert pos != {}, '移动成功'
    print('百度网盘文件移动成功')


if __name__ == '__main__':

    # 启动应用
    res = fn.start_app('xdotool exec /opt/baidunetdisk/baidunetdisk')

    time.sleep(5)  # 等待窗口的响应

    test_move(file_name="测试", myfile="hlmy", path="银河")
