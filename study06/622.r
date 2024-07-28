# 패키지 설치 및 로드
install.packages("lattice")
library(lattice)

# 기본 산점도
xyplot(mpg ~ wt, data = mtcars, main = "Weight vs. MPG", xlab = "Weight", ylab = "MPG")

# 히스토그램
histogram(~ mpg, data = mtcars, main = "Histogram of MPG", xlab = "MPG")

# 박스플롯
bwplot(mpg ~ factor(cyl), data = mtcars, main = "Boxplot of MPG by Cylinder", xlab = "Cylinder", ylab = "MPG")
