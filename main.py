import naver, articleID, apiGet, indexFinder, dataList, checkContent

alertWord = ["n.news.naver.com", "blog.naver.com", "m.site.naver.com", "bit.ly", "github.com"]
url = 'https://cafe.naver.com/applytestcafe'

driver = naver.login()
articleid = articleID.articleIDget()
apiGet.apiGet(driver, alertWord, articleid)