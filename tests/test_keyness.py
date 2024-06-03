from code.lib import File
from code.lib import NLP
from code.lib import keyness
import pandas as pd

def test_keynss():
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_colwidth', None)
    pd.set_option('expand_frame_repr', False)
    
    print(f"\ntest:keyness()\ntarget='Q1', reference='K1'")
    # Load and tokenize the corpora
    target_freq = NLP.frequency(text=File.get_sentence('Q1'), word_identify=True)
    reference_freq = NLP.frequency(text=File.get_sentence('K1'), word_identify=True)
    
    result = keyness.keyness(target_freq, reference_freq)
    print(result)
    
def main():
    test_keynss()