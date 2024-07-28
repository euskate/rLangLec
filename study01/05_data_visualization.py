import matplotlib.pyplot as plt
import seaborn as sns

# 제목 빈도수 시각화
plt.figure(figsize=(10, 6))
sns.countplot(y='title', data=data, order=data['title'].value_counts().index)
plt.title("Title Frequency")
plt.xlabel("Frequency")
plt.ylabel("Title")
plt.show()
