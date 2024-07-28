install.packages("dplyr")
library(dplyr)

# 데이터 생성
df <- tibble(id = 1:1000, value = rnorm(1000))

# 데이터 처리
df_processed <- df %>%
  filter(value > 0) %>%
  group_by(id) %>%
  summarize(mean_value = mean(value))

print(df_processed)
