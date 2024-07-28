library(future.apply)
plan(multicore) # 멀티코어 설정
results <- future_lapply(1:10, function(x) {Sys.sleep(1); x^2})
