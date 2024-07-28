import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules, fpgrowth

# 1. 데이터 준비
dataset = [
    ['Milk', 'Bread', 'Butter'],
    ['Milk', 'Bread'],
    ['Milk', 'Butter'],
    ['Bread', 'Butter'],
    ['Milk', 'Bread', 'Butter', 'Cheese'],
]

# TransactionEncoder를 사용하여 데이터를 변환
te = TransactionEncoder()
te_ary = te.fit_transform(dataset)
df = pd.DataFrame(te_ary, columns=te.columns_)
print("Transaction DataFrame:")
print(df)

# 2. Apriori 알고리즘
frequent_itemsets = apriori(df, min_support=0.6, use_colnames=True)
print("\nFrequent Itemsets (Apriori):")
print(frequent_itemsets)

# 3. 연관 규칙 생성
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)
print("\nAssociation Rules:")
print(rules)

# 4. FP-Growth 알고리즘
frequent_itemsets_fp = fpgrowth(df, min_support=0.6, use_colnames=True)
print("\nFrequent Itemsets (FP-Growth):")
print(frequent_itemsets_fp)
