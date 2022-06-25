from pythonDIR import checkContent
from bs4 import BeautifulSoup


# 알람 설정할 파일
alertWord = ["m.site.naver.com", "bit.ly", "open.kakao.com"]


def comment(json):
    noti =[]
    for k in range(len(json)):
        a = json[k]['result']['comments']['items']
        for i in a:
            content = i['content']
            n = checkContent.checkComment(content, alertWord)
            if n == 1:
                noti.append(json[k]['result']['articleId'])

    return noti


def article(json):
    result = []

    for i in range(0, 10):
        js = json[i]

        a = js['result']['article']['contentHtml']

        soup = BeautifulSoup(a, 'html.parser')
        m = soup.get_text()
        m = m.replace('\n', '')
        m = m.split('.')
        for x in m:
            x = x.split(' ')
            n = checkContent.checkArticle(x, alertWord)
            if n == 1:
                result.append(js['result']['articleId'])

    return result


def article_writer(json):

    return 0


def comment_writer(json):

    return 0


def comment_number(json):

    return 0


def comment_time(json):

    return 0


def article_time(json):

    return 0