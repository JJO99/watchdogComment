def makeList(articleAPI_div, commentIndex, subjectIndex, f, id):
    comment_list = []
    subject_list = [articleAPI_div[subjectIndex[0]]]

    f.write('Title: ' + subject_list[0] + '\n')
    f.write('https://cafe.naver.com/develoid/' + str(id) + '\n')

    for i in range(len(commentIndex)):
        j = str(i + 1)
        a = articleAPI_div[commentIndex[i]]
        b = a.replace('\\n', ' ').replace('\\r', '')
        comment_list.append(b)
        f.write('comment' + j + ': '+ b + '\n')

    f.write('\n\n')

    return(comment_list)