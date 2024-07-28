# 필요한 라이브러리 설치
install.packages("stats")

# 라이브러리 로드
library(stats)

# 예제 데이터 생성
set.seed(123)
data <- matrix(rnorm(100), ncol=2)

# k-means 군집 분석 수행
kmeans_result <- kmeans(data, centers=3)

# 결과 출력
print(kmeans_result)

# 군집 결과 시각화
plot(data, col=kmeans_result$cluster)
points(kmeans_result$centers, col=1:3, pch=8, cex=2)
