# 데이터 프레임 생성
data <- data.frame(values = rnorm(100))

# 히스토그램 생성
ggplot(data, aes(x = values)) +
  geom_histogram(binwidth = 0.5, fill = "blue", color = "black") +
  labs(title = "히스토그램", x = "값", y = "빈도")
