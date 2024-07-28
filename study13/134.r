# 필요한 라이브러리 설치
install.packages("cluster")

# 라이브러리 로드
library(cluster)

# 예제 데이터 생성
set.seed(123)
data <- matrix(rnorm(1000), ncol=2)

# Clara 군집 분석 수행
clara_result <- clara(data, k=3)

# 결과 출력
print(clara_result)

# 군집 결과 시각화
plot(data, col=clara_result$clustering)
points(clara_result$medoids, col=1:3, pch=8, cex=2)
