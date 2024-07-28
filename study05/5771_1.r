# ggplot2 패키지 로드
library(ggplot2)

# 데이터 프레임 생성
data <- data.frame(x = rnorm(100), y = rnorm(100))

# 산점도 생성
ggplot(data, aes(x = x, y = y)) +
  geom_point() +
  labs(title = "산점도", x = "X 값", y = "Y 값")
