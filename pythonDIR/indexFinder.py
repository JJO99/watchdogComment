def indexFinder(articleAPI_div):
    # 나눈 API 중에서 comment, subject가 포함된 리스트의 원소를 찾고
    # 그 원소의 인덱스의 +2가 댓글, 제목이 있는 원소이므로 그걸 긁어오기
    commentIndex = []
    subjectIndex = []

    for i in range(len(articleAPI_div)):
        temp = articleAPI_div[i]
        if temp == 'subject':
            j = i + 2
            subjectIndex.append(j)
        if temp == 'content':
            j = i + 2
            commentIndex.append(j)
        else:
            continue
    return commentIndex, subjectIndex