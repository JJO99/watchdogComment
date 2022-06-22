import datetime
from pythonDIR import naver, articleID, commentAPI, alertURLback

#알람으로 설정할 파일
alertWord = ["m.site.naver.com", "bit.ly", "open.kakao.com"]
now = datetime.datetime.now()

#https://apis.naver.com/cafe-web/cafe-articleapi/v2/cafes/23370764/articles/ + articleid

#차후 댓글 리스트를 파일 형태로 디스코드 봇으로 출력하기 위해 파일 생성 코드를 추가
fileMake = open("list.txt", "wt")
fileMake.close()
useFile = open("list.txt", "at")

#articleID 크롤링 - 로그인 필요가 없음
articleid = articleID.articleIDget()


#네이버 자동 로그인
driver = naver.login()

#제목과 댓글 리스트 파일에 저장
#driver 로그인 세션을 이용해 댓글 크롤링 -> 댓글 검사 -> 문제 있는 articleID만 반환
issueID = commentAPI.commentCheck(driver, alertWord, articleid, useFile)

#문제 있는 articleID를 받아 URL로 변환
issueURL = alertURLback.urlBack(issueID)

print('기준 시간: ' + str(now))

if issueURL is None:
    print("댓글 이상 없음")
else:
    print(issueURL)

useFile.close()