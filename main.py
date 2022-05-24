import sys
from pythonDIR import naver, articleID, apiGet

alertWord = ["n.news.naver.com", "blog.naver.com", "m.site.naver.com", "bit.ly", "github.com"]
fileMake = open("list.txt", "wt")
fileMake.close()
useFile = open("list.txt", "at")

driver = naver.login()
articleid = articleID.articleIDget()
apiGet.apiGet(driver, alertWord, articleid, useFile)

useFile.close()