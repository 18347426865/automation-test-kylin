#!/usr/bin/python3
# coding=utf-8

###################
# Author: Yanrui Hu
# Date: 2022-05-27
# Platform: Kylin Desktop V10 SP1
# Description: 测试WPS Office的表格 (et): 已有文件另存为(save as)
# Warning: 如果OCR服务崩溃，过往的测量数据只能用于特定的场景
# 分辨率：1920*1080, 字体设置为默认的11号
# Version: 1.0
###################

import os
import sys
import time

os.environ['DISPLAY'] = ':0'  # 设置此参数以使得在远程连接情况下运行该文件而不报错
testcasedir = os.path.dirname(__file__)  # 此变量表示 TestCase 目录的路径
kylinautoguidir = f"{testcasedir}/../../../kylinautogui"  # 不同的文件..的个数可能不一样
sys.path.append(kylinautoguidir)

import libs.untils.functions as fn   # NOQA: E402
import libs.untils.composite as com  # NOQA: E402


def save_as_file(filename: str, newfilename: str):
    """
    对已有文件另存为
    Parameters:
     param1: 已有的文件名
     param2: 另存为的文件名
    Returns: None
    """

    # 下面将一个已有的文件另存为其他格式
    # 点击"我的文档"
    com.click_string_in_window('我的文档')
    time.sleep(2)

    # 左键双击文件名, 可以打开此文件
    com.click_string_in_window(filename, repeat=2)
    time.sleep(2)

    # 按下 F12 使用 另存为PDF 功能
    fn.key_input('F12')
    time.sleep(2)

    # 在弹出的窗口中输入新的文件名并保存
    fn.key_input('ctrl+a BackSpace')
    fn.paste_string(newfilename)
    time.sleep(2)
    fn.key_input('Return')
    time.sleep(2)

    # 检测在文档文件夹下是否有目标文件存在
    res = os.popen(f'ls ~/文档/ | grep {newfilename}').read()
    assert res != '', f'文件{newfilename} 创建失败'

    print(f'{sys._getframe().f_code}  (*^▽^*)测试完成！\n')


if __name__ == '__main__':
    # 创建截图文件的保存目录，
    fn.mkdir(f"{testcasedir}/../Outputs/screenshots")

    # 启动应用
    res = fn.start_app('xdotool exec /usr/bin/et')
    assert res == True, 'WPS表格 启动失败'
    time.sleep(5)  # 等待窗口的响应

    save_as_file(filename="TESTFILE.et", newfilename='TESTFILE.xlsx')
