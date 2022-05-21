import requests, indexFinder, dataList
from bs4 import BeautifulSoup

def articleapiget(articleid):
    for x in range(len(articleid)):
        id = articleid[x]
        url2 = 'https://apis.naver.com/cafe-web/cafe-articleapi/v2/cafes/23370764/articles/' + id + '/comments/pages/1?requestFrom=A&orderBy=asc'

        # API를 "로 나누기
        response2 = requests.get(url2)

        html2 = response2.text
        soup2 = BeautifulSoup(html2, 'html.parser')
        articleAPI = soup2
        articleAPI = str(articleAPI)
        articleAPI_div = articleAPI.split('"')

        commentIndex, subjectIndex = indexFinder.indexFinder(articleAPI_div)

        dataList.makeList(articleAPI_div, commentIndex, subjectIndex)