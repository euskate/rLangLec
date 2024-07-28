install.packages("anonymizer")
library(anonymizer)

# 데이터 익명화
# 데이터 생성
df <- data.frame(id = 1:10, name = letters[1:10], age = 20:29)

# 익명화
anonymized_df <- anonymize(df, columns = c("name"))

# 결과 보기
print(anonymized_df)
