# Define some constants

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'
BLACK_DOMAIN = ['www.google.gf', 'www.google.io','www.google.com.lc']

DOMAIN = 'www.google.com'
URL_SEARCH = "https://{domain}/search?hl={language}&q={query}&btnG=Search&gbv=1"
URL_NUM = "https://{domain}/search?hl={language}&q={query}&btnG=Search&gbv=1&num={num}"
URL_NEXT = "https://{domain}/search?hl={language}&q={query}&btnG=Search&gbv=1&num={num}&start={start}"


config = {
    'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36',
    'BAIDU_DOMAIN': 'www.baidu.com',
    'GOOGLE_DOMAIN': 'www.google.com',
    'BAIDU_SEARCH': 'https://www.baidu.com/s?wd={query}&pn={number}&ie=utf-8',
    'GOOGLE_SEARCH': 'https://{domain}/search?hl=en&q={query}&btnG=Search&gbv=1&num={num}&start={start}',
    'BLACK_DOMAIN': ['www.google.gf', 'www.google.io','www.google.com.lc'],
    'BAIDU_NUM': 100,
    'proxy': None,#{'https': '127.0.0.1:8080'},
    'pause': 0
}

def set_config(key, value):
    global config
    config[key] = value

def get_config(key):
    global config
    return config[key]
