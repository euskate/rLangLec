# 필요한 라이브러리 설치
install.packages("stats")

# 라이브러리 로드
library(stats)

# 예제 데이터 생성
data <- matrix(rnorm(100), ncol=2)

# 거리 행렬 계산
dist_matrix <- dist(data)

# 계층적 군집 분석 수행
hclust_result <- hclust(dist_matrix, method="complete")

# 덴드로그램 시각화
plot(hclust_result)
