# 데이터 생성
before <- rnorm(20, mean = 100, sd = 15)
after <- before + rnorm(20, mean = 5, sd = 10)

# Wilcoxon 부호 순위 검정
wilcox.test(before, after, paired = TRUE)
