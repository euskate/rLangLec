import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

# 예제 데이터 생성
np.random.seed(0)
data1 = np.random.normal(loc=50, scale=10, size=100)  # 정규 분포를 따르는 데이터
data2 = np.random.normal(loc=55, scale=15, size=100)  # 정규 분포를 따르는 다른 데이터

# 데이터프레임 생성
df = pd.DataFrame({
    'Group1': data1,
    'Group2': data2
})

# 1. 기술 통계

print("기술 통계:")
print(df.describe())  # 데이터프레임의 기본 통계 정보 출력

# 평균, 중앙값, 최빈값
mean_group1 = np.mean(df['Group1'])
median_group1 = np.median(df['Group1'])
mode_group1 = stats.mode(df['Group1'])[0][0]

mean_group2 = np.mean(df['Group2'])
median_group2 = np.median(df['Group2'])
mode_group2 = stats.mode(df['Group2'])[0][0]

print("\nGroup1 - 평균: {:.2f}, 중앙값: {:.2f}, 최빈값: {:.2f}".format(mean_group1, median_group1, mode_group1))
print("Group2 - 평균: {:.2f}, 중앙값: {:.2f}, 최빈값: {:.2f}".format(mean_group2, median_group2, mode_group2))

# 표준 편차, 분산
std_dev_group1 = np.std(df['Group1'], ddof=1)
variance_group1 = np.var(df['Group1'], ddof=1)

std_dev_group2 = np.std(df['Group2'], ddof=1)
variance_group2 = np.var(df['Group2'], ddof=1)

print("\nGroup1 - 표준 편차: {:.2f}, 분산: {:.2f}".format(std_dev_group1, variance_group1))
print("Group2 - 표준 편차: {:.2f}, 분산: {:.2f}".format(std_dev_group2, variance_group2))

# 히스토그램 및 상자 그림 시각화
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
sns.histplot(df['Group1'], kde=True, color='blue')
plt.title('Group1 히스토그램')

plt.subplot(1, 2, 2)
sns.histplot(df['Group2'], kde=True, color='red')
plt.title('Group2 히스토그램')

plt.show()

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
sns.boxplot(df['Group1'], color='blue')
plt.title('Group1 상자 그림')

plt.subplot(1, 2, 2)
sns.boxplot(df['Group2'], color='red')
plt.title('Group2 상자 그림')

plt.show()

# 2. 추론 통계

# 가설 검정 (t-검정)
t_stat, p_value = stats.ttest_ind(df['Group1'], df['Group2'])

print("\nT-검정 결과:")
print("t-값: {:.2f}".format(t_stat))
print("p-값: {:.3f}".format(p_value))

# ANOVA (분산 분석)
f_stat, p_value_anova = stats.f_oneway(df['Group1'], df['Group2'])

print("\nANOVA 결과:")
print("F-값: {:.2f}".format(f_stat))
print("p-값: {:.3f}".format(p_value_anova))

# 신뢰 구간 계산
conf_interval_group1 = stats.t.interval(0.95, len(df['Group1'])-1, loc=np.mean(df['Group1']), scale=stats.sem(df['Group1']))
conf_interval_group2 = stats.t.interval(0.95, len(df['Group2'])-1, loc=np.mean(df['Group2']), scale=stats.sem(df['Group2']))

print("\n신뢰 구간:")
print("Group1 95% 신뢰 구간: [{:.2f}, {:.2f}]".format(conf_interval_group1[0], conf_interval_group1[1]))
print("Group2 95% 신뢰 구간: [{:.2f}, {:.2f}]".format(conf_interval_group2[0], conf_interval_group2[1]))
