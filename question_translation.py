import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from googletrans import Translator
from pymongo import MongoClient

# BeautifulSoup
# URL을 읽어서 HTML 받아오고, HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
url = "http://iteslj.org/questions/"
result = requests.get(url)
bs_obj = BeautifulSoup(result.content, "html.parser")

# 첫 페이지에서 a 태그로 각 서브페이지의 href 찾기
q_packages = bs_obj.find("tr")
q_packages_html = q_packages.findAll("a")

# googletrans
translator = Translator()

# pymongo
client = MongoClient('mongodb://test:test@localhost', 27017)
# client = MongoClient('localhost', 27017)
db = client.dbbbackco

for q_html in q_packages_html:
    # selenium
    # 서브페이지의 href와 앞의 주소를 붙여 각 서브페이지 링크 연결
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--single-process")
    chrome_options.add_argument("--disable-dev-shm-usage")
    path = '/home/ubuntu/sparta/chromedriver'
    driver = webdriver.Chrome(path, chrome_options=chrome_options)

    # driver = webdriver.Chrome('/home/ubuntu/sparta/chromedriver')
    # driver = webdriver.Chrome('/home/ubuntu/sparta/')  # 웹드라이버 파일의 경로
    # driver = webdriver.Chrome(executable_path="sftp: // ubuntu @ 3.36.75.191 / home / ubuntu / sparta / chromedriver")
    # driver = webdriver.Chrome(ChromeDriverManager().install())


    driver.get("http://iteslj.org/questions/" + q_html['href'])

    # BeautifulSoup
    html = driver.page_source  # 페이지의 elements 모두 가져오기
    soup = BeautifulSoup(html, 'html.parser')  # BeautifulSoup 사용하기
    notices = soup.select('#bd > div.main.wide > ul > li')

    for n in notices:
        questions = n.text.strip()
        q_korean = translator.translate(questions, dest="ko")
        doc = {'question': q_korean.text}
        db.questions_ko.insert_one(doc)
        # print(q_korean.text)

        # selenium 창 닫기
        driver.quit()
