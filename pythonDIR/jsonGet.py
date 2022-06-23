import json

def jsonget(articleid, driver):
    value = []
    for x in range(len(articleid)):
        url = 'https://apis.naver.com/cafe-web/cafe-articleapi/v2/cafes/23370764/articles/' + articleid[x]
        driver.get(url)

        cr = driver.find_element_by_xpath('/html/body/pre').text
        cr = json.loads(cr)
        value.append(cr)

    print("JSON Get")
    return value