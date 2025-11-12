words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}

def test(word):
    for a, b in word.items():
        print(a * b)
test(words)
