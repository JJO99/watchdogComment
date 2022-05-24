import datetime
from pythonDIR import naver, articleID, apiGet, alertURLback

alertWord = ["m.site.naver.com", "bit.ly", "open.kakao.com"]
now = datetime.datetime.now()

fileMake = open("list.txt", "wt")
fileMake.close()
useFile = open("list.txt", "at")

driver = naver.login()
articleid = articleID.articleIDget()
aID = apiGet.apiGet(driver, alertWord, articleid, useFile)

print('기준 시간: ' + str(now))

result = alertURLback.urlBack(aID)
if result == None:
    print("이상 없음")
else:
    print(result)

useFile.close()