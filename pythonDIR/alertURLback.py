def urlBack(list):
    for x in range(len(list)):
        if list[x] != 0:
            a = "https://cafe.naver.com/develoid/" + str(list[x])
            return a
        else:
            continue