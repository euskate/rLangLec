import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules
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

te = TransactionEncoder()
te_ary = te.fit(df['Items']).transform(df['Items'])
df_encoded = pd.DataFrame(te_ary, columns=te.columns_)

# 2. Apriori 알고리즘 적용
frequent_itemsets = apriori(df_encoded, min_support=0.3, use_colnames=True)

# 3. 연관 규칙 생성
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)

# 4. 결과 분석 및 시각화
top_rules = rules.sort_values(by='confidence', ascending=False).head(10)

plt.figure(figsize=(12, 8))
sns.scatterplot(x='support', y='confidence', size='lift', hue='lift', data=top_rules, palette='viridis', sizes=(50, 200))
plt.title('Association Rules - Support vs Confidence')
plt.xlabel('Support')
plt.ylabel('Confidence')
plt.legend(loc='best')
plt.show()
