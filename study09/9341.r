# 패키지 설치 및 로드
install.packages("text2vec")
library(text2vec)

# 데이터 전처리
tokens <- word_tokenizer(texts)
vectorizer <- vocab_vectorizer(vocabulary = vocab$terms)
dtm <- create_dtm(itoken(tokens), vectorizer)

# LDA 모델 생성
lda_model <- LDA(dtm, K = 2, control = list(seed = 123))

# 결과 요약
print(terms(lda_model, 5))  # 각 주제에서 가장 중요한 5개의 단어
