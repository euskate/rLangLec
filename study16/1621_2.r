install.packages("httr")
library(httr)

# API 요청
response <- GET("https://api.example.com/data")
data <- content(response, "parsed")

print(data)
