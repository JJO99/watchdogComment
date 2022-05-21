from bs4 import BeautifulSoup

import checkContent
import indexFinder, dataList

def apiGet(driver, word, articleid):
    print('현재 감시 중인 단어: ' + str(word))

    for x in range(len(articleid)):
        url2 = 'https://apis.naver.com/cafe-web/cafe-articleapi/v2/cafes/23370764/articles/' + articleid[x] + '/comments/pages/1?requestFrom=A&orderBy=asc'
        driver.get(url2)
        driver.implicitly_wait(3)
        html2 = driver.page_source
        soup2 = BeautifulSoup(html2, 'html.parser')
        articleAPI = soup2
        articleAPI = str(articleAPI)
        divData = articleAPI.split('"')

        commentIndex, subjectIndex = indexFinder.indexFinder(divData)
        comment_list = dataList.makeList(divData, commentIndex, subjectIndex)

        checkContent.checkContent(comment_list, word, articleid[x])