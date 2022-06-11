#!/usr/bin/python3
# coding=utf-8

###################
# Author: Yanrui Hu
# Date: 2022-05-30
# Platform: Kylin Desktop V10 SP1
# Description: 测试飞书的创建群聊
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


def create_group(group_name: str) -> None:
    """
    创建一个飞书群聊
     param1: 群聊名称
    """

    com.click_string_in_window_region(CN.sidebar_region, '通讯录')
    time.sleep(2)

    com.click_string_in_window_region(CN.listbar_region, '我的群组')
    time.sleep(2)

    com.click_string_in_window_region(
        CN.titlebar_region, string='创建群组', fuzzy=True)
    time.sleep(2)

    # 输入群组名称
    fn.paste_string(group_name)
    time.sleep(2)

    fn.key_input('ctrl+Return')
    time.sleep(5)

    # 判断群组名称是否显示在群组列表中
    res = com.get_string_coordinate_in_window_region(CN.listbar_region, group_name)
    assert res != {}, f'群组列表中没有找到群组"{group_name}"'

    print(f'{sys._getframe().f_code}  (*^▽^*)测试完成！\n')


def just_test_and_verify_XXX_region():
    """
    此函数仅仅用于测试 XXX_region 的有效性!
    """
    res = com.get_string_coordinate_in_window_region(CN.topbar_region, '搜索', fuzzy=True)
    assert res != {}, f"没有找到搜索按钮"
    time.sleep(2)

    count = com.get_string_count_in_window_region(CN.topbar_region, '搜索', fuzzy=True)
    assert count == 1, f'搜索按钮的数量不为1, 实际为{count}'
    time.sleep(2)


if __name__ == '__main__':
    # 创建截图文件的保存目录，
    fn.mkdir(f"{testcasedir}/../Outputs/screenshots")

    # 启动应用
    fn.start_app('xdotool exec /usr/bin/bytedance-feishu-stable')
    time.sleep(5)  # 等待窗口的响应

    create_group(group_name='测试专用')
