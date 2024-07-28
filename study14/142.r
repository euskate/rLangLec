install.packages("arulesViz")  # 설치 및 로드
library(arulesViz)

plot(rules_filtered, method="scatter", measure=c("support", "confidence"), shading="lift")   # Scatter Plot 시각화 : 규칙의 신뢰도와 지지도 간의 관계를 시각화합니다.
plot(head(sort(rules_filtered, by="lift"), 10), method="graph")  # Top Rules 시각화 : 신뢰도 또는 지지도에 따라 상위 규칙을 시각화합니다.

# Interactive Plot 시각화 : plotly를 사용하여 상호작용 가능한 그래프를 생성합니다.
install.packages("plotly")
library(plotly)

plot_ly(data=as(rules_filtered, "data.frame"), x=~support, y=~confidence, text=~paste("Rule: ", labels), type="scatter", mode="markers", color=~lift, colors="Viridis") %>%
  layout(title="Interactive Association Rules",
         xaxis=list(title="Support"),
         yaxis=list(title="Confidence"))
