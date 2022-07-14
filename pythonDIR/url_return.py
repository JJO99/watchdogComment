def list_url_return(list):
    issueURL = []
    for x in range(len(list)):
        if list[x] != 0:
            a = "https://cafe.naver.com/develoid/" + str(list[x])
            issueURL.append(a)
        else:
            continue

    if issueURL == []:
        return None
    else:
        return issueURL


def one_url_return(id):
    return "https://cafe.naver.com/develoid/" + str(id)
