# 데이터의 기본 통계량 확인
print(data.describe())

# 예를 들어, 'title' 열의 빈도수 분석
title_counts = data['title'].value_counts()
print(title_counts)
