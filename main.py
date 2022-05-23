from pythonDIR import naver, articleID, apiGet

alertWord = ["n.news.naver.com", "blog.naver.com", "m.site.naver.com", "bit.ly", "github.com"]

driver = naver.login()
articleid = articleID.articleIDget()
apiGet.apiGet(driver, alertWord, articleid)