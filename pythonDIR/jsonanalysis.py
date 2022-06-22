from bs4 import BeautifulSoup
from pythonDIR import checkContent, indexFinder, dataList
import requests

#알람으로 설정할 파일
alertWord = ["m.site.naver.com", "bit.ly", "open.kakao.com", "몇주후에"]


def jsonanalysis(javascript):
    noti =[]
    for k in range(len(javascript)):
        a = javascript[k]['result']['comments']['items']
        for i in a:
            content = i['content']
            n = checkContent.checkContent(content, alertWord)
            if n == 1:
                noti.append(javascript[k]['result']['articleId'])

    return noti
