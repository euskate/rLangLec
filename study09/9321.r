# 패키지 설치 및 로드
install.packages("topicmodels")
library(topicmodels)

# LDA 모델 생성
lda_model <- LDA(dtm, k = 2)  # k는 주제의 수

# 결과 요약
topics <- terms(lda_model, 5)  # 각 주제에서 가장 중요한 5개의 단어
print(topics)

# 문서-주제 확률
doc_topics <- posterior(lda_model)$topics
print(doc_topics)
