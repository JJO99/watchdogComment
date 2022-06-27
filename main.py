import datetime
from pythonDIR import naver, articleID, jsonanalysis, alertURLback, jsonGet, result, jsonanalyse

now = datetime.datetime.now()

# articleID 크롤링 - 로그인 필요가 없음
articleid = articleID.articleIDget()

# 네이버 자동 로그인
driver = naver.login()

idlist = []
for i in articleid:
    cube = jsonanalyse.check(driver, i)
    n = cube.articlecheck()
    m = cube.commentcheck()
    if not n == None:
        idlist.append(n)
    if not m == None:
        idlist.append(m)

