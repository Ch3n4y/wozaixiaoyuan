本文写于2020.12.1，目前为止可用，原理为抓包token值模拟登录，再通过脚本将打卡数据post上传至服务器。

思路及代码参考GitHub项目：https://github.com/178me/dailyInspectionReport/

感谢[**178me**](https://github.com/178me)的代码  

# 目录
* [基于腾讯云详细部署使用教程](#\xE5\x9F\xBA\xE4\xBA\x8E\xE8\x85\xBE\xE8\xAE\xAF\xE4\xBA\x91\xE8\xAF\xA6\xE7\xBB\x86\xE9\x83\xA8\xE7\xBD\xB2\xE4\xBD\xBF\xE7\x94\xA8\xE6\x95\x99\xE7\xA8\x8B)
    * [一、抓包获取token值](#\xE4\xB8\x80\xE6\x8A\x93\xE5\x8C\x85\xE8\x8E\xB7\xE5\x8F\x96token\xE5\x80\xBC)
        * [1、下载Fiddler](#1\xE4\xB8\x8B\xE8\xBD\xBDfiddler)
        * [2、安装及配置Fidder](#2\xE5\xAE\x89\xE8\xA3\x85\xE5\x8F\x8A\xE9\x85\x8D\xE7\xBD\xAEfidder)
        * [3、获取token值](#3\xE8\x8E\xB7\xE5\x8F\x96token\xE5\x80\xBC)
    * [二、云函数部署脚本打卡](#\xE4\xBA\x8C\xE4\xBA\x91\xE5\x87\xBD\xE6\x95\xB0\xE9\x83\xA8\xE7\xBD\xB2\xE8\x84\x9A\xE6\x9C\xAC\xE6\x89\x93\xE5\x8D\xA1)
        * [1、登录腾讯云](#1\xE7\x99\xBB\xE5\xBD\x95\xE8\x85\xBE\xE8\xAE\xAF\xE4\xBA\x91)
        * [2、创建云函数](#2\xE5\x88\x9B\xE5\xBB\xBA\xE4\xBA\x91\xE5\x87\xBD\xE6\x95\xB0)
        * [3、获取喵码](#3\xE8\x8E\xB7\xE5\x8F\x96\xE5\x96\xB5\xE7\xA0\x81)
        * [4、Python代码修改](#4python\xE4\xBB\xA3\xE7\xA0\x81\xE4\xBF\xAE\xE6\x94\xB9)
        * [5、设置定时触发](#5\xE8\xAE\xBE\xE7\xBD\xAE\xE5\xAE\x9A\xE6\x97\xB6\xE8\xA7\xA6\xE5\x8F\x91)  
  

# 主要步骤：

- 1、抓包token值

- 2、云函数部署脚本打卡


工具：

- PC台式机一台

- 电脑端微信

- 任一浏览器

- 腾讯云账号(实名认证)


## 一、抓包获取token值

抓包教程为利用Fiddler抓包配置教程

参考文章：

https://www.cnblogs.com/liulinghua90/p/9109282.html


### 1、下载Fiddler

下载最新版fiddler ，可以在官网下载：https://www.telerik.com/download/fiddler

百度云链接：链接：https://pan.baidu.com/s/1LqqJCMlBfQgB5C0_lU4r8g 提取码：whyi 



### 2、安装及配置Fidder

① 正常安装，下一步，下一步，可以修改软件安装地址，安装完毕后，打开软件。

② 打开Fiddler，点击工具栏中的Tools—>Options

![20201202095551](http://img.chaney.top/img/20201202095551.png)

③ 点击https设置选项，勾选选择项

![20201202170213](http://img.chaney.top/img/20201202170213.png)


④ 点击Actions,点击第二项：Export Root Certificate to Desktop，这时候桌面上会出现证书FiddlerRoot.cer文件，点击OK设置成功，关闭fiddler 

![20201202170235](http://img.chaney.top/img/20201202170235.png)

⑤ PC端，在浏览器中导入证书FiddlerRoot.cer，以谷歌浏览器为例说明，在浏览器上输入: chrome://settings/  然后进入高级设置，搜索管理证书

![20201202170302](http://img.chaney.top/img/20201202170302.png)

⑥ 在受信任的根证书颁发机构，对证书进行导入

![20201202170335](http://img.chaney.top/img/20201202170335.png)

⑦ 重新打开fiddler，就可以在电脑上进行https抓包了。如果不成功请看参考文章后面解决方案

![20201202170319](http://img.chaney.top/img/20201202170319.png)

### 3、获取token值

登录电脑端微信，打开我在校园日检日报  
留意最下方出现的```student.wozaixiaoyuan.com```双击打开  

![20201202170352](http://img.chaney.top/img/20201202170352.png)

出现的这一串token字符串值就是我们需要的了，第一步任务已经实现。如果后续登录失效了，重新抓包获取这个值即可，如果不出现特殊情况这个登录能保持四天左右。

![20201202095745](http://img.chaney.top/img/20201202095745.png)

## 二、云函数部署脚本打卡

### 1、登录腾讯云

如果没有用的过话先注册，实名认证

产品中搜索云函数，点击管理控制台

![20201202095903](http://img.chaney.top/img/20201202095903.png)
![20201202095909](http://img.chaney.top/img/20201202095909.png)

### 2、创建云函数

点击左侧的函数服务

![20201202170409](http://img.chaney.top/img/20201202170409.png)

点击新建

![20201202170427](http://img.chaney.top/img/20201202170427.png)

填写函数名称autocheck，运行环境选择Python3.6，空白函数

![20201202170441](http://img.chaney.top/img/20201202170441.png)
![20201202170501](http://img.chaney.top/img/20201202170501.png)

点击下一步，直接拉到最底下点击完成

![20201202170508](http://img.chaney.top/img/20201202170508.png)

### 3、获取喵码

手机微信中搜索公众号喵提醒，注册后添加提醒，获取喵码

![20201202170525](http://img.chaney.top/img/20201202170525.png)
![20201202170542](http://img.chaney.top/img/20201202170542.png)

记住这个喵码待会代码中要用到



### 4、Python代码修改

这段代码主要需要修改的内容为注释修改1、修改2、修改3、修改4  
分别为token值、打卡人昵称、喵提醒中的喵码和打卡人地址(可从Fiddler中看到之前打卡的位置信息)  
将修改后的代码贴到index.py中  

```python
import json
import logging
import requests, time, random
import datetime

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class Xiao:
    def __init__(self):
        # Token 列表
        # 修改1
        self.tokenArray = ["98bf740e-9f38-45c0-a163-688f7831b8a8"]
        # 修改2 
        self.tokenName = ["小明"]

        # 喵提醒通知
        # 修改3
        self.notifytoken = 'tnPS8eT'
        self.api = "https://student.wozaixiaoyuan.com/heat/save.json"
        self.headers = {
            "Host": "student.wozaixiaoyuan.com",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat",
            "Referer": "https://servicewechat.com/wxce6d08f781975d91/147/page-frame.html",
            "token": "",
            "Content-Length": "360",
        }
        # 修改4
        self.data = {
            "answers": '["0"]',
            "seq": self.get_seq(),
            "temperature": self.get_random_temprature(),
            "latitude": "10.0000000000", # 维度
            "longitude": "100.0000000000", # 经度
            "country": "中国",
            "city": "某某市",
            "district": "某某区",
            "province": "某某省",
            "township": "某某街道",
            "street": "某某路",
        }

    # 获取随机体温
    def get_random_temprature(self):
        random.seed(time.ctime())
        return "{:.1f}".format(random.uniform(36.2, 36.7))

    # seq的1,2,3代表着早，中，晚
    def get_seq(self):
        current_hour = datetime.datetime.now()
        current_hour = current_hour.hour + 8
        if 0 <= current_hour <= 8:
            return "1"
        elif 11 <= current_hour < 15:
            return "2"
        elif 17 <= current_hour < 21:
            return "3"
        else:
            return 1

    def run(self):
        num = 0
        for i in self.tokenArray:
            self.headers["token"] = i
            print("Token:" + self.headers["token"])
            print(datetime.datetime.now())
            res = requests.post(self.api, headers=self.headers, data=self.data, ).json()
            time.sleep(1)
            print(res)
            print(random.randint(1,100))
            msg = {
                "id": self.notifytoken,
                "text": "Token"  + '\n' + self.tokenName[num] +self.headers["token"] + '\n' + json.dumps(res, ensure_ascii=False),
                "type": "json"
            }
            print(type(msg))
            requests.post("http://miaotixing.com/trigger", data=msg)
            num = num + 1
        return True


if __name__ == "__main__":
    Xiao().run()


def main_handler(event, context):
    logger.info('got event{}'.format(event))
    return Xiao().run()
```


![20201202170558](http://img.chaney.top/img/20201202170558.png)

拉到下面保存，然后测试。测试成功说明代码没问题，这时你微信喵提醒应该就会给你发消息了。

![20201202170608](http://img.chaney.top/img/20201202170608.png)

这里一般会出现三种消息
```json
{“code”：0}, #表示打卡成功  
{“code”：-10}, #表示token值失效了，需要重新抓包获取token值  
{“code”：1}, #表示打卡时间已结束，不能打卡  
```


### 5、设置定时触发

点击左侧触发管理，创建触发器

![20201202170729](http://img.chaney.top/img/20201202170729.png)

起一个定时任务名称，将触发周期设置为最下面一个自定义触发周期

![20201202170739](http://img.chaney.top/img/20201202170739.png)
![20201202170747](http://img.chaney.top/img/20201202170747.png)

参数值为0 0 7，13，19 * * * *

分别代表着秒 分 时 日 月 星期 年

这里参数表示每天的上午7点、下午1点和晚上7点定时触发我们的云函数

![20201202170756](http://img.chaney.top/img/20201202170756.png)
![20201202170802](http://img.chaney.top/img/20201202170802.png)

那么到了这一步基本上我们的自动打卡也就完成了，如果有什么其他问题，可以多百度一下，享受探索的快感。