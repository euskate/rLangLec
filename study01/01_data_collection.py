import requests
from bs4 import BeautifulSoup

# 웹 페이지 요청
url = "http://www.naver.com"
response = requests.get(url)

# HTML 파싱
soup = BeautifulSoup(response.text, 'html.parser')

# 예시로, Naver의 제목을 추출
title = soup.title.string
print("Page Title:", title)