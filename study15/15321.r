install.packages("openssl")
library(openssl)

# 데이터 암호화 및 해독
# 암호화 키 생성
key <- rand_bytes(32)
iv <- rand_bytes(16)

# 데이터 암호화
plain_text <- "This is a secret message."
cipher_text <- aes_cbc_encrypt(charToRaw(plain_text), key = key, iv = iv)

# 암호화된 데이터 출력
print(cipher_text)

# 데이터 해독
decrypted_text <- rawToChar(aes_cbc_decrypt(cipher_text, key = key, iv = iv))
print(decrypted_text)
