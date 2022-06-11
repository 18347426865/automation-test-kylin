#!/usr/bin/python3
# coding=utf-8

###################
# Author: Yanrui Hu
# Date: 2022-06-04
# Platform: Kylin Desktop V10 SP1
# Description: 测试飞书的发送图片功能
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


def send_image(chat_name: str, img_path: str) -> None:
    """
    发送图片
     param1: 聊天名称
     param2: 图片路径
    """
    # 点击消息栏
    com.click_string_in_window_region(CN.sidebar_region, '消息')
    time.sleep(2)

    # 点击群聊
    com.click_string_in_window_region(CN.listbar_region, chat_name)
    time.sleep(2)

    # 点击消息输入框内部的展开图标
    fn.click_location(*CN.unfold_cor)
    time.sleep(2)

    # 点击在弹出的展开区域点击"图片/视频"按钮
    com.click_string_in_window_region(CN.unfold_region, '图片/视频', fuzzy=True)
    time.sleep(2)

    # 在弹出的窗口中输入图片的路径
    fn.paste_string(img_path)
    time.sleep(2)

    # 选择图片
    fn.key_input('Return')
    time.sleep(2)

    # 回车触发发送按钮
    fn.key_input('Return')
    time.sleep(2)


if __name__ == '__main__':
    # 创建截图文件的保存目录，
    fn.mkdir(f"{testcasedir}/../Outputs/screenshots")

    # 启动应用
    fn.start_app('xdotool exec /usr/bin/bytedance-feishu-stable')
    time.sleep(5)  # 等待窗口的响应

    # 发送文件
    send_image('测试专用', '~/TEST/test.png')
