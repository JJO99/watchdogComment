def checkContent(comment, word, id):
    for x in range(len(comment)):
        t = comment[x]
        p = t.split("/")

        for y in range(len(p)):
            for z in range(len(word)):
                if p[y] == word[z]:
                    print("%%%%%%%%%% ALERT! %%%%%%%%%%")
                    print('%%%%%%%%%% URL: https://cafe.naver.com/develoid/' + str(id) + ' %%%%%%%%%%')