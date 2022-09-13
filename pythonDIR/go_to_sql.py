import pymysql as pymysql
import sshtunnel
import pymysql

tunnel = sshtunnel.SSHTunnelForwarder(('138.2.119.24', 22), ssh_username='ubuntu', ssh_pkey='/Users/juno/PycharmProjects/watchdogComment/pythonDIR/ssh-key-2022-09-10 (1).key', remote_bind_address=('127.0.0.1', 3306))
tunnel.start()
db = pymysql.connect(host='127.0.0.1', user='root', password='Mandu920@', port=tunnel.local_bind_port)

cursor = db.cursor()


def comment_insert(id, comment, writer, cid, refid, cdate):
    id = int(id)
    comment = str(comment)
    cid = int(cid)
    refid = int(refid)
    nowdate = cdate

    sql = "INSERT IGNORE INTO develoid.comment (article_id, comment, writer, wrote, comment_id, comment_ref_id) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (id, comment, writer, nowdate, cid, refid)
    cursor.execute(sql, val)
    db.commit()


def article_insert(article_id, article, writer, wrote, count):
    article_id = int(article_id)
    article = str(article)
    writer = str(writer)
    wrote_date = wrote
    count = int(count)

    sql = "INSERT IGNORE INTO develoid.article (article_id, article, writer, wrote) VALUES (%s, %s, %s, %s)"
    val = (article_id, article, writer, wrote_date)
    cursor.execute(sql, val)
    db.commit()
