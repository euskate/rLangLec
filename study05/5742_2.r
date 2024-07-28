# 다중 반환값을 가진 함수 정의
calc_stats <- function(x) {
  mean_val <- mean(x)
  sd_val <- sd(x)
  return(list(mean=mean_val, sd=sd_val))
}

# 함수 호출
stats <- calc_stats(c(1, 2, 3, 4, 5))
print(stats$mean)
print(stats$sd)
