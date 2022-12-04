import random

class Alphabet:
    def __init__(self, language):
        self.language = language
        self.id = -1
        if self.language == 'en':
            self.alp = range(ord('a'), ord('z')+1)
            
        elif self.language == 'ru':
            self.alp = list(range(ord('а'), ord('я')+1))
            

    def __iter__(self):
        return self

    def __next__(self):
        self.id += 1
        if self.id > len(self.alp)-1:
            self.id = 0
        return chr(self.alp[self.id])



en_alpha = Alphabet('en')

letters = [next(en_alpha) for _ in range(28)]

print(*letters)