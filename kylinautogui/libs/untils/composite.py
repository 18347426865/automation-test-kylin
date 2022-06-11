#!/usr/bin/python3
# coding=utf-8

###################
# Author: Yanrui Hu
# Date: 2022-05-18
# Description: 组装了一些方法, 可以更加方便的进行OCR识别和点击
# Warning: fn.get_coordinate() 的返回值是{} 或者是 "传参 coordinate_dict的value的类型"
#       我实现的ocr_img() 方法返回的虽然也是字典
#       但是是一个"键类型为str 但是值类型为list的dict",
#       与kylin的 get_all_coordinates() 返回的类型不完全一样
#       所以return 的pos 是 {} 或者是一个 list 类型的对象
#       也就是说, 识别成功的话,返回的形式是 [x, y, w, h], eg: [100, 200, 300, 400]
#       识别失败的话, 返回的形式是 {}
#       kylin的返回值一直都是dict, eg: {'width': 100, 'height': 500}
# Version: 1.0
###################

import sys
import os

os.environ['DISPLAY'] = ':0'  # 设置此参数以使得在远程连接情况下运行该文件而不报错
sys.path.append(os.path.dirname(__file__))  # 将当前文件所在目录添加到搜索路径中

import functions as fn   # NOQA: E402
import paddleocr as ocr  # NOQA: E402


def ocr_img_and_get_coordinate(img_path: str, string: str, fuzzy: bool = False) -> list:
    """
    将图片进行OCR识别, 返回想要定位的文本的中心坐标以及文本border的尺寸 [x, y, w, h]
    Parameters:
     param1: 需要识别的图片路径
     param2: 需要定位的文本
     param3: 是否使用模糊匹配, 默认为False
    Returns: 是否成功识别, 如果成功返回 list, 表示文字中心的坐标 [x, y, w, h] (坐标参考系是传入的图片);
                           如果失败返回{}
    """
    text_coordinates = ocr.ocr_img(img_path)[0]
    print(f'OCR result is {text_coordinates}')
    pos = fn.get_coordinate(string, text_coordinates, fuzzy=fuzzy)
    return pos


def ocr_img_and_get_string_count(img_path: str, string: str, fuzzy: bool = False) -> int:
    """
    将图片进行OCR识别, 获取给定字符串在图片中出现的次数
    Parameters:
     param1: 需要识别的图片路径
     param2: 需要识别的字符串
     param3: 是否使用模糊匹配, 默认为False
    Returns: 识别出给定字符串的个数
    """
    strlist: list = ocr.ocr_img(img_path)[1]
    print(f'OCR result is {strlist}')
    # count = 0

    # if fuzzy:
    #     for item in strlist:
    #         if string in item:
    #             count += 1
    # else:
    #     for item in strlist:
    #         if string == item:
    #             count += 1

    # 下面使用 map 和 lambda 实现与上面相同结果的count的计算
    m1 = map(lambda x: 1 if string in x else 0, strlist)
    m2 = map(lambda x: 1 if string == x else 0, strlist)
    count: int = sum(list(m1)) if fuzzy else sum(list(m2))
    return count


def screenshot_window_and_ocr(string: str, fuzzy: bool = False) -> list:
    """
    截图当前窗口, 并进行OCR识别, 返回想要定位的文本的中心坐标以及文本border的尺寸 [x, y, w, h]
    Parameters:
     param1: 需要定位的文本
     param2: 是否使用模糊匹配, 默认为False
    Returns: 是否成功识别, 如果成功返回 list, 表示文字中心的坐标 [x, y, w, h] (坐标参考系是传入的图片);
                           如果失败返回{}
    """
    img_path = fn.screenshot_window(
        filename='%Y-%m-%d_$wx$h.png',
        filepath='../Outputs/screenshots')
    print(f'\n\tSaved screenshot to {img_path}')

    pos = ocr_img_and_get_coordinate(img_path, string, fuzzy=fuzzy)
    return pos


def get_string_coordinate_in_window(string: str, fuzzy: bool = False) -> list:
    """
    此函数是 `screenshot_window_and_ocr` 的别名
    截图当前窗口, 并进行OCR识别, 返回想要定位的文本的中心坐标以及文本border的尺寸 [x, y, w, h]
    Parameters:
     param1: 需要定位的文本
     param2: 是否使用模糊匹配, 默认为False
    Returns: 是否成功识别, 如果成功返回 list, 表示文字中心的坐标 [x, y, w, h] (坐标参考系是传入的图片);
                           如果失败返回{}
    """
    return screenshot_window_and_ocr(string, fuzzy=fuzzy)


def screenshot_region_and_ocr(region: list, string: str, fuzzy: bool = False) -> list:
    """
    截图指定区域, 并进行OCR识别, 返回想要定位的文本的中心坐标以及文本border的尺寸 [x, y, w, h]
    Parameters:
     param1: 区域坐标, 是一个列表 [x_pos, y_pos, width, height]
            (x_pos, y_pos都是相对于整个屏幕左上角的坐标)
     param2: 需要定位的文本
     param3: 是否使用模糊匹配, 默认为False
    Returns: 是否成功识别, 如果成功返回 list, 表示文字中心的坐标 [x, y, w, h] (坐标参考系是传入的图片);
                           如果失败返回{}
    """
    img_path = fn.screenshot_custom(region=region,
                                    filepath='../Outputs/screenshots')
    print(f'\n\tSaved screenshot to {img_path}')

    pos = ocr_img_and_get_coordinate(img_path, string, fuzzy=fuzzy)
    return pos


def get_string_coordinate_in_region(region: list, string: str, fuzzy: bool = False) -> list:
    """
    此函数是 `screenshot_region_and_ocr` 的别名
    截图指定区域, 并进行OCR识别, 返回想要定位的文本的中心坐标以及文本border的尺寸 [x, y, w, h]
    Parameters:
     param1: 区域坐标, 是一个列表 [x_pos, y_pos, width, height]
            (x_pos, y_pos都是相对于整个屏幕左上角的坐标)
     param2: 需要定位的文本
     param3: 是否使用模糊匹配, 默认为False
    Returns: 是否成功识别, 如果成功返回 list, 表示文字中心的坐标 [x, y, w, h] (坐标参考系是传入的图片);
                           如果失败返回{}
    """
    return screenshot_region_and_ocr(region, string, fuzzy=fuzzy)


def screenshot_in_window_region_and_ocr(inner_region: list, string: str, fuzzy: bool = False) -> list:
    """
    截取指定区域, 并进行OCR识别, 获取想要定位的文本的中心坐标以及文本border的尺寸 [x, y, w, h]
    Parameters:
     param1: 区域坐标, 是一个列表 [x_pos, y_pos, width, height]
            (x_pos, y_pos都是相对于窗口左上角的坐标)
     param2: 需要定位的文本
     param3: 是否使用模糊匹配, 默认为False
    Returns: 是否成功识别, 如果成功返回 list, 表示文字中心的坐标 [x, y, w, h] (坐标参考系是传入的图片);
                           如果失败返回{}
    """
    window_pos = fn.get_active_window_position()
    x_pos = window_pos[0] + inner_region[0]
    y_pos = window_pos[1] + inner_region[1]
    region = [x_pos, y_pos, inner_region[2], inner_region[3]]

    return screenshot_region_and_ocr(region, string, fuzzy)


def get_string_coordinate_in_window_region(inner_region: list, string: str, fuzzy: bool = False) -> list:
    """
    此函数是 `screenshot_in_window_region_and_ocr` 的别名
    截取指定区域, 并进行OCR识别, 获取想要定位的文本的中心坐标以及文本border的尺寸 [x, y, w, h]
    Parameters:
     param1: 区域坐标, 是一个列表 [x_pos, y_pos, width, height]
            (x_pos, y_pos都是相对于窗口左上角的坐标)
     param2: 需要定位的文本
     param3: 是否使用模糊匹配, 默认为False
    Returns: 是否成功识别, 如果成功返回 list, 表示文字中心的坐标 [x, y, w, h] (坐标参考系是传入的图片);
                           如果失败返回{}
    """
    return screenshot_in_window_region_and_ocr(inner_region, string, fuzzy=fuzzy)


def click_string_in_window(string: str, fuzzy: bool = False, option: int = 1, repeat: int = 1) -> None:
    """
    截取当前窗口, 并进行OCR识别, 获取想要定位的文本的中心坐标, 鼠标点击文本位置
    Parameters:
     param1: 需要定位的文本
     param2: 是否使用模糊匹配, 默认为False
     param3: 鼠标点击的选项, 默认为1, Left mouse is 1, middle[滚轮] is 2, right is 3, wheel up[滚轮上滚] is 4, wheel down[滚轮下滚] is 5
     param4: 鼠标点击的次数, 默认为1
    Return: None
    """
    string_pos = screenshot_window_and_ocr(string=string, fuzzy=fuzzy)
    assert string_pos != {}, f'获取{string}的坐标失败'

    # 获取当前活动的窗口id
    window_id = int(os.popen("xdotool getactivewindow").readline())
    res = os.system(
        f"xdotool mousemove -w {window_id} {string_pos[0]} {string_pos[1]} click --repeat {repeat} {option}")
    assert res == 0, f'鼠标点击{string}失败'


def click_string_in_region(region: list, string: str, fuzzy: bool = False, option: int = 1, repeat: int = 1) -> None:
    """
    截取指定区域, 并进行OCR识别, 获取想要定位的文本的中心坐标, 鼠标点击文本位置
    Parameters:
     param1: 区域坐标, 是一个列表 [x_pos, y_pos, width, height]
            (x_pos, y_pos都是相对于整个屏幕左上角的坐标)
     param2: 需要定位的文本
     param3: 是否使用模糊匹配, 默认为False
     param4: 鼠标点击的选项, 默认为1, Left mouse is 1, middle[滚轮] is 2, right is 3, wheel up[滚轮上滚] is 4, wheel down[滚轮下滚] is 5
     param5: 鼠标点击的次数, 默认为1
    Return: None
    """
    # 获取字符串在图片中的坐标
    string_pos_in_region = screenshot_region_and_ocr(
        region=region, string=string, fuzzy=fuzzy)

    assert string_pos_in_region != {}, f'获取{string}的坐标失败'

    string_pos = [region[0] + string_pos_in_region[0],
                  region[1] + string_pos_in_region[1]]

    res = os.system(
        f"xdotool mousemove {string_pos[0]} {string_pos[1]} click --repeat {repeat} {option}")

    assert res == 0, f'鼠标点击{string}位置失败'


def click_string_in_window_region(inner_region: list, string: str, fuzzy: bool = False, option: int = 1, repeat: int = 1) -> None:
    """
    截取指定区域, 并进行OCR识别, 获取想要定位的文本的中心坐标, 鼠标点击文本位置
    Parameters:
     param1: 区域坐标, 是一个列表 [x_pos, y_pos, width, height]
            (x_pos, y_pos都是相对于窗口左上角的坐标)
     param2: 需要定位的文本
     param3: 是否使用模糊匹配, 默认为False
     param4: 鼠标点击的选项, 默认为1, Left mouse is 1, middle[滚轮] is 2, right is 3, wheel up[滚轮上滚] is 4, wheel down[滚轮下滚] is 5
     param5: 鼠标点击的次数, 默认为1
    Return: None
    """
    window_pos = fn.get_active_window_position()
    x_pos = window_pos[0] + inner_region[0]
    y_pos = window_pos[1] + inner_region[1]
    region = [x_pos, y_pos, inner_region[2], inner_region[3]]

    click_string_in_region(region=region, string=string,
                           fuzzy=fuzzy, option=option, repeat=repeat)


def get_string_count_in_window(string: str, fuzzy: bool = False) -> int:
    """
    截图当前窗口, 并进行OCR识别, 返回识别出的字符串的个数
    Parameters
     param1: 需要统计的文本
     param2: 是否使用模糊匹配, 默认为False
    Returns: 识别出字符串的个数
    """
    img_path = fn.screenshot_window(
        filename='%Y-%m-%d_$wx$h.png',
        filepath='../Outputs/screenshots')
    print(f'\n\tSaved screenshot to {img_path}')

    count = ocr_img_and_get_string_count(img_path, string, fuzzy=fuzzy)
    return count


def get_string_count_in_region(region: list, string: str, fuzzy: bool = False) -> int:
    """
    截图指定区域, 并进行OCR识别, 返回识别出的字符串的个数
    Parameters
     param1: 区域坐标, 是一个列表 [x_pos, y_pos, width, height]
            (x_pos, y_pos都是相对于整个屏幕左上角的坐标)
     param2: 需要统计的文本
     param3: 是否使用模糊匹配, 默认为False
    Returns: 识别出字符串的个数
    """
    img_path = fn.screenshot_custom(
        region=region,
        filepath='../Outputs/screenshots')
    print(f'\n\tSaved screenshot to {img_path}')

    count = ocr_img_and_get_string_count(img_path, string, fuzzy=fuzzy)
    return count


def get_string_count_in_window_region(inner_region: list, string: str, fuzzy: bool = False) -> int:
    """
    截取指定区域, 并进行OCR识别, 返回识别出的字符串的个数
    Parameters
     param1: 区域坐标, 是一个列表 [x_pos, y_pos, width, height]
            (x_pos, y_pos都是相对于窗口左上角的坐标)
     param2: 需要统计的文本
     param3: 是否使用模糊匹配, 默认为False
    Returns: 识别出字符串的个数
    """
    window_pos = fn.get_active_window_position()
    x_pos = window_pos[0] + inner_region[0]
    y_pos = window_pos[1] + inner_region[1]
    region = [x_pos, y_pos, inner_region[2], inner_region[3]]

    return get_string_count_in_region(region=region, string=string, fuzzy=fuzzy)


def get_string_border_size_in_window(string: str, fuzzy: bool = False) -> list:
    """
    截图当前窗口, 并进行OCR识别, 返回识别出的字符串的边界大小
    Parameters
     param1: 需要统计的文本
     param2: 是否使用模糊匹配, 默认为False
    Returns: 识别出字符串的边界大小[w, h]
    """
    border_size = screenshot_window_and_ocr(string=string, fuzzy=fuzzy)[2:4]
    return border_size


def get_string_border_size_in_region(region: list, string: str, fuzzy: bool = False) -> list:
    """
    截图指定区域, 并进行OCR识别, 返回识别出的字符串的边界大小
    Parameters
     param1: 区域坐标, 是一个列表 [x_pos, y_pos, width, height]
            (x_pos, y_pos都是相对于整个屏幕左上角的坐标)
     param2: 需要统计的文本
     param3: 是否使用模糊匹配, 默认为False
    Returns: 识别出字符串的边界大小[w, h]
    """
    border_size = screenshot_region_and_ocr(
        region=region, string=string, fuzzy=fuzzy)[2:4]
    return border_size


def get_string_border_size_in_window_region(inner_region: list, string: str, fuzzy: bool = False) -> list:
    """
    截取指定区域, 并进行OCR识别, 返回识别出的字符串的边界大小
    Parameters
     param1: 区域坐标, 是一个列表 [x_pos, y_pos, width, height]
            (x_pos, y_pos都是相对于窗口左上角的坐标)
     param2: 需要统计的文本
     param3: 是否使用模糊匹配, 默认为False
    Returns: 识别出字符串的边界大小[w, h]
    """
    window_pos = fn.get_active_window_position()
    x_pos = window_pos[0] + inner_region[0]
    y_pos = window_pos[1] + inner_region[1]
    region = [x_pos, y_pos, inner_region[2], inner_region[3]]

    return get_string_border_size_in_region(region=region, string=string, fuzzy=fuzzy)


def click_string_in_window_with_offset(string: str, offset: list, fuzzy: bool = False, option: int = 1, repeat: int = 1) -> None:
    """
    截取当前窗口, 并进行OCR识别, 获取想要定位的文本的中心坐标, 鼠标点击偏移文本的位置, 偏移量为offset
    Parameters:
     param1: 需要定位的文本
     param2: 偏移量, 是一个列表 [x_offset, y_offset]
     param3: 是否使用模糊匹配, 默认为False
     param4: 鼠标点击的选项, 默认为1, Left mouse is 1, middle[滚轮] is 2, right is 3, wheel up[滚轮上滚] is 4, wheel down[滚轮下滚] is 5
     param5: 鼠标点击的次数, 默认为1
    """
    string_pos = screenshot_window_and_ocr(string=string, fuzzy=fuzzy)
    assert string_pos != {}, f'获取{string}的坐标失败'

    # 获取当前活动的窗口id
    window_id = int(os.popen("xdotool getactivewindow").readline())
    res = os.system(
        f"xdotool mousemove -w {window_id} {string_pos[0] + offset[0]} {string_pos[1] + offset[1]} click --repeat {repeat} {option}")
    assert res == 0, f'鼠标点击{string}失败'


def click_string_in_region_with_offset(region: list, string: str, offset: list, fuzzy: bool = False, option: int = 1, repeat: int = 1) -> None:
    """
    截取指定区域, 并进行OCR识别, 获取想要定位的文本的中心坐标, 鼠标点击偏移文本的位置, 偏移量为offset
    Parameters:
     param1: 区域坐标, 是一个列表 [x_pos, y_pos, width, height]
            (x_pos, y_pos都是相对于整个屏幕左上角的坐标)
     param2: 需要定位的文本
     param3: 偏移量, 是一个列表 [x_offset, y_offset]
     param4: 是否使用模糊匹配, 默认为False
     param5: 鼠标点击的选项, 默认为1, Left mouse is 1, middle[滚轮] is 2, right is 3, wheel up[滚轮上滚] is 4, wheel down[滚轮下滚] is 5
     param6: 鼠标点击的次数, 默认为1
    """
    # 获取字符串在图片中的坐标
    string_pos_in_region = screenshot_region_and_ocr(
        region=region, string=string, fuzzy=fuzzy)

    assert string_pos_in_region != {}, f'获取{string}的坐标失败'

    string_pos = [region[0] + string_pos_in_region[0],
                  region[1] + string_pos_in_region[1]]

    res = os.system(
        f"xdotool mousemove {string_pos[0] + offset[0]} {string_pos[1]+ offset[1]} click --repeat {repeat} {option}")

    assert res == 0, f'鼠标点击{string}位置失败'


def click_string_in_window_region_with_offset(inner_region: list, string: str, offset: list, fuzzy: bool = False, option: int = 1, repeat: int = 1) -> None:
    """
    截取指定区域, 并进行OCR识别, 获取想要定位的文本的中心坐标, 鼠标点击偏移文本的位置, 偏移量为offset
    Parameters:
     param1: 区域坐标, 是一个列表 [x_pos, y_pos, width, height]
            (x_pos, y_pos都是相对于窗口左上角的坐标)
     param2: 需要定位的文本
     param3: 偏移量, 是一个列表 [x_offset, y_offset]
     param4: 是否使用模糊匹配, 默认为False
     param5: 鼠标点击的选项, 默认为1, Left mouse is 1, middle[滚轮] is 2, right is 3, wheel up[滚轮上滚] is 4, wheel down[滚轮下滚] is 5
     param6: 鼠标点击的次数, 默认为1
    Return: None
    """
    window_pos = fn.get_active_window_position()
    x_pos = window_pos[0] + inner_region[0]
    y_pos = window_pos[1] + inner_region[1]
    region = [x_pos, y_pos, inner_region[2], inner_region[3]]

    click_string_in_region_with_offset(region=region, string=string, offset=offset,
                                       fuzzy=fuzzy, option=option, repeat=repeat)


if __name__ == '__main__':
    img_path = "/home/huyanrui/test.png"  # 测试图片的路径
    print()
    print(ocr_img_and_get_string_count(img_path, '矩形'))
    print()
    print(ocr_img_and_get_string_count(img_path, '矩形', fuzzy=True))
    print()
    print(ocr_img_and_get_coordinate(img_path, '矩形'))
    print()
    print(ocr_img_and_get_coordinate(img_path, '矩形', fuzzy=True))
