# 필수 라이브러리 가져오기
import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# 데이터 불러오기
df = pd.read_csv('https://raw.githubusercontent.com/zzhining/python_ml_dl/main/dataset/concrete.csv')


# 데이터 확인
print(df.shape)
print(df.head())

# 특성과 레이블 분리
X = df.drop(columns=['CompressiveStrength'])  # 입력 데이터 (특성)
y = df['CompressiveStrength']  # 출력 데이터 (레이블)

# 2. 훈련과 테스트 세트로 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. 데이터 표준화 (StandardScaler 사용)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)






# 4. 인공신경망(ANN) 모델 생성
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(X_train_scaled.shape[1],)),  # 첫 번째 은닉층
    tf.keras.layers.Dense(32, activation='relu'),  # 두 번째 은닉층
    # 출력층 (회귀 문제이므로 출력 뉴런은 1개, 분류문제면 타켓 개수 만큼 설정.)
    tf.keras.layers.Dense(1)  
    
])

# 5. 모델 컴파일
model.compile(optimizer='adam', loss='mse')

#조기종료 설정
early_stopping = tf.keras.callbacks.EarlyStopping(
   monitor='val_loss', 
   patience=10, 
   restore_best_weights=True
)

# 6. 모델 학습 - 학습결과를 history변수에 저장
history = model.fit(
   X_train_scaled, 
   y_train, 
   epochs=100, 
   validation_split=0.2,
   callbacks=[early_stopping]
)

# # 7. 학습 결과 시각화 (loss와 val_loss 그래프)
plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Model Loss')
plt.ylabel('Loss (MSE)')
plt.xlabel('Epochs')
plt.legend()
plt.show()

# # 8. 테스트 데이터로 모델 평가
y_pred = model.predict(X_test_scaled)

# # 9. MSE(평균 제곱 오차) 계산
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# # 10. 실제 값과 예측 값 비교
comparison_df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred.flatten()})
print(comparison_df.head())


model.save('concrete_strength_model.keras')
