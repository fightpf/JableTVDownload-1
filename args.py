import argparse
from bs4 import BeautifulSoup
import random
from urllib.request import Request, urlopen
from config import headers
import re


def get_parser():
    parser = argparse.ArgumentParser(description="Jable TV Downloader")
    parser.add_argument("--random", type=bool, default=False,
                        help="Enter True for download random ")
    parser.add_argument("--url", type=str, default="",
                        help="Jable TV URL to download")
    parser.add_argument("--hot", type=bool, default=False,
                        help="Jable TV hot URL to download")

    return parser


def av_recommand():
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = 'https://jable.tv/'
    request = Request(url, headers=headers)
    web_content = urlopen(request).read()
    # 得到繞過轉址後的 html
    soup = BeautifulSoup(web_content, 'html.parser')
    h6_tags = soup.find_all('h6', class_='title')
    av_list = re.findall(r'https[^"]+', str(h6_tags))
    return random.choice(av_list)
def av_list(num):
    headers = {'User-Agent': 'Mozilla/5.0'}
    result = []
    for i in range(1,int(num)+1):
        url = 'https://jable.tv/hot/'+str(i) +"/"
        request = Request(url, headers=headers)
        web_content = urlopen(request).read()
        # 得到繞過轉址後的 html
        soup = BeautifulSoup(web_content, 'html.parser')
        h6_tags = soup.find_all('h6', class_='title')
        av_list = re.findall(r'https[^"]+', str(h6_tags))
        result += av_list
        print(result)
    return result



# print(av_recommand())
