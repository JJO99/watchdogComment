import requests
from bs4 import BeautifulSoup

def articleIDget ():
    articleid = []
    url = 'https://cafe.naver.com/develoid'
    # 최신 댓글이 달린 게시글을 긁어오기
    response = requests.get(url)

    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    temp = [1,2,3,4,5]
    for x in temp:
        x = str(x)
        rawData = soup.select_one('#first-reply-page > li:nth-child(' + x + ') > a')
        # li:nth-child(N) --> N을 로테이션 돌려야
        # first --> second
        # first-reply-page > li:nth-child(1) > a
        # 함수 형태로 구현한 다음, 게시글 5개를 전부다 사이클 돌리게 제작?
        rawData = str(rawData)
        rawData_div = rawData.split("articleid=")
        rawData_div2 = rawData_div[1].split('"')
        articleid.append(rawData_div2[0])

    for x in temp:
        x = str(x)
        rawData = soup.select_one('#second-reply-page > li:nth-child(' + x + ') > a')
        # li:nth-child(N) --> N을 로테이션 돌려야
        # first --> second

        # 함수 형태로 구현한 다음, 게시글 5개를 전부다 사이클 돌리게 제작?
        rawData = str(rawData)
        rawData_div = rawData.split("articleid=")
        rawData_div2 = rawData_div[1].split('"')
        articleid.append(rawData_div2[0])

    return articleid