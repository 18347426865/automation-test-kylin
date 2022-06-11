#!/usr/bin/python3
# coding=utf-8

###################
# Author: Yanrui Hu
# Date: 2022-05-25
# Platform: Kylin Desktop V10 SP1
# Description: 测试WPS Office的表格 (et) 新建表格文件
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


def create_file(newfilename: str, inputdata: str):
    """
    新建一个表格文件
    Parameters:
     param1: filename: 文件名字,建议不要使用中文!!!
     param2: inputdata: 表格的内容, 建议不要使用中文!!!
    Returns: None
    """

    # 下面新建一个表格文件
    # 点击"新建"的坐标
    com.click_string_in_window("新建", fuzzy=True)
    time.sleep(2)

    # 录入一些数据
    fn.paste_string(inputdata)
    time.sleep(2)

    # 按下 ctrl + S 保存文件
    fn.key_input('ctrl+s')
    fn.key_input('ctrl+s')
    time.sleep(2)

    # 更改文件名
    fn.key_input('ctrl+a BackSpace')
    time.sleep(1)
    fn.paste_string(newfilename)
    time.sleep(2)

    # 按下 回车 键
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

    create_file(newfilename="TESTFILE.et", inputdata='helloworld')
