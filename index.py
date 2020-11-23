import requests, time, random, json, datetime

class Xiao:
    def __init__(self):
        # Token 列表
        self.tokenArray = ["xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx"]
        # 喵提醒通知 https://miaotixing.com/
        self.notifytoken = 'XXX'
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
        self.data = {
            "answers": '["0"]',
            "seq": self.get_seq(),
            "temperature": self.get_random_temprature(),
            "latitude": "10.000000000",# 维度
            "longitude": "100.000000000",# 经度
            "country": "中国",
            "city": "市",
            "district": "区",
            "province": "省",
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
        current_hour = current_hour.hour
        if 0 <= current_hour <= 8:
            return "1"
        elif 11 <= current_hour < 15:
            return "2"
        elif 17 <= current_hour < 21:
            return "3"
        else:
            return 1

    def run(self):
        for i in self.tokenArray:
            self.headers["token"] = i
            res = requests.post(self.api, headers=self.headers, data=self.data, ).json()
            time.sleep(1)
            print(res)
            msg = {
                "id": self.notifytoken,
                "text": "Token" + self.headers["token"] + '\n' + json.dumps(res, ensure_ascii=False),
                "type": "json"
            }
            requests.post("http://miaotixing.com/trigger", data=msg)
        return True


if __name__ == "__main__":
    Xiao().run()


def main_handler(event, context):
    return Xiao().run()
