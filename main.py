import datetime
from pythonDIR import naver, articleID, jsonanalysis, alertURLback, jsonGet, result

now = datetime.datetime.now()

#articleID 크롤링 - 로그인 필요가 없음
articleid = articleID.articleIDget()

#네이버 자동 로그인
driver = naver.login()
now1 = datetime.datetime.now()

# json API 이용
# 1. json return
json = jsonGet.jsonget(articleid, driver)
now2 = datetime.datetime.now()

# 2. json에서 원하는 요소를 찾아서 변수에 저장하기 + content 분석
alertComment = jsonanalysis.comment(json)
alertArticle = jsonanalysis.article(json)

result.res(alertComment, alertArticle, now)

now3 = datetime.datetime.now()

print('\n<<소요시간>>\n' + '드라이버 로그인: ' + str(now1-now) + '초');
print('JSON 파일 크롤링: ' + str(now2-now1) + '초');
print('내용 검사: ' + str(now3-now2) + '초')