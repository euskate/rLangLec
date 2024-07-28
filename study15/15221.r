install.packages("anonymizer")
library(anonymizer)

# 데이터 생성
df <- data.frame(id = 1:10, name = c("Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah", "Ivy", "Jack"), age = 20:29)

# 데이터 익명화
anonymized_df <- anonymize(df, columns = c("name"))

# 익명화된 데이터 출력
print(anonymized_df)
