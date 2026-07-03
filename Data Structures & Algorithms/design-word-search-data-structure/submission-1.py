class WordDictionary:

    def __init__(self):
        self.words = []
        

    def addWord(self, word: str) -> None:
        self.words.append(word)

    
        

    def search(self, word: str) -> bool:
        matched_words = [w for w in self.words if re.fullmatch(word, w)]
        print(matched_words)
        if len(matched_words) > 0:
            return True
        return False
        
