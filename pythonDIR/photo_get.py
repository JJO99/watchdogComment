import requests
from pythonDIR import url_return, json_analysis
from bs4 import BeautifulSoup
import time

def photo_get(recent_id, driver):
    url = "https://cafe.naver.com/ArticleList.nhn?search.clubid=23370764&search.menuid=7&search.boardtype=L&userDisplay=15&search.headid=2391"
    photo_list = []
    r = requests.get(url)
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')
    for n in range(1, 16, 1):
        n = str(n)
        article_id = str(soup.select(
            "#main-area>div:nth-child(4)> table > tbody > tr:nth-child(" + n + ") > td.td_article > div.board-number > div"))
        article_id = article_id.split(">")
        article_id = article_id[1]
        article_id = article_id.split("<")
        article_id = article_id[0]
        article_url = url_return.one_url_return(article_id)

        if article_id == recent_id:
            break

        article_title = str(soup.select(
            "#main-area > div:nth-child(4) > table > tbody > tr:nth-child(" + n + ") > td.td_article > div.board-list > div > a.article"))
        article_title = article_title.split("</span>")
        article_title = article_title[1].replace("\n", "").replace("</a>", "").replace(" ]", "").strip()

        article_author = str(soup.select(
            "#main-area > div:nth-child(4) > table > tbody > tr:nth-child(" + n + ") > td.td_name > div > table"))
        article_author = article_author.split(';">')
        article_author = article_author[1].split("<")
        article_author = article_author[0]

        json_open = json_analysis.check(driver, article_id, "")
        origin_text = json_open.article()

        origin_unix_time = json_open.wrote_date() / 1000
        origin_unix_time = origin_unix_time
        dateset = time.gmtime(origin_unix_time)
        article_date = str(dateset.tm_year) + "년 " + str(dateset.tm_mon) + "월 " + str(dateset.tm_mday) + "일 " + str(dateset.tm_hour) + ":" + str(dateset.tm_min) + ":" + str(dateset.tm_sec)

        article_image = origin_text.split('src')

        article_image_list = []
        for x in range(len(article_image)):
            if x % 2 == 0:
                continue
            else:
                image = article_image[x].split('\"')
                image = image[2].replace("\\", "")
                article_image_list.append(image)

        article_location = origin_text.split("촬영 장소 ▶")
        article_location = article_location[1].split("</span>")
        article_location = article_location[0].strip()

        image_date = origin_text.split("촬영 날짜 ▶")
        image_date = image_date[1].split("</span>")
        image_date = image_date[0].strip()

        image_title = origin_text.split("작품을 대표할 제목 ▶")
        if len(image_title) == 1:
            image_title = "Unknown"
        else:
            image_title = image_title[1].split("</span>")
            image_title = image_title[0].strip()

        one_article = [article_title, article_author, article_location, article_image_list, article_date, article_url, image_date, image_title, article_id]

        photo_list.insert(0, one_article)

    return photo_list
