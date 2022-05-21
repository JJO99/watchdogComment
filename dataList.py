import checkContent


def makeList(articleAPI_div, commentIndex, subjectIndex):
    comment_list = []
    subject_list = [articleAPI_div[subjectIndex[0]]]

    print(subject_list[0])

    for i in range(len(commentIndex)):
        j = str(i + 1)
        a = articleAPI_div[commentIndex[i]]
        b = a.replace('\\n', ' ').replace('\\r', '')
        comment_list.append(b)
        print('comment ' + j + ': ' + b)

    return(comment_list)