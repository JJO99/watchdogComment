import requests
import json
from bs4 import BeautifulSoup


def recent_article_id_get ():
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


def all_article_id_get():
    # 최근 게시글 40개의 "게시글 내용" 분석만을 위함
    article_id = []
    url = 'https://cafe.naver.com/ArticleList.nhn?search.clubid=23370764&search.boardtype=L&search.menuid=&search.marketBoardTab=D&search.specialmenutype=&userDisplay=40'
    r = requests.get(url)
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')
    for x in range(1, 41, 1):
        x = str(x)
        check = str(soup.select('#main-area>div:nth-child(4)>table>tbody>tr:nth-child(' + x + ')>td.td_article>div.board-list>div>a.article'))
        check = check.split("articleid=")
        check = check[1].split("&amp")
        article_id.append(check[0])

    return article_id



