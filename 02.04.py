#[\w.-] - выбрать все буквы \w, тире и точки (все записано в квадратные скобки
 # и значит то, что значит)

 # [\w.-] - любое слово, ключая тире и .
 # + @ - далее @
 # [\w.-] - снова любое слово
 # \.\w+ - + точка (\ перед .  нужно,
 # чтоб программа воспринимала ее как точку а не "любой символ"
import re

def check_email():
    user_input = input("Введите email\n")
    match_result = re.match('[\w.-]+@[\w.-]+\.\w+', user_input)
    if match_result:
        print("Cпасибо")
    else:
        print("sosi")


check_email()


def check_first():
    [
