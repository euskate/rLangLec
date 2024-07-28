import requests
from bs4 import BeautifulSoup
import pandas as pd

# 1. 웹 페이지 요청
url = 'https://kosis.kr/statHtml/statHtml.do?orgId=101&tblId=DT_1B81A21&vw_cd=MT_ZTITLE&list_id=A21&seqNo=&lang_mode=ko&language=kor&obj_var_id=&itm_id=&conn_path=MT_ZTITLE'
response = requests.get(url)

# 요청이 성공했는지 확인
if response.status_code == 200:
    print("웹 페이지 요청 성공")
else:
    print(f"웹 페이지 요청 실패, 상태 코드: {response.status_code}")
    exit()

# 2. HTML 파싱
soup = BeautifulSoup(response.text, 'html.parser')

# 3. 데이터 추출
# 표의 ID가 'copyMainTableT'인 테이블을 찾습니다
table = soup.find('table', id='copyMainTableT')

# 테이블이 존재하는지 확인
if table is None:
    print("테이블을 찾을 수 없습니다.")
    exit()

# 헤더 추출
headers = []
header_row = table.find('thead').find_all('th')
for th in header_row:
    headers.append(th.get_text(strip=True))

# 데이터 추출
data = []
rows = table.find('tbody').find_all('tr')
for row in rows:
    cols = row.find_all('td')
    row_data = [col.get_text(strip=True) for col in cols]
    data.append(row_data)

# 4. 데이터프레임 생성
df = pd.DataFrame(data, columns=headers)

# 데이터 확인
print("출산율 데이터:")
print(df.head())

# 5. CSV 파일로 저장 (선택적)
df.to_csv('birth_rates_by_region.csv', index=False)

print("CSV 파일로 저장 완료: birth_rates_by_region.csv")
