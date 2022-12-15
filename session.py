# 작업 세션별로 사용되는 코드가 달라져서, 이를 한번에 해결하기 위한 방책입니다.

def chrome_path(os):
    if os == "Darwin":
        return '../watchdogComment/pythonDIR/chromedriver'
    elif os == "Linux":
        return '/home/ubuntu/chromedriver'
    elif os == "Windows":
        return '..\watchdogComment\pythonDIR\chromedriver.exe'


def os_id(os):
    if os == "Darwin":
        return 1
    elif os == "Linux":
        return 2
    elif os == "Windows":
        return 3
