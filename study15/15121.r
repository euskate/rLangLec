library(dplyr)
df <- tibble(id = 1:1000, value = rnorm(1000))
df_summary <- df %>%
  filter(value > 0) %>%
  group_by(id) %>%
  summarize(mean_value = mean(value))
