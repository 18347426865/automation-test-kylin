#!/usr/bin/python3
# coding=utf-8

###################
# Author: Jianguo Yang
# Date: 2022-05-17
# Platform: Kylin Desktop V10 SP1
# Description: 通用测试样例，测试应用的安装
# Warning: 如果OCR服务崩溃，过往的测量数据只保证在特定的分辨率和字号设置下生效
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

import libs.untils.functions as fn   # NOQA: E402
import libs.untils.paddleocr as ocr  # NOQA: E402
import libs.untils.composite as com  # NOQA: E402


wpsapp = {'name': 'WPS 办公软件', 'search_name': 'WPSbgrj'}
baidunetdisk = {'name': '百度网盘', 'search_name': 'bdwp'}
kdesktop = {'name': '金山文档', 'search_name': 'jswd'}
feishu = {'name': '飞书', 'search_name': 'feishu'}
qaxsafe = {'name': '奇安信网神终端安全', 'search_name': 'qaxsafe'}


def install_app(app: dict) -> None:
    """
    安装应用
    Parameters:
     param1 app_name: 应用名称
    Return: None
    """
    # 创建截图文件的保存目录，
    fn.mkdir(f"{testcasedir}/../Outputs/screenshots")

    # 启动软件商店
    res = fn.start_app('xdotool exec /usr/bin/kylin-software-center')
    assert res == True, '软件商店 启动失败'

    time.sleep(5)  # 等待窗口的响应
    fn.get_active_window_info()

    com.click_string_in_window('请输入要搜索的软件', fuzzy=True)
    time.sleep(1)

    # 输入搜索内容
    fn.input_string(f"{app['search_name']}")
    time.sleep(1)

    # 按下回车键
    fn.key_input('Return')
    time.sleep(3)

    pos = com.screenshot_window_and_ocr(app['name'].split(' ')[0], fuzzy=True)
    # split(' ')[0]是为了防止搜索的应用名称中包含空格但是识别结果不包含空格导致搜索失败的情况
    # 例如， 想要搜索"WPS 办公软件"，但是识别结果是"WPS办公软件",
    # 这时候就需要用split(' ')[0]来获取"WPS", 同时需要使用模糊搜索
    # "WPS" 包含在"WPS办公软件"中, 模糊搜索会认为搜到了结果

    assert pos != {}, f'获取 "{app["name"]}" 的坐标失败'
    print(f'{app["name"]} 的坐标是{pos}')

    region = [pos[0] + 50, pos[1] + 10, 100, 100]
    # region 表示一个区域[x_pos, y_pos, width, height],
    time.sleep(1)
    try:
        com.click_string_in_window_region(region, string="下载")
    except:
        time.sleep(1)
        res = com.screenshot_in_window_region_and_ocr(region, string="打开")
        assert res != {}, '未识别到打开按钮或者下载按钮, 可能是截图区域有问题'
        print(f"{app['name']} 不用安装, 应用已存在!")


if __name__ == '__main__':

    install_app(qaxsafe)
