# 데이터 생성
before <- rnorm(20, mean = 100, sd = 15)
after <- before + rnorm(20, mean = 5, sd = 10)

# 종속 표본 t-검정
t.test(before, after, paired = TRUE)
