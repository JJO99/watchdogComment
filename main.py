import datetime
from pythonDIR import articleID, alertURLback, jsonanalyse


def watch(driver):
    now = datetime.datetime.now()

    # articleID 크롤링 - 로그인 필요가 없음
    articleid = articleID.articleIDget()

    # 네이버 자동 로그인


    idlist = []
    for i in articleid:
        cube = jsonanalyse.check(driver, i)
        n = cube.articlecheck()
        m = cube.commentcheck()
        if not n == None:
            idlist.append(n)
        if not m == None:
            idlist.append(m)

    idlist = list(set(idlist))
    if not idlist == None:
        urllist = alertURLback.urlBack(idlist)


    if not urllist == None:
        urllist = str(urllist)
    else:
        urllist = "0"
    now = str(now)

    return urllist, now