def checkContent(comment, word):
    for x in comment:
        y = x.replace('\n', ' ')
        y = y.split(' ')
        for i in y:
            if i in word:
                return x
            else:
                continue
    return 0