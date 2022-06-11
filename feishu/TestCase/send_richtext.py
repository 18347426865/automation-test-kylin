#!/usr/bin/python3
# coding=utf-8

###################
# Author: Yanrui Hu
# Date: 2022-05-30
# Platform: Kylin Desktop V10 SP1
# Description: 测试飞书的发送富文本消息
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


def send_richtext(chat_name: str, title: str, text: str) -> None:
    """
    发送富文本消息
     param1: 聊天名称
     param2: 标题
     param3: 正文文本
    """
    # 点击消息栏
    com.click_string_in_window_region(CN.sidebar_region, '消息')
    time.sleep(2)

    # 点击群聊
    com.click_string_in_window_region(CN.listbar_region, chat_name)
    time.sleep(2)

    # 点击富文本输入按钮
    fn.click_location(*CN.richtext_cor)
    time.sleep(2)

    # 输入富文本的标题
    fn.paste_string(title)
    time.sleep(2)
    fn.key_input('Return')
    time.sleep(1)

    # 输入富文本的正文
    fn.paste_string(text)
    time.sleep(2)
    fn.key_input('Return')
    time.sleep(1)

    # 点击发送按钮
    com.click_string_in_window_region(CN.richtext_region, '发送')
    time.sleep(2)

    # 在聊天区域验证消息是否发送成功
    count = com.get_string_count_in_window_region(CN.chat_region, title)
    assert count != 0, '富文本消息标题发送失败'
    time.sleep(2)
    count = com.get_string_count_in_window_region(CN.chat_region, text)
    assert count != 0, '富文本消息正文发送失败'
    time.sleep(2)

    print(f'{sys._getframe().f_code}  (*^▽^*)测试完成！\n')


if __name__ == '__main__':
    # 创建截图文件的保存目录，
    fn.mkdir(f"{testcasedir}/../Outputs/screenshots")

    # 启动应用
    fn.start_app('xdotool exec /usr/bin/bytedance-feishu-stable')
    time.sleep(5)  # 等待窗口的响应

    send_richtext(chat_name='测试专用', title='测试标题', text='测试正文')
