# 데이터 프레임 생성
data <- data.frame(group = rep(c("A", "B"), each = 50), value = c(rnorm(50), rnorm(50, mean = 3)))

# 상자 그림 생성
ggplot(data, aes(x = group, y = value)) +
  geom_boxplot(fill = "lightblue") +
  labs(title = "상자 그림", x = "그룹", y = "값")
