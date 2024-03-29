from selenium import webdriver
from pythonDIR import personalInfo
from selenium.webdriver.common.by import By
import platform
import session


def login():
    driver_path = session.chrome_path(str(platform.system()))

    naver_id = personalInfo.id()
    naver_pw = personalInfo.pw()

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--disable-gpu")
    options.add_argument("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70")
    driver = webdriver.Chrome(driver_path, chrome_options=options) # macos: .exe 빼기 / windows: .exe 붙이기

    driver.get("https://naver.com")  # 네이버 접속
    driver.implicitly_wait(3)
    element = driver.find_element(By.XPATH, '//*[@id="account"]/a')
    driver.find_element(By.XPATH, '//*[@id="account"]/a').click()

    driver.execute_script("document.getElementsByName('id')[0].value=\'" + naver_id + "\'")
    driver.execute_script("document.getElementsByName('pw')[0].value=\'" + naver_pw + "\'")
    # https://2dowon.github.io/docs/python/google-naver-daum-automatic-login/
    driver.find_element(By.XPATH, '//*[@id="log.login"]').click()  # 로그인 클릭
    driver.implicitly_wait(5)

    return driver

