import json
from pythonDIR import alertword, checkContent
from bs4 import BeautifulSoup

class check:
    def __init__(self, driver, articleid):
        self.driver = driver
        self.articleid = articleid

        url = 'https://apis.naver.com/cafe-web/cafe-articleapi/v2/cafes/23370764/articles/' + self.articleid
        self.driver.get(url)

        cr = self.driver.find_element_by_xpath('/html/body/pre').text
        cr = json.loads(cr)

        self.jsonfile = cr

        self.commenttext = None
        self.articletext = None
        self.word = alertword.word()

    def commentcheck(self):
        word = self.word
        a = self.jsonfile['result']['comments']['items']
        self.commenttext = a

        for i in a:
            content = i['content']
            n = checkContent.checkComment(content, word)
            if n == 1:
                return self.articleid
            else:
                return None


    def articlecheck(self):
        word = self.word
        js = self.jsonfile

        a = js['result']['article']['contentHtml']

        soup = BeautifulSoup(a, 'html.parser')
        m = soup.get_text()
        m = m.replace('\n', '')
        m = m.split('.')
        for x in m:
            x = x.split(' ')
            n = checkContent.checkArticle(x, word)
            if n == 1:
                return self.articleid
            else:
                return None

    def comment(self):
        return self.commenttext

    def article(self):
        return self.articletext