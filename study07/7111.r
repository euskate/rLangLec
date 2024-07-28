# 데이터 생성
set.seed(123)
group1 <- rnorm(30, mean = 50, sd = 10)
group2 <- rnorm(30, mean = 55, sd = 10)

# 독립 표본 t-검정
t.test(group1, group2)
