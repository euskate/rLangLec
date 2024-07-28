# 데이터 프레임 생성
df <- data.frame(Name=c("Alice", "Bob", "Charlie"), Age=c(25, 30, 35), Score=c(90, 85, 88))

# 데이터 프레임 출력
print(df)

# 데이터 프레임의 특정 열 접근
print(df$Name)

# 데이터 프레임의 특정 행 접근
print(df[2, ])