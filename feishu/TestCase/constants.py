#!/usr/bin/python3
# coding=utf-8

###################
# Author: Yanrui Hu
# Date: 2022-05-30
# Platform: Kylin Desktop V10 SP1
# Description: 提供有关飞书界面的诸多位置常量
# Warning: 如果OCR服务崩溃，过往的测量数据只能用于特定的场景
# 分辨率：1920*1080, 字体设置为默认的11号
# Version: 1.0
###################


topbar_region = [380, -50, 450, 100]    # 顶部栏
sidebar_region = [-80, 0, 160, 600]     # 左侧栏
listbar_region = [105, 110, 200, 455]   # 列表栏
titlebar_region = [410, 40, 800, 100]   # 标题栏
chat_region = [450, 110, 700, 555]      # 聊天区域
pin_region = [60, 0, 355, 130]       # 置顶聊天图标出现的区域

setting_cor = (1180, 330)               # 群聊设置按钮的坐标
setting_region = [800, 45, 360, 690]    # 群聊设置区域

unfold_cor = (1074, 688)                  # 群聊右下角展开按钮的坐标
unfold_region = [1010, 300, 150, 370]     # 群聊右下角展开按钮的区域

search_bar_region = [114, 66, 700, 150]     # 搜索框的区域
search_result_region = [114, 66, 970, 575]  # 搜索结果区域

input_cor = (500, 688)                   # 输入框的坐标
input_region = [415, 630, 720, 100]      # 输入框的区域

richtext_cor = (1105, 688)                  # 富文本消息的坐标
richtext_region = [415, 120, 735, 615]      # 富文本编辑区域

sendfile_region = [395, 230, 420, 270]      # 发送文件确认弹窗区域
