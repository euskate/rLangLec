# 필요한 패키지 설치 및 로드
install.packages(c("tm", "topicmodels"))
library(tm)
library(topicmodels)

# 데이터 생성
texts <- c("Data science is an interdisciplinary field.",
            "Machine learning involves training algorithms.",
            "Big data is analyzed using statistical techniques.")

# Corpus 및 Document-Term Matrix 생성
corpus <- Corpus(VectorSource(texts))
corpus <- tm_map(corpus, content_transformer(tolower))
corpus <- tm_map(corpus, removePunctuation)
corpus <- tm_map(corpus, removeNumbers)
corpus <- tm_map(corpus, removeWords, stopwords("en"))
corpus <- tm_map(corpus, stripWhitespace)

dtm <- DocumentTermMatrix(corpus)

# LDA 모델 생성
lda_model <- LDA(dtm, k = 2)  # k는 주제의 수

# 결과 요약
topics <- terms(lda_model, 5)
print(topics)

# 문서-주제 확률
doc_topics <- posterior(lda_model)$topics
print(doc_topics)
