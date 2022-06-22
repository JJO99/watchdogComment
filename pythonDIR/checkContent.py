def checkContent(comment, word):
    c = 0

    y = comment.replace('\n', ' ').replace('\r', '').replace('\t', '')
    y = y.split(' ')

    for i in y:
        i = i.split('/')
        for j in i:
            if j in word:
                c = 1
            else:
                continue

    return c