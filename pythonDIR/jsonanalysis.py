from pythonDIR import checkContent

#알람으로 설정할 파일
alertWord = ["m.site.naver.com", "bit.ly", "open.kakao.com", "아무래도"]

def jsonanalysis(javascript):
    noti =[]
    for k in range(len(javascript)):
        a = javascript[k]['result']['comments']['items']
        for i in a:
            content = i['content']
            n = checkContent.checkContent(content, alertWord)
            if n == 1:
                noti.append(javascript[k]['result']['articleId'])

    return noti
