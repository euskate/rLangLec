# 패키지 설치 및 로드
install.packages("plotly")
library(plotly)

# 기본 산점도
plot_ly(data = mtcars, x = ~wt, y = ~mpg, type = 'scatter', mode = 'markers') %>%
  layout(title = 'Weight vs. MPG', xaxis = list(title = 'Weight'), yaxis = list(title = 'MPG'))

# 히스토그램
plot_ly(data = mtcars, x = ~mpg, type = 'histogram') %>%
  layout(title = 'Histogram of MPG', xaxis = list(title = 'MPG'), yaxis = list(title = 'Frequency'))

# 박스플롯
plot_ly(data = mtcars, y = ~mpg, x = ~factor(cyl), type = 'box') %>%
  layout(title = 'Boxplot of MPG by Cylinder', xaxis = list(title = 'Cylinder'), yaxis = list(title = 'MPG'))
