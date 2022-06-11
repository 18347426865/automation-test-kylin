# 麒麟操作系统软件自动化测试项目

## 项目简介

本项目是南开大学软件学院2022年春季学期《软件测试与维护》专业课程的**期末大作业**，

项目要求如下所示：

> 环境要求：PC端安装麒麟桌面操作系统(v10sp1)
> 准入材料：麒麟提供桌面常用的软件（应用列表，需求说明书）
>
> 实施步骤：
> 1. 每组随机分配5个应用，保证每组分配的应用测试难度均衡，每个应用设计10+条测试用例
> 包括：通用测试用例（安装/启动/卸载）和专用测试用例（根据应用业务情况，设计用户高频的使用场景，如微信：发送消息，发送图片，查看朋友圈，查看通讯录，搜索等）
>   每条用例需要包括(用例编号,用例名称,用例属性,重要等级,预置条件,测试数据,测试步骤,预期结果),用例符合规范。
>
> 2. 熟悉kylinautogui的所有方法，可在麒麟桌面操作系统单独运行kylinautogui中的每个方法
>
> 3. 组内分工，结合自动化测试开发的分层思想使用unitest测试框架，实现用例进行转化与组装，测试用例按照unittest格式进行编写，测试数据以yaml格式
>
> 4. 使用unittestreport输出单个应用测试报告，并最终输出一份完整的包含所有应用的测试报告，测试报告应包含（测试环境，用例总数，测试时间,开始时间,通过数,失败数，每条用例的详细信息）并将测试报告发送到邮箱。
>
> 5. 在整个过程中，记录遇到的问题以及问题的解决办法、解决思路，工具可优化改进的地方。

本项目的协作者为：

- 胡艳瑞
- 卢紫宇
- 马子智
- 杨建国

## 项目目录结构

```
.
├── Adjuncts
│   ├── 此文件夹存放非源代码性质的附件
├── baidunetdisk
│   └── "百度网盘"测试根目录
├── kdesktop
│   └── "金山文档"测试根目录
├── kylinautogui
│   ├── 此为kylinautogui模块根目录
├── feishu
│   └── "飞书"测试根目录
├── qaxsafe
│   └── "奇安信网神终端安全管理系统"测试根目录
├── README.md   (此文件)
└── wpsoffice
    ├── "WPS_Office"测试根目录，包含四个子程序
    ├── wps     (WPS 文字)
    ├── et      (WPS 表格)
    ├── wpp     (WPS 演示)
    └── wpspdf  (WPS PDF)
```

## 运行方式

### 配置要求

- 硬件要求： 4核CPU 4GB内存
- 系统要求：银河麒麟桌面操作系统V10 (SP1)
- 软件要求：软件商店更新至最新版
- 依赖要求：scrot &emsp; xdotool &emsp; python3 **python版本必须是 3.9.7 或以上**

### 安装xdotool依赖

sudo apt install xdotool

### 安装scrot依赖

sudo apt install scrot

### 安装python依赖(在项目根目录执行)

pip3 install -r ./kylinautogui/requirements.txt

## 项目运行者须知

首先，参照上一节安装各种依赖，然后，使用最新版的软件商店安装本测试项目所需的5个软件.
可能会出现软件的界面与目前开发时的软件界面不一致的情况. 如果遇到这种情况，本测试项目不能保证完美运行

另外，在测试过程中存在一些小问题需要手动处理.

- 百度网盘在安装以后需要先使用账号登录一次，为的是通过手机验证码信任当前环境，否则会出现登录失败的情况. 如果测试登录困难太大，那就只能跳过登录的测试样例了.(目前，百度网盘的第一个测试用例--登录账号测试是跳过的状态，如果想要启用，可以去掉装饰器)

- 百度网盘在测试开始之前，需要先进入[baidunetdisk_all.py](./baidunetdisk/TestCase/baidunetdisk_all.py) 中修改 setUp() 函数里面的配置, 一般只要修改用户名就可以了. 有时候会出现用户名太长的情况，在百度网盘上显示不全，所以还需要一个在百度网盘上能够识别的名字。

- 飞书的测试需要先登录账号，并且15天以内免登录(15这个数字应该没有记错)

- 金山文档的测试也需要先登录账号，测试默认的状态是已登录

- 奇安信网神终端安全管理系统十分好测，注意事项几乎没有

- WPS Office的测试基本上没大问题，只是需要注意测试样例执行的顺序，有些步骤需要前面创建的文件作为原材料.

## 项目开发者须知

### 1. 如何在终端中使用命令行启动想要测试的应用？

**注意：下面的桌面快捷方式是安装好应用之后设置的，如果安装路径不一样，那么下面提供的文件和命令所含的路径都将失效！**
**如果发现失效，可以在测试的系统上查看桌面快捷方式文件，检索Exec即可找到正确的启动应用的命令**

查看此项目Adjuncts文件夹下以`.desktop`结尾的文件(本质上是桌面的快捷方式))，文件名与想要启动的应用的名字相对应

例如：想要启动`百度网盘`程序，可以打开`./Adjuncts/baidudnetdisk.desktop`文件，找到包含`Exec`关键字的一行，
等号后面的内容复制到终端中，回车，即可打开对应的程序

PS: 在每个以`.desktop`结尾的文件中，搜索`Name`即可得知此文件对应的程序名称

为了方便使用，现把部分应用的启动命令整理如下：（均使用bash执行）

```bash

# 奇安信网神终端安全管理系统
qaxtray

# 金山文档
/opt/apps/cn.kdocs.kdesktop/files/bin/kdesktop

# 飞书
/usr/bin/bytedance-feishu-stable

# 百度网盘
/opt/baidunetdisk/baidunetdisk

# WPS 表格
/usr/bin/et

# WPS 文字
/usr/bin/wps

# WPS 演示
/usr/bin/wpp

# WPS PDF阅读器
/usr/bin/wpspdf

```


### 2. 当想要使用某些功能操作应用窗口，但是kylinautogui没有给怎么办？

**自己使用python的os模块以及bash脚本进行封装**

例如， kylinautogui/libs/untils.functions有一个函数叫做 close_app,
其内部实现是调用了python os模块执行bash脚本 kill -9,
这样做虽然可以关闭应用, 但是属于强制关闭. 在测试的过程中发现这个方法极其不好用, 存在引发bug的风险
更好的关闭应用的方式是使用快捷键 `alt+F4`, 写成代码就是
使用 kylinautogui/libs/untils/functions.py 中的 `key_input('alt+F4')`


###  3. 如何使用OCR服务？

第一种：自己在kylin OS中部署一个服务并使用

在之前的小作业期间，我们已经学过部署的方法，如果相关环境没有删除，下面的命令可以直接在终端执行

```bash
hub serving start -m chinese_ocr_db_crnn_mobile
```

不出所料的话，执行之后将会获得服务Running的地址: http://127.0.0.1:8866
如果不一致，需要修改 kylinautogui/libs/untils/paddleocr.py 文件的内容

第二种: 使用学校的 PaddleOCR 服务

这个是默认的策略. 如果在校外的同学无法使用此服务, try 语句块将无法进行下去, 跳转到 except 语句块使用本地的服务

### 4. 使用VS Code远程连接进行开发时, 对python功能的支持不全或者有错误怎么办?

1. import 顺序在格式化时出问题

    这个问题可以通过在 import 语句的末尾加上注释 `# NOQA: E402` 来解决

2. 导入自定义包无法解析(找不到)

    无法解析有两种情况:

    1) 在命令行运行时无法解析;

    2) VS Code 代码编辑窗口无法解析;

    对于第一种情况, 在运行的python文件里加上类似下面的代码即可解决:

    ```python
    testcasedir = os.path.dirname(__file__)
    kylinautoguidir = f"{testcasedir}/../../kylinautogui"
    sys.path.append(kylinautoguidir)

    ```

    对于第二种情况, 需要对SSH远程连接进行设置.

    这个是 VS Code 关于python包搜索路径设置的问题, 只要在设置中加上 kylinautogui 的路径即可

    `ctrl+逗号`打开 VS Code 设置页面, 在三个设置范围内选择 远程SSH 一栏, 意味着接下来的设置项只对当前远程连接的机器生效,
    不会应用到本地. 在搜索栏中输入关键字 `python.analysis.extraPath`, 添加 kylinautogui 文件夹的绝对路径即可

    (Note: 当使用 VS Code 打开项目文件夹时, 在资源管理器视图右击一个文件或者文件夹, 弹出的菜单中有复制绝对路径和相对路径的选项~~)

    由于VS Code所有的设置都保存在一个叫做 `settings.json`的文件中, 因此我们可以直接编辑此文件来进行设置

    如何打开此文件? 可以在设置页面随便选择一个带有 `在settings.json编辑`标记的设置项, 点击这个标记, 即可打开settings.json文件.

    需要注意的是, 不同的机器, 不同的文件夹 都可以有个性化的设置, 文件夹内的设置只对此文件夹下的项目有效.

    本人的settings.json文件的内容如下:

    ```json
    {
        "python.languageServer": "Pylance",
        "python.analysis.completeFunctionParens": true,
        "python.analysis.extraPaths": [
            "/home/huyanrui/KylinLabs/AutomationTest/kylinautogui"
        ],
        "python.analysis.typeCheckingMode": "basic",
        "python.condaPath": "/home/huyanrui/anaconda3/bin/conda",
        "python.formatting.autopep8Path": "/home/huyanrui/anaconda3/bin/autopep8",
        "editor.codeActionsOnSave": {
            "source.organizeImports": false
        }
    }

    ```

3. 语言服务器总是崩溃
    目前想到的办法就是重启 VS Code

4. DISPALY环境变量的问题
    有时候可能需要在VS Code里面快速调试, 但是可能报DISPALY变量找不到的错误, 此时我们可以在python代码中加入如下一行:
    `os.environ['DISPLAY'] = ':0'  `


### 5. git 的使用

如果不清楚git的用法，可以点击[这里](https://gitee.com/help/articles/4105), 查看其中的“Git 版本控制入门”一节; 也可以去B站学习~

git [command] -h | --help 可以查看有关某个 command 的帮助信息 (-h 对应简短帮助, --help 对应详细帮助)

```bash

git clone git@gitee.com:hulumayang/automation-test.git AT
git switch -c XXXX  # (创建一个新的分支并切换过去)
git status          # (可以帮助你查看当前的状态，十分有用！迷糊的时候就使用这条命令)
git add 文件名/目录
git commit -m "This is a message."
git push origin     # (提交代码，遇到冲突先问问组长，别把仓库搞烂了。。按提示操作应该不会出问题)
git push --set-upstream origin hyr      #(指定push的上游分支)
git stash           # (把当前的更改进行一个临时存储[贮藏], 在 pull --rebase 的时候可能用到)
git stash list      # (查看所有贮藏的记录)
git stash show      # (查看贮藏的对文件的更改有哪些)
git stash pop       # (恢复最近一次暂时存储的文件, 之后丢弃)
git stash apply     # (恢复, 不丢弃, 默认恢复最近一次的贮藏记录)
git stash drop      # (丢弃, 默认恢复最近一次的贮藏记录)
git remote -v       # (列出所有远端仓库)
git remote remove origin    # (删除一个仓库)
git remote add origin git@gitee.com:hulumayang/automation-test.git  # 增加与本地仓库关联的远端仓库
git pull origin master      # (拉取远端origin仓库master分支的最新代码, 并合并到当前分支)
git pull origin master --rebase     # 这是最推荐的获取最新代码的命令 !!! \建议不要用上一个,因为默认的合并策略是 merge, 会产生一个多余的提交
# rebase 策略会让分支更整齐, 没有那么多分叉
```

### 6. python os 模块的两个方法的使用

1. status_code = os.system("`command line`")  # 返回的是一个状态码, 若为 0 表示命令正常结束执行
                                (注意, 命令执行的结果会直接输出到stdout中, python程序无法捕获)

2. result = os.popen("`command line`")   # 返回的是命令输出的内容,调用readline()可以读取其中内容


### 7. xdotool 键盘输入有效的key值列表

在使用 kylinautogui/libs/untils/functions.py 中的 key_input()方法时, 需要传入一个表示按键的字符串,
这个实际上是由 `xdotool` 来解析执行的.

程序对字符串内字母的大小写很敏感, 比如'A'和'a'表示不同的按键.

另外, 有些按键的名字有些让人意外, 比如回车
不是'enter' 或者 'Enter', 而是 'Return', 大小写必须与这个单词完全一致, 写成 'return' 则无法识别.

键盘最上方的 f1~f12 按键对应的是 'F1' ~ 'F12', 大小写也不容出错.
所以 key_input('alt+F4') 可行, 但是把F换成f就不行

参考资料如下：

- [xdotool-keyboard](https://www.linux.org/threads/xdotool-keyboard.10528/)

- [xdotool-list-of-key-codes](https://gitlab.com/cunidev/gestures/-/wikis/xdotool-list-of-key-codes) 比第一个更详细一些~~

使用技巧： 浏览器打开页面, ctrl + F 直接搜索关键字, 如 enter, 可以发现回车对应的key是 Return(是不是很吃惊？)


### 8. 关于 kylinautogui 默认的一系列不好用的地方

1. 很多方法都需要一个 window_id, 有些麻烦...

    私以为, 加入此参数确实有利于提高通用性, 但是在绝大多数场合下, 我们只想对当前激活的窗口进行操作,
    如果每次调用方法都需要传入此参数, 显得有些累赘. window_id 应该有一个默认值, 也就是当前激活的窗口的 window_id
    所以, 我对 functions.py 中的某些方法进行了改进, 把 window_id设置成默认参数, 放在参数列表的后面, 默认值设为0
    在函数内部, 如果发现 window_id 的值为 0, 说明调用者没有传入 window_id 的值( 传入的window_id应该不可能是 0)
    此时, 将 window_id 重新赋值为当前窗口的 window_id

2. start_app() 和 close_app() 方法并不总是合意

    有些应用是常驻后台的, 譬如 百度网盘 和 qaxsafe (中文名太长懒得记...), 这时候 start_app()就不好用了.
    虽然能够打开页面, 但是返回值是 False. 原因在于进程在页面打开之前就已经存在. 这个函数的小毛病暂且忍一忍.

    很多时候，调用close_app()方法时, 只是想要关闭窗口。然而某些应用的窗口关闭后，应用后台进程依然存在。而close_app()方法
    的实现是采用 kill -9 查杀进程的方法，并不只是结束前台窗口的进程，而是一窝端。

    关闭应用怎么能直接 `kill -9` 呢? 这多么危险啊! 万一有个文档还没保存好, 这样子岂不是直接丢了!
    还是使用快捷键 `alt+F4` 更合理

    在查看 xdotool 手册的时候，我注意到有一个 `windowkill` 命令，它可以直接把窗口关闭。
    本来以为这个可以避开 `kill -9` 的坑，后来测试的时候发现也会强制关闭窗口，并不会提示用户文档没有保存。
    所以我在functions.py 里面添加的 `close_current_window()` 方法其实还是没有满足我的需要。

    为了安全性和合理性，还是老老实实用快捷键 `alt+F4` 关闭窗口吧。

3. OCR接口不能用了

    其实这个不该怪 kylinautogui, 解决办法就是自己写了一个 paddleocr.py 文件来提供OCR接口. 这应该算是写了一个适配器.

4. 有些流程如 **截图-> 识别 -> 获取字符串坐标 -> 点击** 没有好用的组装方法
    所以我费尽心思写了 composite.py 文件, 目的就是组装 OCR 和截图、鼠标点击操作

5. 鼠标矩形选取，没有现成的操作

    所以我在 functions.py 里面补充上了
    - mouse_select_rectangle
    - mouse_select_rectangle_in_window


### 9. 当打开 report.html 文件时, 图表不显示的解决方法

首先要明白原因: 图表的显示需要从服务器下载 css 和 js 文件, 如果服务器无法访问, 图表就不显示了.

最近, 也就是2022-05-30, cdn.jsdelivr.net 正好无法访问,
所以我们需要找一个替代品

将如下的代码复制到 report.html 文件的 `<head>` 标签里面, 取代原来无法访问的包含 `cdn.jsdelivr.net` 的`script` 和 `style`标签即可

```html
<link rel="stylesheet" href="https://cdn.staticfile.org/twitter-bootstrap/4.5.0/css/bootstrap.min.css">
<script src=" https://cdn.staticfile.org/jquery/2.0.0/jquery.min.js"></script>
<script src="https://cdn.staticfile.org/echarts/5.1.2/echarts.min.js"></script>
```

更新: 从[官方网站](https://unittestreport.readthedocs.io/en/latest/)上找到了解释:

> 说明：1.4版本之前报告模板中的使用的jsdelivr CDN站点现在国内访问不了，已在1.4.2和1.5.0版中进行了更换，
> 如果生成的报告样式和图表丢失，请升级unittestreport版本
>
> pip install unittestreport==1.4.2 用的bootstrap的CDN
> pip install unittestreport==1.5.0 用的七牛云的CDN

所以不需要每次手动调整 HTML 文件的内容, 只需要把 unittestreport 包更新即可.

### 10. input_string() 的解决方案 paste_string()

在使用 functions.py 中的 input_string() 方法时, 如果输入的字符串中包含了中文, 就会出现问题.
表现为桌面分辨率突然改变, 自动化测试方法的稳定性骤降.

为了解决这个问题, 我在网上发现了一种新的输入字符串的方法, 也就是先把要输入的字符串复制到剪贴板,
然后用 ctrl + v 粘贴输入. 这样做就没有问题了. 复制到剪贴板的功能由 xclip 工具提供.

但是！凡事都有但是，这个方法只能在不关注样式的条件下使用. 比如, 在我测试的时候发现, 在WPS 演示中使用 paste_string 时, 本意是要在标题框里面
输入文字, 但是经过测试, 实际上, 文字不会输入到标题框里, 而是粘贴在了一个新的文本框里. 当我发现这一现象时, 我只好改用 input_string() 方法.
此时就没问题了. 也许默认的 ctrl+v 需要换成 ctrl+shift+v 才能起到预期的效果? 目前尚未测试.

这种现象不难理解, 在windows电脑上, 我们使用复制粘贴的时候, 有时候粘贴的是一个带格式的文本, 而不单单是简单的字符串.
正是由于这个特性, paste_string() 方法无法满足之前对它的期望.


### 11. 善用回车键

在编写测试用例的时候, 我发现有些时候弹出的一个对话框的按钮位置总是变化, 同时这个对话框并不是以一个独立窗口的形式出现的.
这种情况下, 我们可以通过按下回车键来起到点击按钮的作用. 不过, 一定要确保在点击按钮之前, 焦点聚焦在了我们想要操作的按钮上. 如果没有聚焦上, 可以使用 Tab 键切换聚焦位置.


### 12. 坐标常量 和 区域常量

有些时候, 我们需要点击一个图标按钮, 但是使用现成的 OCR 技术无法识别出这个图标按钮的坐标
(因为现在的 OCR 不认识图标, 只认得文字). 所以我们可以在确保图标的位置不变动或者不经常变动的情况下,
使用手工测量的方法获取按钮的坐标. 这样做的好处在于, 通过手工的测量, 以后点击按钮的时候就不需要再使用 OCR 获取坐标了.

同样的道理, 我们也可以使用手工测量的方法划定一块区域, 然后使用 OCR 获取这块儿区域内的文字.
使用固定的区域有助于提高识别的效率, 避免识别出不关心甚至干扰正常识别的字符

本项目中应用此理念的一个示例 : `feishu/TestCase/constants.py`



## 项目观察者、研究者、发扬者须知

关于本项目的设计思想，请查看项目根目录的 [`DesignThought.md`](./DesignThought.md) 文件，
里面的内容对理解项目公共方法十分重要！
