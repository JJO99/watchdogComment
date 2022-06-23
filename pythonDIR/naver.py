from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyperclip
from pythonDIR import personalInfo

def login():

    my_id = personalInfo.id()
    my_pw = personalInfo.pw()

    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument("disable-gpu")
    options.add_argument(
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.108 Safari/537.36")
    driver = webdriver.Chrome('../watchdogComment/pythonDIR/chromedriver', chrome_options=options) # macos: .exe 빼기 / windows: .exe 붙이기

    driver.get("https://naver.com")  # 네이버 접속
    driver.implicitly_wait(3)
    driver.find_element_by_xpath('//*[@id="account"]/a').click()  # NAVER 로그인 클릭

    pyperclip.copy(my_id)  # id 복사
    driver.find_element_by_xpath('//*[@id="id"]').send_keys(Keys.COMMAND, 'v')  # id 붙여넣기
    driver.implicitly_wait(5)
    pyperclip.copy(my_pw)  # 비밀번호 복사
    driver.find_element_by_xpath('//*[@id="pw"]').send_keys(Keys.COMMAND, 'v')  # 비밀번호 붙여넣기
    driver.implicitly_wait(5)
    driver.find_element_by_xpath('//*[@id="log.login"]').click()  # 로그인 클릭
    driver.implicitly_wait(5)

    print("Driver Pass")

    return driver

