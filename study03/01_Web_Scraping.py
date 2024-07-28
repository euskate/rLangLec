import requests
from bs4 import BeautifulSoup

# 웹 페이지 요청
response = requests.get('https://example.com')
soup = BeautifulSoup(response.text, 'html.parser')

# 데이터 추출
titles = soup.find_all('h1')
for title in titles:
    print(title.get_text())