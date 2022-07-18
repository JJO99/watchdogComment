import requests
from pythonDIR import url_return, auto_login
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By


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

        article_date = str(
            soup.select("#main-area > div:nth-child(4) > table > tbody > tr:nth-child(" + n + ") > td.td_date"))
        article_date = article_date.split(">")
        article_date = article_date[1]
        article_date = article_date.split("<")[0]

        article_title = str(soup.select(
            "#main-area > div:nth-child(4) > table > tbody > tr:nth-child(" + n + ") > td.td_article > div.board-list > div > a.article"))
        article_title = article_title.split("</span>")
        article_title = article_title[1].replace("\n", "").replace("</a>", "").replace(" ]", "").strip()

        article_author = str(soup.select(
            "#main-area > div:nth-child(4) > table > tbody > tr:nth-child(" + n + ") > td.td_name > div > table"))
        article_author = article_author.split(';">')
        article_author = article_author[1].split("<")
        article_author = article_author[0]

        article_api_url = 'https://apis.naver.com/cafe-web/cafe-articleapi/v2/cafes/23370764/articles/' + article_id

        driver.get(article_api_url)
        origin_text = driver.find_element(By.XPATH, '/html/body/pre').text
        article_image = origin_text.split('src')
        article_image = article_image[1].split('\"')
        article_image = article_image[2].replace("\\", "")

        article_location = origin_text.split("촬영 장소 ▶")
        article_location = article_location[1].split("</span>")
        article_location = article_location[0].strip()

        one_article = [article_title, article_author, article_location, article_image, article_date, article_url]

        photo_list.append(one_article)

    return photo_list
