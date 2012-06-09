from pwphrase import *

if __name__ == '__main__':
    run()

def run():
    print random_phrase(read_words('/usr/share/dict/words'), 4)
