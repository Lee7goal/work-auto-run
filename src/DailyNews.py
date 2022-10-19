import requests
from lxml import etree
import base64
import hashlib

import requests

import argparse

parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument("--wx-secret", type=str, default="0")

args = parser.parse_args()


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

def get_message_content() -> str:
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
    }

    url = "https://www.163.com/dy/media/T1603594732083.html"

    response = requests.get(url, headers=headers).text
    first_news_xpath = '//div[@class="tab_content"]/ul/li/a/@href'

    html = etree.HTML(response)
    content_url = html.xpath(first_news_xpath)[0]
#     proxies = {
#         "http": "http://221.5.80.66:3128",
#         "https": "http://221.5.80.66:3128",
#     }
#     content = requests.get(content_url, headers=headers, proxies=proxies).text
    content = requests.get(content_url, headers=headers).text
#     html = etree.HTML(content)

#     news_text_xpath = '//div[@class="post_body"]/p[2]/text()'
#     content_text_list = html.xpath(news_text_xpath)
#     content_text_list[0] = '每日早报, 精选15条热点新闻, 只花一分钟, 知晓天下事!'
#     content_text = "\n".join(content_text_list)
    content_text = content[:2000]
    return content_text


if __name__ == '__main__':
    bot = Bot(args.wx_secret)
    msg = get_message_content()
    bot.send_message(msg)
