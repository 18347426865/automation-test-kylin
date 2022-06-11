#!/usr/bin/python3
# coding=utf-8

###################
# Author: Jianguo Yang
# Date: 2022-05-26
# Platform: Kylin Desktop V10 SP1
# Description: 测试百度网盘的登录功能
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
import libs.untils.paddleocr as ocr # NOQA: E402
import libs.untils.composite as com # NOQA: E402

def test_login(user: str,pwd: str):

    # 点击输入用户名
    com.click_string_in_window('手机号/用户名/邮箱', fuzzy=True)
    time.sleep(1)
    
    # 输入用户名
    fn.input_string(user)
    time.sleep(1)

    # 点击输入密码
    com.click_string_in_window('密码', fuzzy=True)
    time.sleep(1)
    
    # 输入密码
    fn.input_string(pwd)
    time.sleep(1)

    # 登录
    fn.key_input("Return")
    time.sleep(8)

    # 验证登录成功
    pos = com.get_string_coordinate_in_window('会员中心')
    assert pos != {}, '登录成功'
    print('百度网盘成功登录')


if __name__ == '__main__':

    # 创建截图文件的保存目录，
    fn.mkdir(f"{testcasedir}/../Outputs/screenshots")

    # 启动应用
    res = fn.start_app('xdotool exec /opt/baidunetdisk/baidunetdisk')

    time.sleep(5)  # 等待窗口的响应

    test_login(user="18347426865",pwd="111213yjg")