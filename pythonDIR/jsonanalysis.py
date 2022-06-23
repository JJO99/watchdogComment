from pythonDIR import checkContent

#알람으로 설정할 파일
alertWord = ["m.site.naver.com", "bit.ly", "open.kakao.com", "아무래도"]

def comment(json):
    noti =[]
    for k in range(len(json)):
        a = json[k]['result']['comments']['items']
        for i in a:
            content = i['content']
            n = checkContent.checkContent(content, alertWord)
            if n == 1:
                noti.append(json[k]['result']['articleId'])

    return noti


def article(json):
    temp = []
    json = json[0]

    a = json['result']['article']['contentHtml']

    return a


def article_writer(json):

    return 0


def comment_writer(json):

    return 0