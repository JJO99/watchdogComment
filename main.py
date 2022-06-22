import datetime
from pythonDIR import naver, articleID, jsonanalysis, alertURLback, jsonGet

now = datetime.datetime.now()

#articleID 크롤링 - 로그인 필요가 없음
articleid = articleID.articleIDget()

#네이버 자동 로그인
driver = naver.login()

# json API 이용
# 1. json return
json = jsonGet.jsonget(articleid, driver)

# 2. json에서 원하는 요소를 찾아서 변수에 저장하기 + content 분석
noti = jsonanalysis.jsonanalysis(json)

issueURL = None
#문제 있는 articleID를 받아 URL로 변환
if not noti == []:
    issueURL = alertURLback.urlBack(noti)

print('기준 시간: ' + str(now))

if issueURL is None:
    print("댓글 이상 없음")
else:
    print(issueURL)