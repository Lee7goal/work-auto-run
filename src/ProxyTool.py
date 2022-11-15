import requests
import time


class ProxyTools:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42'
        }

    def check(self, proxies):
        url = 'https://www.163.com'
        try:
            resp = self.session.get(url, proxies=proxies, timeout=20)
            if resp.status_code == 200:
                return True
            else:
                return False
        except:
            return False

    def get(self):
        resp = self.session.get('http://demo.spiderpy.cn/get/')
        if 'proxy' in resp.json():
            proxy = resp.json()['proxy']
            proxies = {
                "http": f'http://{proxy}',
                "https": f'http://{proxy}'
            }
            return proxies
        else:
            return None

    def run(self):
        while True:
            p = self.get()
            status = self.check(p)
            if status is True:
                return p
            time.sleep(5)
