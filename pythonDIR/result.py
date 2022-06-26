from pythonDIR import alertURLback


def res(com, art, now):
    print('\n기준 시간: ' + str(now))

    # 문제 있는 articleID를 받아 URL로 변환
    if not com == []:
        comment = alertURLback.urlBack(com)
        print("이상 댓글: " + str(comment))
    else:
        print("댓글 이상 없음")
    if not art == []:
        article = alertURLback.urlBack(art)
        print("이상 게시글: " + str(article))
    else:
        print("게시글 이상 없음")