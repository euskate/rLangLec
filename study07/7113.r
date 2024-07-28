# 데이터 생성
group <- factor(rep(c("A", "B", "C"), each = 20))
value <- c(rnorm(20, mean = 10), rnorm(20, mean = 15), rnorm(20, mean = 20))

# 단일 인자 ANOVA
anova_result <- aov(value ~ group)
summary(anova_result)
