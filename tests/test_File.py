from code.lib import File
from code.lib import NLP

def test_get_history():
    print(f"\ntest:get_history()")
    File.history_init()
    
    print("searching... word='given'")
    NLP.search_word("given", File.get_fileName())
    print("searching... word='the'")
    NLP.search_word("the", File.get_fileName())
    history = File.get_history()
    print(f"search history:{history}")
    File.history_init()
    
def main():
    test_get_history()