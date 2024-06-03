import numpy as np
import pandas as pd
from . import NLP
from . import File

# Calculate loglikelihood
def loglikelihood(f1, f2, n1, n2):
    E1 = n1 * (f1 + f2) / (n1 + n2)
    E2 = n2 * (f1 + f2) / (n1 + n2)
    G2 = 2 * ((f1 * np.log(f1 / E1) if f1 > 0 else 0) + (f2 * np.log(f2 / E2) if f2 > 0 else 0))
    return G2

# Calculate Odds Ratio
def odds_ratio(N1, N2, T1, T2):
    odds1 = N1 / (T1 - N1)
    odds2 = N2 / (T2 - N2)
    ratio = odds1 / odds2 if odds2 > 0 else float('inf')
    return ratio

def keyness(target_freq, reference_freq):
    # Total number of words in each corpus
    total_target = sum(target_freq.values())
    total_reference = sum(reference_freq.values())

    # Calculate loglikelihood and effect size for each word in the target corpus
    results = []
    for word in target_freq.keys():
        target_count = target_freq.get(word, 0)
        ref_count = reference_freq.get(word, 0)
    
        # Loglikelihood
        ll = loglikelihood(target_count, ref_count, total_target, total_reference)
    
        # Effect size (Odds Ratio)
        effect_size = odds_ratio(target_count, ref_count, total_target, total_reference)
    
        results.append((word, target_count, ref_count, ll, effect_size))

    # Sort results by loglikelihood value
    results.sort(key=lambda x: x[3], reverse=True)
    
    # results to dataframe
    df = pd.DataFrame(columns=['Target Freq', 'Reference Freq', 'LL', 'Odds Ratio'])
    for result in results:
        df.loc[result[0]] = [int(result[1]), int(result[2]), f"{result[3]:.2f}", f"{result[4]:.2f}"]
        
    return df

def main():
    # Load and tokenize the corpora
    target_freq = NLP.frequency(text=File.get_sentence('Q1'), word_identify=True)
    reference_freq = NLP.frequency(text=File.get_sentence('K1'), word_identify=True)
    
    result = keyness(target_freq, reference_freq)
    print(result)