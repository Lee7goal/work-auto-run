import requests
from lxml import etree


def get_message_content() -> str:
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Referer": "https://www.baidu.com/link?url=P5vJLXg3Xw_oJz7SKHtCB7oK6B9ZcAqVmn8h1xQ00toj0CN9C-QPLi97Mv_FwhI4r9DrSyRnt-IQl9X1IGg-5K&wd=&eqid=a75c7a660009df0c0000000662ded05b",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.71",
        "sec-ch-ua": "^\\^",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "^\\^Windows^^"
    }

    url = "https://www.163.com/dy/media/T1603594732083.html"
    response = requests.get(url, headers=headers).text
    first_news_xpath = '//div[@class="tab_content"]/ul/li/a/@href'

    html = etree.HTML(response)
    content_url = html.xpath(first_news_xpath)[0]

    content = requests.get(content_url, headers=headers).text
    html = etree.HTML(content)

    news_text_xpath = '//div[@class="post_body"]/p[2]/text()'
    content_text_list = html.xpath(news_text_xpath)
    content_text_list[0] = '每日早报, 精选15条热点新闻, 只花一分钟, 知晓天下事!'
    content_text = "\n".join(content_text_list)
    return content_text


if __name__ == '__main__':
    msg = get_message_content()
    print(msg)
