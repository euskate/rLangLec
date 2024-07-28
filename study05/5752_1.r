# 데이터 프레임 생성
data <- data.frame(Name=c("Alice", "Bob"), Age=c(25, 30))

# CSV 파일 쓰기
write.csv(data, "output.csv", row.names=FALSE)
