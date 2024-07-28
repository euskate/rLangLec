# 패키지 설치 및 로드
install.packages("tm")
library(tm)

# 데이터 생성
texts <- c("Text mining is a powerful tool.",
            "Topic modeling helps in discovering the topics.",
            "Text analytics involves processing and analyzing text data.")

# Corpus 생성
corpus <- Corpus(VectorSource(texts))

# 전처리
corpus <- tm_map(corpus, content_transformer(tolower))
corpus <- tm_map(corpus, removePunctuation)
corpus <- tm_map(corpus, removeNumbers)
corpus <- tm_map(corpus, removeWords, stopwords("en"))
corpus <- tm_map(corpus, stripWhitespace)

# Document-Term Matrix 생성
dtm <- DocumentTermMatrix(corpus)
