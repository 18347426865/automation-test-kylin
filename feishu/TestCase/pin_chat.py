#!/usr/bin/python3
# coding=utf-8

###################
# Author: Yanrui Hu
# Date: 2022-05-30
# Platform: Kylin Desktop V10 SP1
# Description: 测试飞书的置顶聊天
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
rootdir = f"{testcasedir}/../../"  # 此变量表示 项目根目录的路径

sys.path.append(kylinautoguidir)
sys.path.append(rootdir)

import libs.untils.functions as fn   # NOQA: E402
import libs.untils.paddleocr as ocr  # NOQA: E402
import libs.untils.composite as com  # NOQA: E402
import feishu.TestCase.constants as CN               # NOQA: E402


def pin_group(chat_name: str) -> None:
    """
    置顶一个飞书聊天
     param1: 聊天名称
    """
    # 点击消息栏
    com.click_string_in_window_region(CN.sidebar_region, '消息')
    time.sleep(2)

    # 点击聊天
    com.click_string_in_window_region(CN.listbar_region, chat_name, option=3)
    time.sleep(2)

    # 点击"添加到置顶"
    com.click_string_in_window_region(CN.listbar_region, '添加到置顶', fuzzy=True)
    time.sleep(2)

    # 检查置顶聊天是否成功
    count = com.get_string_count_in_window_region(
        CN.pin_region, chat_name, fuzzy=True)
    assert count != 0, f"置顶聊天失败，'{chat_name}'不在置顶列表中"

    print(f'{sys._getframe().f_code}  (*^▽^*)测试完成！\n')


def unpin_group(chat_name: str) -> None:
    """
    取消置顶一个飞书聊天
     param1: 聊天名称
    """
    # 点击消息栏
    com.click_string_in_window_region(CN.sidebar_region, '消息')
    time.sleep(2)

    # 点击聊天
    com.click_string_in_window_region(CN.listbar_region, chat_name, option=3)
    time.sleep(2)

    # 点击"取消置顶"
    com.click_string_in_window_region(CN.listbar_region, '取消置顶', fuzzy=True)
    time.sleep(2)

    # 检查置顶聊天是否成功
    count = com.get_string_count_in_window_region(
        CN.pin_region, chat_name, fuzzy=True)
    assert count == 0, f"取消置顶聊天失败，'{chat_name}'仍在置顶列表中"

    print(f'{sys._getframe().f_code}  (*^▽^*)测试完成！\n')


if __name__ == '__main__':
    # 创建截图文件的保存目录，
    fn.mkdir(f"{testcasedir}/../Outputs/screenshots")

    # 启动应用
    fn.start_app('xdotool exec /usr/bin/bytedance-feishu-stable')
    time.sleep(5)  # 等待窗口的响应

    pin_group(chat_name='测试专用')
    unpin_group(chat_name='测试专用')
