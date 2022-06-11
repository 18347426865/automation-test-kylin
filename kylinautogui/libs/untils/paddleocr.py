#!/usr/bin/python3
# coding=utf-8

###################
# Author: Yanrui Hu
# Date: 2022-05-17
# Description: 自己设置的OCR方法
# Warning: 如果try中的OCR服务崩溃, 需要自己在本地使用hub命令启动一个OCR服务
# Version: 1.0
###################

import requests
import cv2
import json
import base64
import sys


def cv2_to_base64(image):
    data = cv2.imencode('.jpg', image)[1]
    return base64.b64encode(data.tobytes()).decode('utf8')


def ocr_img(img_path: str) -> tuple[dict,list]:
    """
    获取OCR的识别结果
    Param1: 传入需要识别的图片路径
    Returns: 返回识别结果(dict形式), eg: {'文字1': [x, y, w, h], '文字2': [x, y, w, h]}

    """
    img_data = {'images': [cv2_to_base64(cv2.imread(img_path))]}
    headers = {"Content-type": "application/json"}
    data = None
    # 发送HTTP请求
    try:
        # 如果是在学校的同学, 连接校园网即可使用base_url提供的服务
        print("正在尝试使用校园网的OCR服务......")
        base_url = "http://10.11.55.80:8866"
        url = f"{base_url}/predict/chinese_ocr_db_crnn_mobile"  # 修改ip地址为服务器地址
        r = requests.post(url=url, headers=headers, data=json.dumps(img_data))
        data = r.json()["results"][0]["data"]
    except:
        # 如果无法使用上面的服务,可以自己在本地跑一个
        print("使用校园网的服务失败! 尝试使用本地的OCR服务......", file=sys.stderr)
        base_url = "http://127.0.0.1:8866"
        url = f"{base_url}/predict/chinese_ocr_db_crnn_mobile"  # 修改ip地址为服务器地址
        r = requests.post(url=url, headers=headers, data=json.dumps(img_data))
        data = r.json()["results"][0]["data"]

    assert data is not None, 'data为None'

    # 下面开始获取文本框的中心坐标以及文本border的尺寸,并于文字本身进行关联,保存在dict中
    text_coordinates = {}
    for dic in data:
        assert type(dic) == dict, '结果与预期不符合'
        key: str = dic.get('text')
        val: list = dic.get('text_box_position')

        # val是一个双层list, eg: [[26, 134], [50, 134], [50, 159], [26, 159]]
        # 含义是 text_box 的四个角的坐标
        center_position: list = [0, 0]
        center_position[0] = (val[0][0] + val[1][0]) // 2
        center_position[1] = (val[0][1] + val[2][1]) // 2
        border_size: list = [0, 0]
        border_size[0] = val[1][0] - val[0][0]
        border_size[1] = val[2][1] - val[0][1]
        text_coordinates[key] = center_position + border_size

    strlist = [item['text'] for item in data]

    return text_coordinates, strlist


if __name__ == '__main__':
    # 这部分只是用来测试 OCR接口的
    img_path = "/home/huyanrui/test.png"
    print(ocr_img(img_path))
    print()
    # print(ocr_img(img_path)[0])
    # print()
    # print(ocr_img(img_path)[1])
