library(sparklyr)
sc <- spark_connect(master = "local")
sdf <- sdf_copy_to(sc, df, overwrite = TRUE)
spark_summary <- sdf %>%
  filter(value > 0) %>%
  group_by(id) %>%
  summarize(mean_value = mean(value))
collect(spark_summary)
