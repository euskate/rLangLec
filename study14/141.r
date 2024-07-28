install.packages("arules")
library(arules)

# 예제 데이터 로드
data("Groceries")
head(Groceries)

# 연관 규칙 생성 : apriori 함수를 사용하여 연관 규칙을 생성합니다. 이 함수는 최소 지지도(support)와 최소 신뢰도(confidence)를 기준으로 규칙을 생성합니다.
rules <- apriori(Groceries, parameter=list(support=0.005, confidence=0.5))
inspect(rules)

# 특정 규칙 필터링 : 불필요한 규칙을 제거하기 위해 subset 함수를 사용할 수 있습니다.
rules_filtered <- subset(rules, subset = lift > 1)
inspect(rules_filtered)

install.packages("arulesViz")  # 규칙 시각화 : arulesViz 패키지를 사용하여 규칙을 시각화할 수 있습니다.
library(arulesViz)

# 그래프 시각화
plot(rules_filtered, method="graph")
