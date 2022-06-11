#!/usr/bin/python3
# coding=utf-8

###################
# Author: Jianguo Yang
# Date: 2022-05-26
# Platform: Kylin Desktop V10 SP1
# Description: 测试百度网盘的文件上传功能，将本地文件上传
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


def test_upload(upfile_name: str):

    # 创建上传文件
    address = f'/home/{os.getlogin()}/桌面/{upfile_name}'
    os.system(f'touch {address}')

    # 点击上传
    com.click_string_in_window('上传', fuzzy=True)
    time.sleep(3)

    # 选择上传文件夹
    com.click_string_in_window('上传文件', fuzzy=True)
    time.sleep(3)

    # 点击桌面
    dirbar_region = [0, 0, 200, 650]
    com.click_string_in_window_region(dirbar_region, '口桌面', fuzzy=True)
    time.sleep(4)

    # 点击待上传文件
    filelist_region = [200, 0, 400, 650]
    com.click_string_in_window_region(filelist_region, upfile_name)
    time.sleep(4)

    # 回车确定
    fn.key_input('Return')
    # time.sleep(4)

    # # 上传到百度网盘主目录下
    # com.click_string_in_window('存入百度网盘', fuzzy=True)
    time.sleep(10)

    # 检查是否成功
    pos = com.get_string_coordinate_in_window(upfile_name, fuzzy=True)
    assert pos != {}, f'未检测到{upfile_name}'

    print('百度网盘上传文件成功')

    # 删除桌面的文件，算是做一些善后工作
    os.system(f'rm -f {address}')



if __name__ == '__main__':

    # 启动应用
    res = fn.start_app('xdotool exec /opt/baidunetdisk/baidunetdisk')

    time.sleep(5)  # 等待窗口的响应

    test_upload(upfile_name="UPLOAD")
