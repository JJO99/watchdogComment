import pymysql
from pythonDIR import personalInfo

db = pymysql.connect(
    user='dbmasteruser',
    passwd=personalInfo.sql_password(),
    host=personalInfo.sql_host(),
    db='develoid'
)

cursor = db.cursor()


def comment_insert(id, comment, writer, cid, refid, cdate):
    id = int(id)
    comment = str(comment)
    cid = int(cid)
    refid = int(refid)
    nowdate = cdate

    sql = "INSERT INTO develoid.comment (article_id, comment, writer, wrote, comment_id, comment_ref_id) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (id, comment, writer, nowdate, cid, refid)
    cursor.execute(sql, val)
    db.commit()


def article_insert(article_id, article, writer, wrote, count):
    article_id = int(article_id)
    article = str(article)
    writer = str(writer)
    wrote_date = wrote
    count = int(count)

    sql = "INSERT INTO develoid.article (article_id, article, writer, wrote, count) VALUES (%s, %s, %s, %s, %s)"
    val = (article_id, article, writer, wrote_date, count)
    cursor.execute(sql, val)
    db.commit()

