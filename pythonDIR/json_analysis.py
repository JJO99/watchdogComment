import json
from pythonDIR import check_content
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from datetime import datetime


class check:
    def __init__(self, driver, articleid, word):
        self.driver = driver

        self.articleid = articleid

        url = 'https://apis.naver.com/cafe-web/cafe-articleapi/v2/cafes/23370764/articles/' + self.articleid
        self.driver.get(url)

        cr = self.driver.find_element(By.XPATH, '/html/body/pre').text
        cr = json.loads(cr)
        self.jsonfile = cr

        self.commenttext = []

        self.article_count = self.jsonfile['result']['article']['readCount']

        self.articletext = self.jsonfile['result']['article']['contentHtml']

        self.ar_date = self.jsonfile['result']['article']['writeDate']

        self.word = word

    def commentcheck(self):
        word = self.word
        a = self.commenttext

        for i in a:
            n = check_content.checkComment(i, word)
            if n == 1:
                return self.articleid
            else:
                return None

    def articlecheck(self):
        word = self.word
        a = self.articletext

        soup = BeautifulSoup(a, 'html.parser')
        m = soup.get_text() # text만 불러오므로 태그가 포함된 soup 자체를 읽을 필요가 있음
        m = m.replace('\n', '')
        # m = m.split('.')
        m = m.split('/')
        if len(m) > 1:
            for x in m:
                for y in word:
                    if x == y:
                        return self.articleid
                    else:
                        continue

    def comment(self):
        result = []
        y = self.commenttext
        for x in y:
           result.append(x.replace('\n', ' ').replace('\r', '').replace('\t', ''))
        return result

    def article(self):
        return self.articletext
    
    def wrote_date(self):
        return self.ar_date

    def comment_sql_Data(self):
        comment_item = self.jsonfile['result']['comments']['items']
        to_send_sql_comment = []

        for x in comment_item:
            content = x['content']
            writer = x['writer']['id']
            comment_id = x['id']
            comment_ref_id = x['refId']

            comment_date = int(x['updateDate'])
            comment_date = comment_date / 1000
            comment_date = datetime.fromtimestamp(comment_date).strftime('%Y-%m-%d %H:%M:%S')

            self.commenttext.append(content)

            mkl = [content, writer, comment_date, comment_id, comment_ref_id]

            to_send_sql_comment.append(mkl)

        return to_send_sql_comment

    def article_sql_Data(self):
        a = self.articletext
        soup = BeautifulSoup(a, 'html.parser')
        m = soup.get_text() # text만 불러오므로 태그가 포함된 soup 자체를 읽을 필요가 있음
        m = m.replace('\n', '')
        # m = m.split('.')
        article_only_text = m.split('/')

        writer = self.jsonfile['result']['article']['writer']['id']

        wrote = self.wrote_date()
        wrote = wrote / 1000
        wrote = datetime.fromtimestamp(wrote).strftime('%Y-%m-%d %H:%M:%S')

        count = self.article_count

        origin_article_sql_data = [article_only_text, writer, wrote, count]

        return origin_article_sql_data
