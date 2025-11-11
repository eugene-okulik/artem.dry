text = ("Etiam tincidunt neque erat, quis molestie enim imperdiet vel. "
        "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero")
new_text = text.split()
lol = []
for tex in new_text:
    if tex.endswith(','):
        word = tex[:-1] + 'ing,'
    elif tex.endswith('.'):
        word = tex[:-1] + 'ing.'
    else:
        word = tex + 'ing'
    lol.append(word)
lol = ' '.join(lol)
print(lol)
