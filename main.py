import datetime
from pythonDIR import naver, articleID, jsonanalysis, alertURLback, jsonGet, result

now = datetime.datetime.now()

#articleID 크롤링 - 로그인 필요가 없음
articleid = articleID.articleIDget()

#네이버 자동 로그인
driver = naver.login()

# 2. json에서 원하는 요소를 찾아서 변수에 저장하기 + content 분석
alertComment = jsonanalysis.comment(json)
alertArticle = jsonanalysis.article(json)

result.res(alertComment, alertArticle, now)
