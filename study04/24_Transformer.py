import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense, Embedding, Dropout, Add, LayerNormalization
from tensorflow.keras.layers import MultiHeadAttention, GlobalAveragePooling1D
from tensorflow.keras.optimizers import Adam
import matplotlib.pyplot as plt

# 1. 라이브러리 및 데이터 로드
max_features = 10000  # 단어 사전의 최대 크기
maxlen = 100  # 시퀀스 길이

(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features)

print(f"Training data shape: {x_train.shape}")
print(f"Testing data shape: {x_test.shape}")

# 2. 데이터 전처리
# 시퀀스 길이를 맞추기 위해 패딩 추가
x_train = pad_sequences(x_train, maxlen=maxlen)
x_test = pad_sequences(x_test, maxlen=maxlen)

# 3. Transformer 인코더 정의
def transformer_encoder(inputs, head_size, num_heads, ff_dim, dropout=0):
    # 셀프 어텐션 층
    x = MultiHeadAttention(
        key_dim=head_size, 
        num_heads=num_heads
    )(inputs, inputs)
    x = Dropout(dropout)(x)
    x = Add()([x, inputs])
    x = LayerNormalization(epsilon=1e-6)(x)
    
    # 피드포워드 네트워크
    x_ff = Dense(ff_dim, activation="relu")(x)
    x_ff = Dense(inputs.shape[-1])(x_ff)
    x_ff = Dropout(dropout)(x_ff)
    x = Add()([x_ff, x])
    x = LayerNormalization(epsilon=1e-6)(x)
    
    return x

def create_transformer_model(input_shape, num_classes, head_size, num_heads, ff_dim, num_transformer_blocks, dropout=0):
    inputs = Input(shape=input_shape)
    
    # 임베딩 층
    x = Embedding(input_dim=max_features, output_dim=128, input_length=input_shape[0])(inputs)
    
    # Transformer 인코더 블록
    for _ in range(num_transformer_blocks):
        x = transformer_encoder(x, head_size, num_heads, ff_dim, dropout)
    
    # 풀링 및 출력층
    x = GlobalAveragePooling1D()(x)
    x = Dense(128, activation="relu")(x)
    x = Dropout(dropout)(x)
    outputs = Dense(num_classes, activation="sigmoid")(x)
    
    model = Model(inputs, outputs)
    return model

# 모델 파라미터 설정
input_shape = (maxlen,)  # 입력 시퀀스의 길이
num_classes = 1  # 이진 분류
head_size = 64
num_heads = 4
ff_dim = 32
num_transformer_blocks = 2
dropout = 0.1

# 모델 생성
model = create_transformer_model(input_shape, num_classes, head_size, num_heads, ff_dim, num_transformer_blocks, dropout)

# 모델 컴파일
model.compile(optimizer=Adam(), loss='binary_crossentropy', metrics=['accuracy'])

# 4. 모델 훈련 및 평가
# 조기 종료 콜백
early_stopping = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True)

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
plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label='val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.ylim([0, 1])
plt.legend(loc='lower right')
plt.show()
