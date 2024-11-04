class Robot:
    def __init__(self):
        self.known_words = [
            'thank',
            'you',
            'for',
            'teaching',
            'me',
            'i',
            'already',
            'know',
            'the',
            'word',
            'do',
            'not',
            'understand',
            'input'
        ]

    def learn_word(self, word):
        if not word.isalpha():
            return "I do not understand the input"
        
        word_lower = word.lower()
        
        if word_lower in self.known_words:
            return f"I already know the word {word}"
        
        self.known_words.append(word_lower)
        return f"Thank you for teaching me {word}"