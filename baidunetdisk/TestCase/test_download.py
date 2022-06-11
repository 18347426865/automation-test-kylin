#!/usr/bin/python3
# coding=utf-8

###################
# Author: Jianguo Yang
# Date: 2022-05-29
# Platform: Kylin Desktop V10 SP1
# Description: 测试百度网盘的彻底删除文件功能
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


def test_download(file_name: str):

    # 选中要下载的文件，右键
    com.click_string_in_window(file_name, fuzzy=True, option=3)
    time.sleep(3)

    # 点击下载
    com.click_string_in_window('下载', fuzzy=True)
    time.sleep(4)

    # 确定下载
    com.click_string_in_window('确定', fuzzy=True)
    time.sleep(3)

    # 查看传输结果
    com.click_string_in_window('传输', fuzzy=True)
    time.sleep(3)

    # 点击传输完成
    com.click_string_in_window('传输完成', fuzzy=True)
    time.sleep(3)

    # 验证下载文件成功
    pos = com.get_string_coordinate_in_window(file_name)
    assert pos != {}, '下载成功'
    print('百度网盘下载文件成功')


if __name__ == '__main__':

    # 启动应用
    res = fn.start_app('xdotool exec /opt/baidunetdisk/baidunetdisk')

    time.sleep(5)  # 等待窗口的响应

    test_download(file_name="mytest")
