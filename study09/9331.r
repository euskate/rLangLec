# 패키지 설치 및 로드
install.packages("textmineR")
library(textmineR)

# LDA 모델 생성
lda_model <- FitLdaModel(dtm, k = 2, iterations = 1000, burnin = 100, seed = 123)

# 결과 요약
print(lda_model$phi)  # 주제-단어 분포
print(lda_model$theta)  # 문서-주제 분포

# NMF 모델 생성
nmf_model <- FitNmfModel(dtm, k = 2, iterations = 1000, seed = 123)

# 결과 요약
print(nmf_model$W)  # 주제-단어 행렬
print(nmf_model$H)  # 문서-주제 행렬
