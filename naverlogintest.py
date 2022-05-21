from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import pyperclip
import articleID, indexFinder, checkContent, dataList, articleAPIget, personalInfo

alertWord = ["n.news.naver.com", "blog.naver.com", "m.site.naver.com", "bit.ly"]

def test(articleid):
    driver = webdriver.Chrome('./chromedriver')

    my_id = personalInfo.id()
    my_pw = personalInfo.pw()

    driver.get("http://naver.com")  # 네이버 접속
    driver.implicitly_wait(3)
    driver.find_element_by_xpath('//*[@id="account"]/a').click()  # NAVER 로그인 클릭

    pyperclip.copy(my_id)  # id 복사
    driver.find_element_by_xpath('//*[@id="id"]').send_keys(Keys.COMMAND, 'v')  # id 붙여넣기
    driver.implicitly_wait(5)
    pyperclip.copy(my_pw)  # 비밀번호 복사
    driver.find_element_by_xpath('//*[@id="pw"]').send_keys(Keys.COMMAND, 'v')  # 비밀번호 붙여넣기
    driver.implicitly_wait(5)
    driver.find_element_by_xpath('//*[@id="log.login"]').click()  # 로그인 클릭
    driver.implicitly_wait(5)

    word = str(alertWord)
    print('현재 감시 중인 단어: ' + word + '\n')

    for x in range(len(articleid)):
        url2 = 'https://apis.naver.com/cafe-web/cafe-articleapi/v2/cafes/23370764/articles/' + articleid[x] + '/comments/pages/1?requestFrom=A&orderBy=asc'
        driver.get(url2)
        driver.implicitly_wait(3)
        html2 = driver.page_source
        soup2 = BeautifulSoup(html2, 'html.parser')
        articleAPI = soup2
        articleAPI = str(articleAPI)
        articleAPI_div = articleAPI.split('"')

        commentIndex, subjectIndex = indexFinder.indexFinder(articleAPI_div)

        comment_list = dataList.makeList(articleAPI_div, commentIndex, subjectIndex)

        a = checkContent.checkContent(comment_list, alertWord)

        if a == 1:
            print('%%%%%%%%% ALERT! %%%%%%%%%\n')
        else:
            print('\n')

