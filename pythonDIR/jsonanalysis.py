from pythonDIR import checkContent, alertword
from bs4 import BeautifulSoup

# 클래스 형태로 제작 하는 것을 고민
# 현재 상태는 분석을 위해 여러개의 파이썬 파일에서 여러개의 함수를 이용했으나, 클래스를 이용해 되도록 하나로 모으는 것을 고민
def comment(json):
    word = alertword.word()
    result = []
    for k in range(len(json)):
        a = json[k]['result']['comments']['items']
        for i in a:
            content = i['content']
            n = checkContent.checkComment(content, word)
            if n == 1:
                result.append(json[k]['result']['articleId'])

    return result


def article(json):
    word = alertword.word()
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
            n = checkContent.checkArticle(x, word)
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