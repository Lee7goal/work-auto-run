import base64
import hashlib

import requests


class Bot:
    def __init__(self, key):
        self.key = key
        self.headers = {
            'Content-Type': 'application/json'
        }

    def post_file(self, file):
        id_url = f'https://qyapi.weixin.qq.com/cgi-bin/webhook/upload_media?key={self.key}&type=file'  # 把机器人的key放入
        wx_url = f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={self.key}'

        data = {'file': open(file, 'rb')}

        response = requests.post(url=id_url, files=data)
        json_res = response.json()
        media_id = json_res['media_id']

        data = {"msgtype": "file",
                "file": {"media_id": media_id}
                }
        result = requests.post(url=wx_url, json=data)
        print(result)

    def send_message(self, text):
        data = {
            "msgtype": "text",
            "text": {
                "content": text
            }
        }
        resp = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={self.key}', headers=self.headers,
                             json=data)
        print(resp)
        print(resp.text)

    def send_img(self, file):
        with open(f"./image/{file}", "rb") as fa:
            base64_data = base64.b64encode(fa.read()).decode("ascii")

        f = open(f"./image/{file}", "rb")
        md = hashlib.md5()
        md.update(f.read())
        md5_str = md.hexdigest()

        data = {
            "msgtype": "image",
            "image": {
                "base64": base64_data,
                'md5': md5_str
            }
        }
        resp = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={self.key}', headers=self.headers,
                             json=data)
        print(resp)
        print(resp.text)