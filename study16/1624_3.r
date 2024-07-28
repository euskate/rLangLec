install.packages("ggplot2")
library(ggplot2)

# 데이터 생성
df <- data.frame(x = rnorm(100), y = rnorm(100))

# 산점도 생성
ggplot(df, aes(x = x, y = y)) +
  geom_point() +
  labs(title = "Scatter Plot", x = "X-axis", y = "Y-axis")
