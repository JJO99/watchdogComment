import datetime
from pythonDIR import naver, articleID, alertURLback, jsonanalyse

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

idlist = list(set(idlist))
if not idlist == None:
    urllist = alertURLback.urlBack(idlist)

print('\n기준 시간: ' + str(now))
if not urllist == None:
    print("이상 게시글: " + str(urllist))
else:
    print("게시글 이상 없음")

