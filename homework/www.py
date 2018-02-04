inp = input("Введите слово:")

def t():
    with open("q.txt", encoding = "utf-8") as f:
        t = f.read().lower()
        text = t.split(" ")
    print(word_freq())
    print(word_omni())
    return t

def word_freq():
    text = t()
    freq = {}
    for inp in text:
        if inp in freq :
            freq[inp] += 1 / len(text)
        else:
            freq[inp] = 1 / len(text)
    return freq

def word_omni():
    text = t()
    omni = {}
    for inp in text:
        if inp.startswith("omni") in omni:
            omni[inp] += 1 / len(text)
        else:
            omni[inp] = 1 / len(text)
    return omni

print(t())

