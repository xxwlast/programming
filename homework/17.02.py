import random

def read(n):
    with open(n, encoding="utf-8") as f:
        t = f.read()
        a = t.split('\n')
    return a

def splitt(r):
    dict = {}
    for i in r:
        a = i.split(',')

        dict[a[0]] = a[1:]
    return dict

def word(d):
    words = list(d.keys())
    word = random.choice(words)
    random_w = random.choice(d[word])
    print(random_w)
    kus = input("Загаданное слово: ")
    r = 4
    for i in range(6):
            if kus == word:
                print("Ура, это победа")
                break
            else:
                print
                print(random.choice(d[word]))
                r = r - 1
                kus = input("Еще раз:")
                if r > 0:
                    print(" ")
                    print("У тебя осталось попыток до  лимита в 3 попытки:", r)
                    
                else:
                    print(' ')
                    print("мяк")
    

def main():
    word(splitt(read("sable.txt")))

if __name__ == "__main__":
    main()

