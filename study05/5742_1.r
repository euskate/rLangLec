# 기본값 인수를 가진 함수 정의
greet <- function(name="Guest") {
  message <- paste("안녕하세요,", name)
  return(message)
}

# 함수 호출
print(greet())
print(greet("Alice"))
