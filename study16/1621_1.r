install.packages("rvest")
library(rvest)

# 웹 페이지 읽기
url <- "https://example.com"
web_page <- read_html(url)

# 데이터 추출
title <- web_page %>%
  html_node("title") %>%
  html_text()

print(title)
