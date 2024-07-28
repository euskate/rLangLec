# 패키지 설치 및 로드
install.packages("ggplot2")
library(ggplot2)

# 기본 산점도
ggplot(mtcars, aes(x = wt, y = mpg)) + 
  geom_point() + 
  labs(title = "Weight vs. MPG", x = "Weight", y = "MPG")

# 히스토그램
ggplot(mtcars, aes(x = mpg)) + 
  geom_histogram(binwidth = 2) + 
  labs(title = "Histogram of MPG", x = "MPG", y = "Frequency")

# 박스플롯
ggplot(mtcars, aes(x = factor(cyl), y = mpg)) + 
  geom_boxplot() + 
  labs(title = "Boxplot of MPG by Cylinder", x = "Cylinder", y = "MPG")
