#!/usr/bin/python3
# coding=utf-8

###################
# Author: Yanrui Hu
# Date: 2022-05-30
# Platform: Kylin Desktop V10 SP1
# Description: 测试飞书的删除群聊
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



def delete_group(group_name: str) -> None:
    """
    删除一个飞书群聊
     param1: 群聊名称
    """
    # 点击消息栏
    com.click_string_in_window_region(CN.sidebar_region, '消息')
    time.sleep(2)

    # 点击群聊
    com.click_string_in_window_region(CN.listbar_region, group_name)
    time.sleep(2)

    # 点击设置
    fn.click_location(*CN.setting_cor)
    time.sleep(2)

    # 在设置区域点击"解散群组"
    com.click_string_in_window_region(CN.setting_region, '解散群组')
    time.sleep(2)

    # 在窗口上点击"解散"
    com.click_string_in_window('解散')
    time.sleep(2)

    print(f'{sys._getframe().f_code}  (*^▽^*)测试完成！\n')


if __name__ == '__main__':
    # 创建截图文件的保存目录，
    fn.mkdir(f"{testcasedir}/../Outputs/screenshots")

    # 启动应用
    fn.start_app('xdotool exec /usr/bin/bytedance-feishu-stable')
    time.sleep(5)  # 等待窗口的响应

    delete_group(group_name='测试专用')
