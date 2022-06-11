#!/usr/bin/python3
# coding=utf-8

###################
# Author: Yanrui Hu
# Date: 2022-05-30
# Platform: Kylin Desktop V10 SP1
# Description: 测试飞书顶部状态栏的搜索（search）功能
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


def search(content: str, type_: str) -> None:
    """
    搜索
     param1: 搜索内容
    """
    # 点击搜索栏
    com.click_string_in_window_region(CN.topbar_region, '搜索', fuzzy=True)
    time.sleep(2)

    # 输入搜索内容
    fn.paste_string(content)
    time.sleep(2)

    #  点击类别
    com.click_string_in_window_region(CN.search_bar_region, type_)
    time.sleep(2)

    # 检测搜索结果
    count = com.get_string_count_in_window_region(
        CN.search_result_region, content, fuzzy=True)
    assert count != 0, f"{content} 的搜索结果为空"

    # 按下回车
    fn.key_input('Return')
    time.sleep(2)

    print(f'{sys._getframe().f_code}  (*^▽^*)测试完成！\n')


if __name__ == '__main__':
    # 创建截图文件的保存目录，
    fn.mkdir(f"{testcasedir}/../Outputs/screenshots")

    # 启动应用
    fn.start_app('xdotool exec /usr/bin/bytedance-feishu-stable')
    time.sleep(5)  # 等待窗口的响应

    search(content='测试专用', type_='群组')
