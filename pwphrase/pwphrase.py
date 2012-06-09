import re
import Crypto.Random.random



_word_re = re.compile('^([a-z]{4,8})$')

def read_words(path):
    words = []
    for line in open(path, 'r'):
        match = _word_re.match(line)
        if match:
            words.append(match.groups()[0])
    return words

def pick_word(words):
    return Crypto.Random.random.choice(words)

def random_phrase(words, n):
    return ' '.join([pick_word(words) for i in range(n)])


