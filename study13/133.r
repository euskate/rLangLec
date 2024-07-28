# 필요한 라이브러리 설치
install.packages("dbscan")

# 라이브러리 로드
library(dbscan)

# 예제 데이터 생성
set.seed(123)
data <- matrix(rnorm(100), ncol=2)

# DBSCAN 군집 분석 수행
dbscan_result <- dbscan(data, eps=0.5, minPts=5)

# 결과 출력
print(dbscan_result)

# 군집 결과 시각화
plot(data, col=dbscan_result$cluster + 1L)
