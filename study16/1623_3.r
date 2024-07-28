install.packages("sparklyr")
library(sparklyr)

# Spark 클러스터 연결
sc <- spark_connect(master = "local")

# 데이터 프레임을 Spark 데이터프레임으로 변환
spark_df <- sdf_copy_to(sc, df, overwrite = TRUE)

# 데이터 처리
spark_summary <- spark_df %>%
  filter(value > 0) %>%
  group_by(id) %>%
  summarize(mean_value = mean(value))

# 결과 수집
result <- collect(spark_summary)
print(result)

# Spark 연결 종료
spark_disconnect(sc)
