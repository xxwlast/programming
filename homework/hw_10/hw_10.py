import re

def first(e):
    match = re.search(r'Отряд(.*?)>(.*?)<"', e, flags=re.DOTALL)
    if match:
        print(match.group(2))
    else:
        print("У меня как обычно ничего не вышло")
     
        
def second(n):
    with open(n, encoding="UTF-8") as f:
       t = f.read()
    return t

def main():
    (second(first(input("Введи название текста: (всё равно ничего нормального не выдаст)"))))
    
if __name__ == "__main__":
    main()
