import requests
import json
from bs4 import BeautifulSoup


def recent_article_id_get():
    articleid = []
    url = 'https://cafe.naver.com/develoid'
    # 최신 댓글이 달린 게시글을 긁어오기
    response = requests.get(url)

    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    temp = [1,2,3,4,5]
    for x in temp:
        x = str(x)
        rawdata = str(soup.select('#first-reply-page'))
        firstsplit = rawdata.split("articleid=")
        secondsplit = []
        for x in firstsplit:
            secondsplit.append(x.split('"'))
        for x in temp:
            articleid.append(secondsplit[x][0])

    for x in temp:
        x = str(x)
        rawdata = str(soup.select('#second-reply-page'))
        firstsplit = rawdata.split("articleid=")
        secondsplit = []
        for x in firstsplit:
            secondsplit.append(x.split('"'))
        for x in temp:
            articleid.append(secondsplit[x][0])

    return articleid