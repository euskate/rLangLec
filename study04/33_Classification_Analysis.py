import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

# 1. 데이터 준비
iris = load_iris()
X = iris.data
y = iris.target
feature_names = iris.feature_names
target_names = iris.target_names

df = pd.DataFrame(X, columns=feature_names)
df['target'] = y

# 데이터 시각화
sns.pairplot(df, hue='target', palette='Dark2', diag_kind='kde')
plt.show()

# 데이터 전처리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 2. 로지스틱 회귀
log_reg = LogisticRegression(max_iter=200)
log_reg.fit(X_train, y_train)
y_pred_log_reg = log_reg.predict(X_test)
print("Logistic Regression")
print("Accuracy:", accuracy_score(y_test, y_pred_log_reg))
print("Classification Report:\n", classification_report(y_test, y_pred_log_reg, target_names=target_names))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_log_reg))

# 3. 결정 트리
dec_tree = DecisionTreeClassifier()
dec_tree.fit(X_train, y_train)
y_pred_dec_tree = dec_tree.predict(X_test)
print("\nDecision Tree")
print("Accuracy:", accuracy_score(y_test, y_pred_dec_tree))
print("Classification Report:\n", classification_report(y_test, y_pred_dec_tree, target_names=target_names))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_dec_tree))

# 4. 랜덤 포레스트
random_forest = RandomForestClassifier(n_estimators=100, random_state=0)
random_forest.fit(X_train, y_train)
y_pred_rf = random_forest.predict(X_test)
print("\nRandom Forest")
print("Accuracy:", accuracy_score(y_test, y_pred_rf))
print("Classification Report:\n", classification_report(y_test, y_pred_rf, target_names=target_names))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_rf))

# 5. 서포트 벡터 머신
svm = SVC(kernel='linear', random_state=0)
svm.fit(X_train, y_train)
y_pred_svm = svm.predict(X_test)
print("\nSupport Vector Machine")
print("Accuracy:", accuracy_score(y_test, y_pred_svm))
print("Classification Report:\n", classification_report(y_test, y_pred_svm, target_names=target_names))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_svm))

# 6. K-최근접 이웃
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred_knn = knn.predict(X_test)
print("\nK-Nearest Neighbors")
print("Accuracy:", accuracy_score(y_test, y_pred_knn))
print("Classification Report:\n", classification_report(y_test, y_pred_knn, target_names=target_names))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_knn))
