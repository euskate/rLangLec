import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import fpgrowth
import matplotlib.pyplot as plt
import seaborn as sns

# 1. 데이터 준비
data = {
    'Transaction': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Items': [
        ['Milk', 'Bread'],
        ['Milk', 'Diaper', 'Beer', 'Bread'],
        ['Milk', 'Diaper', 'Beer'],
        ['Diaper', 'Beer'],
        ['Milk', 'Bread'],
        ['Milk', 'Diaper', 'Bread'],
        ['Milk', 'Diaper', 'Beer', 'Bread'],
        ['Beer', 'Bread'],
        ['Milk', 'Diaper', 'Bread'],
        ['Milk', 'Bread']
    ]
}

df = pd.DataFrame(data)

# 2. 데이터 전처리
te = TransactionEncoder()
te_ary = te.fit(df['Items']).transform(df['Items'])
df_encoded = pd.DataFrame(te_ary, columns=te.columns_)

# 3. FP-Growth 알고리즘 적용
frequent_itemsets = fpgrowth(df_encoded, min_support=0.3, use_colnames=True)

print(frequent_itemsets)

# 4. 결과 분석 및 시각화
top_itemsets = frequent_itemsets.sort_values(by='support', ascending=False).head(10)

plt.figure(figsize=(12, 8))
sns.barplot(x='support', y='itemsets', data=top_itemsets, palette='viridis')
plt.title('Top 10 Frequent Itemsets')
plt.xlabel('Support')
plt.ylabel('Itemsets')
plt.show()
