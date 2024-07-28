# 패키지 설치 및 로드
install.packages("rstatix")
library(rstatix)

# 데이터 생성
group <- factor(rep(c("A", "B", "C"), each = 20))
value <- c(rnorm(20, mean = 10), rnorm(20, mean = 15), rnorm(20, mean = 20))

# 데이터 요약
data_summary <- group_by(data.frame(group, value), group) %>% 
  get_summary_stats(value, type = "mean_sd")

# 단일 인자 ANOVA
anova_result <- anova_test(data = data.frame(group, value), dv = value, between = group)
get_anova_table(anova_result)
