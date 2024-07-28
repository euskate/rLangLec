# 데이터 생성
df <- data.frame(id = 1:10, phone_number = c("123-456-7890", "987-654-3210", "555-555-5555", "111-222-3333", "444-555-6666"))

# 전화번호 마스킹
df$masked_phone_number <- sub("\\d{3}-\\d{3}-", "XXX-XXX-", df$phone_number)

# 결과 출력
print(df)
