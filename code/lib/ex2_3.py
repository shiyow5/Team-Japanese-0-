import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency

# サンプルデータ
corpus1 = {'word1': 50, 'word2': 30, 'word3': 20}
corpus2 = {'word1': 30, 'word2': 50, 'word3': 10}

# キー性の計算（対数尤度）
def calculate_keyness(corpus1, corpus2):
    keyness_scores = {}
    total1 = sum(corpus1.values())
    total2 = sum(corpus2.values())
    
    for word in set(corpus1.keys()).union(set(corpus2.keys())):
        f1 = corpus1.get(word, 0)
        f2 = corpus2.get(word, 0)
        E1 = total1 * (f1 + f2) / (total1 + total2)
        E2 = total2 * (f1 + f2) / (total1 + total2)
        
        if f1 == 0:
            LL1 = 0
        else:
            LL1 = 2 * f1 * np.log(f1 / E1)
            
        if f2 == 0:
            LL2 = 0
        else:
            LL2 = 2 * f2 * np.log(f2 / E2)
        
        LL = LL1 + LL2
        keyness_scores[word] = LL
        
    return keyness_scores

# 効果量の計算（オッズ比）
def calculate_odds_ratio(corpus1, corpus2):
    odds_ratios = {}
    
    for word in set(corpus1.keys()).union(set(corpus2.keys())):
        f1 = corpus1.get(word, 0)
        f2 = corpus2.get(word, 0)
        not_f1 = sum(corpus1.values()) - f1
        not_f2 = sum(corpus2.values()) - f2
        
        odds_ratio = (f1 / not_f1) / (f2 / not_f2) if not_f1 != 0 and not_f2 != 0 else 0
        odds_ratios[word] = odds_ratio
    
    return odds_ratios

# 結果表示
def display_results(keyness_scores, odds_ratios, sort_by='keyness', ascending=False):
    df = pd.DataFrame({
        'Keyness': keyness_scores,
        'OddsRatio': odds_ratios
    }).sort_values(by=sort_by.capitalize(), ascending=ascending)
    
    print(df)

# 計算実行
keyness_scores = calculate_keyness(corpus1, corpus2)
odds_ratios = calculate_odds_ratio(corpus1, corpus2)

# 結果表示
display_results(keyness_scores, odds_ratios, sort_by='Keyness', ascending=False)
