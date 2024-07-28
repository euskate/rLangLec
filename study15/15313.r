install.packages("sparklyr")
library(sparklyr)

# Apache Spark와의 연결
# Spark 클러스터 연결
sc <- spark_connect(master = "local")

# 데이터프레임을 Spark 데이터프레임으로 변환
spark_df <- sdf_copy_to(sc, df, overwrite = TRUE)

# 데이터 전처리
spark_result <- spark_df %>%
  filter(value > 0) %>%
  mutate(squared_value = value^2) %>%
  group_by(id) %>%
  summarize(mean_value = mean(squared_value))

# 결과 보기
collect(spark_result)
