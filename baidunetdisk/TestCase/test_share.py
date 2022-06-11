#!/usr/bin/python3
# coding=utf-8

###################
# Author: Jianguo Yang
# Date: 2022-05-26
# Platform: Kylin Desktop V10 SP1
# Description: 测试百度网盘的文件分享功能
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


def test_share(file_name: str):

    # 右键选中要分享的文件
    com.click_string_in_window(file_name, fuzzy=True, option=3)
    time.sleep(3)

    # 点击分享
    com.click_string_in_window('分享', fuzzy=True)
    time.sleep(3)

    # 创建分享链接
    com.click_string_in_window('创建链接', fuzzy=True)
    time.sleep(3)

    # 复制文件二维码
    com.click_string_in_window('复制二维码', fuzzy=True)
    time.sleep(3)

    # 验证分享成功
    pos = com.get_string_coordinate_in_window('复制二维码')
    assert pos != {}, '分享成功'
    print('百度网盘文件分享成功')

    # 关闭应用
    res = fn.close_current_window()
    assert res == 0, '关闭应用失败'


if __name__ == '__main__':

    # 启动应用
    res = fn.start_app('xdotool exec /opt/baidunetdisk/baidunetdisk')

    time.sleep(5)  # 等待窗口的响应

    test_share(file_name="mysql")
