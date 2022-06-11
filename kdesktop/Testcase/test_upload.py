#!/usr/bin/python3
# coding=utf-8

###################
# Author: Ziyu Lu
# Date: 2022-05-17
# Platform: Kylin Desktop V10 SP1
# Description: 测试金山文档文档的上传
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


def upload(upfile_name) -> None:
    """
    测试金山文档上传文件功能
    注意：为了测试的通用性，在上传文件之前会先在桌面创建一个空白文件
    :param upload_name: 上传文件名
    """
    # 创建上传文件
    address = f'/home/{os.getlogin()}/桌面/{upfile_name}'
    os.system(f'touch {address}')

    # 有可能 新建按钮 已经被点击，所以
    fn.key_input('Escape')
    time.sleep(4)

    # 点击 新建 按钮
    leftbar_region = [0, 0, 300, 720]
    com.click_string_in_window_region(leftbar_region, '新建', fuzzy=True)
    time.sleep(4)

    # 点击 上传 按钮
    com.click_string_in_window_region(leftbar_region, '上传')
    time.sleep(4)

    # 选择 文件 选项
    upchioce_region = [180, 575, 250, 200]
    com.click_string_in_window_region(upchioce_region, '文件')
    time.sleep(4)

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
    time.sleep(4)

    # 检查是否成功
    pos = com.get_string_coordinate_in_window(upfile_name, fuzzy=True)
    assert pos != {}, f'未检测到{upfile_name}'

    fn.close_current_window()
    time.sleep(4)

    # 点击标题栏任意位置，用于关闭弹窗
    fn.click_location(10, 10)

    # 删除桌面的文件，算是做一些善后工作
    os.system(f'rm -f {address}')

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

    upload(upfile_name='KKTEST.txt')
