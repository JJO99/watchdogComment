from pythonDIR import alertURLback


def res(art, now):
    print('\n기준 시간: ' + str(now))

    if not art == None:
        article = alertURLback.urlBack(art)
        print("이상 게시글: " + str(article))
    else:
        print("게시글 이상 없음")