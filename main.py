import naverlogintest, articleID

url = 'https://cafe.naver.com/applytestcafe'

articleid = articleID.articleIDget()

naverlogintest.test(articleid)
