from pythonDIR import personalInfo

db = personalInfo.sql_control()
cursor = db.cursor()


def comment_insert(list_value, x):
    sql = "INSERT IGNORE INTO develoid.comment (article_id, comment, writer, comment_raw, wrote, comment_id, comment_ref_id, deleted, alarm) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (int(x), list_value[0], list_value[1], list_value[0], list_value[2], list_value[3], list_value[4], False, False)
    cursor.execute(sql, val)
    db.commit()


def article_insert(temp, x):
    sql = "INSERT IGNORE INTO develoid.article (article_id, article, article_raw, writer, wrote, deleted, alarm) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (int(x), temp[0], temp[1], temp[2], temp[3], False, False)
    cursor.execute(sql, val)
    db.commit()


def search_sql_article(word):
    result = []
    for check_word in word:
        sql_article1 = "SELECT article_id, article, writer FROM develoid.article where article like %s"
        cursor.execute(sql_article1, check_word)
        temp = cursor.fetchall()
        if temp == ():
            continue
        else:
            result.append(temp)

    if result == []:
        return None
    else:
        return result


def search_sql_comment(word):
    result = []
    for check_word in word:
        sql_article3 = "SELECT article_id, comment, writer FROM develoid.comment where comment like %s"
        cursor.execute(sql_article3, check_word)
        temp = cursor.fetchall()
        if temp == ():
            continue
        else:
            result.append(temp)

    if result == []:
        return None
    else:
        return result
