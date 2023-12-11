import random

import requests


class WordlWordsGenerator:

    english_words = None

    def __init__(self):
        url = "https://www.mit.edu/~ecprice/wordlist.100000"
        response = requests.get(url)
        self.english_words = [word.strip() for word in response.text.splitlines() if len(word.strip()) == 5]
        return

    def generate_real_word(self):
        word = random.choice(list(self.english_words))
        while len(word) != 5:
            word = random.choice(list(self.english_words))
        return word

    def generate(self, rounds):
        return [
            [self.generate_real_word() for _ in range(6)]
            for _ in range(rounds)
        ]
