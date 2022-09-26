def checkComment(comment, word):
    c = 0

    y = comment.replace('\n', ' ').replace('\r', '').replace('\t', '')
    y = y.split(' ')

    for i in y:
        i = i
        for j in i:
            if j in word:
                c = 1
            else:
                continue

    return c


def checkArticle(article, word):
    c = 0

    for i in article:
        if i in word:
            c = 1
        else:
            continue

    return c