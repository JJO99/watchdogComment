import datetime
from pythonDIR import naver, articleID, commentAPI, alertURLback

alertWord = ["m.site.naver.com", "bit.ly", "open.kakao.com"]
now = datetime.datetime.now()

fileMake = open("list.txt", "wt")
fileMake.close()
useFile = open("list.txt", "at")

driver = naver.login()
articleid = articleID.articleIDget()

print('기준 시간: ' + str(now))

aID = commentAPI.apiGet(driver, alertWord, articleid, useFile)
result = alertURLback.urlBack(aID)
if result is None:
    print("댓글 이상 없음")
else:
    print(result)

useFile.close()