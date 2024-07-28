# 데이터 생성
group1 <- rnorm(30, mean = 50, sd = 10)
group2 <- rnorm(30, mean = 55, sd = 10)

# Mann-Whitney U 검정
wilcox.test(group1, group2)
