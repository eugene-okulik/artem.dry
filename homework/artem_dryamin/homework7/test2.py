words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}


def new_function(word):
    for a, b in word.items():
        print(a * b)
        
new_function(words)
