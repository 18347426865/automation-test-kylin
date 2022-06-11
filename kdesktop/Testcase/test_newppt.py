#!/usr/bin/python3
# coding=utf-8

###################
# Author: Ziyu Lu
# Date: 2022-05-17
# Platform: Kylin Desktop V10 SP1
# Description: 测试金山文档演示的新建
# Warning: 如果OCR服务崩溃，过往的测量数据只能用于特定的场景
# 分辨率：1920*1200, 字体设置为默认的11号
# Version: 1.0
###################


import os
import sys
import time

os.environ['DISPLAY'] = ':0'  # 设置此参数以使得在远程连接情况下运行该文件而不报错
sys.path.append('../../kylinautogui')
import libs.untils.functions as fn  # NOQA: E402
import libs.untils.composite as com  # NOQA: E402


def new_ppt(ppt_name: str='PPPPP') -> None:
    """
    新建一个演示
    :param1:文档名称
    """

    leftbar_region = [0, 0, 300, 720]
    # 点击“新建”坐标
    com.click_string_in_window_region(leftbar_region, '新建', fuzzy=True)
    time.sleep(4)

    # 点击演示坐标
    com.click_string_in_window_region(leftbar_region, '演示')
    time.sleep(4)

    region2 = [100, 100, 250, 200]
    # 点击空白演示文档坐标
    com.click_string_in_window_region(region2, '空白演示文档')
    time.sleep(8)

    region3 = [0, 43, 200, 150]
    com.click_string_in_window_region(region3, '演示', fuzzy=True)
    time.sleep(4)

    # 输入演示的标题
    fn.input_string(ppt_name)
    fn.key_input('Return')
    time.sleep(4)

    # 关闭标签页
    fn.key_input('ctrl+w')
    time.sleep(4)

    # 此时已经回到首页，刷新以正常显示新建文档的标题
    fn.key_input('F5')
    time.sleep(4)

    # 检测新建文档的标题
    pos = com.get_string_coordinate_in_window(ppt_name, fuzzy=True)
    assert pos != {}, f'未检测到{ppt_name}'

    print(f'{sys._getframe().f_code}  (*^▽^*)测试完成！\n')


def prepare():
    """
    准备工作
    """
    # 创建截图文件的保存目录，
    fn.mkdir("../Outputs/screenshots")

    # 启动应用
    fn.start_app(
        'xdotool exec /opt/apps/cn.kdocs.kdesktop/files/bin/kdesktop')
    time.sleep(4)

    # 获取窗口id
    window_id = fn.get_active_window_id()

    # 提前设置窗口位置和大小，要不然ocr识别不到
    fn.move_window(window_id, 0, 0)
    fn._set_window_size(window_id, 1200, 900)


    fn.click_location(50, 30)  # 点击首页标签
    time.sleep(4)


if __name__ == '__main__':
    prepare()

    new_ppt('PPPPP')
