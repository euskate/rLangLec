# 데이터 생성
group1 <- factor(rep(c("A", "B"), each = 30))
group2 <- factor(rep(c("X", "Y", "Z"), times = 20))
value <- rnorm(60, mean = 10) + as.numeric(group1) + as.numeric(group2)

# 이원 인자 ANOVA
anova_result <- aov(value ~ group1 * group2)
summary(anova_result)
