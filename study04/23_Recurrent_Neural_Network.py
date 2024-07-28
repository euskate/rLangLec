import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense, Embedding
from tensorflow.keras.callbacks import EarlyStopping

# 1. 라이브러리 및 데이터 로드
# IMDB 데이터셋 로드
max_features = 10000  # 단어 사전의 최대 크기
maxlen = 100  # 시퀀스 길이

(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features)

print(f"Training data shape: {x_train.shape}")
print(f"Testing data shape: {x_test.shape}")

# 2. 데이터 전처리
# 시퀀스 길이를 맞추기 위해 패딩 추가
x_train = pad_sequences(x_train, maxlen=maxlen)
x_test = pad_sequences(x_test, maxlen=maxlen)

# 3. RNN 모델 정의
def create_rnn_model(input_shape, num_classes):
    model = Sequential()
    
    # 임베딩 층
    model.add(Embedding(input_dim=max_features, output_dim=128, input_length=input_shape[0]))
    
    # RNN 층
    model.add(SimpleRNN(64, activation='tanh'))
    
    # 출력층
    model.add(Dense(num_classes, activation='sigmoid'))
    
    # 모델 컴파일
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

# 모델 생성
input_shape = (maxlen,)  # 입력 시퀀스의 길이
num_classes = 1  # 이진 분류
model = create_rnn_model(input_shape, num_classes)

# 4. 모델 훈련 및 평가
# 조기 종료 콜백
early_stopping = EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True)

# 모델 훈련
history = model.fit(x_train, y_train, 
                    epochs=10, 
                    batch_size=64, 
                    validation_split=0.2, 
                    callbacks=[early_stopping])

# 모델 평가
test_loss, test_accuracy = model.evaluate(x_test, y_test, verbose=0)
print(f"Test Loss: {test_loss:.4f}")
print(f"Test Accuracy: {test_accuracy:.4f}")

# 훈련 과정 시각화 (선택 사항)
import matplotlib.pyplot as plt

plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label='val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.ylim([0, 1])
plt.legend(loc='lower right')
plt.show()
