from bs4 import BeautifulSoup
from pythonDIR import checkContent, indexFinder, dataList

def apiGet(driver, word, articleid, file):
    alertID = []

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
        comment_list = dataList.makeList(divData, commentIndex, subjectIndex, file, articleid[x])

        findID = checkContent.checkContent(comment_list, word, articleid[x])

        alertID.append(findID)

    return alertID