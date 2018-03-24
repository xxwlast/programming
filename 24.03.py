import re

def clean_phone(text):
    digits = re.findall(r'\d', text)
    return ''.join(digits)

def clean_phone_re(text):
    return re.sub(r'\D', '', text)

# \D - without letters (only numbers)

phone = "+7 (985) 123-45-67"
print(clean_phone(phone))
print(clean_phone_re(phone))

s = 'abc def'
print(s.replace('abc', 'ABC'))
print(re.sub('abc', 'ABC', s))
      # re.sub & s.replace заменяют что-то на другое :
      # s.replace("то что есть","то, на что надо заменить")

print(re.sub(r'\w+', 'X', s))
#вот это хз что

print(re.sub(r'x*', "_", s, count=2))
# count = максимальное кол-во раз, которые мы хотим сделать замену

s = "Национальный исследовательский университет Высшая Школа Экономики"
#оставить от каждого слова только первую букву 
result = re.search(
    r'\s*(\w)\w+\s*',
    s
    )

print(result.group(), result.groups())

short = re.sub(
    r'\s*(\w)\w+\s*',
    r'\1',
    s
    )
print(short)

#s = '''Меня зовут <b>Поля!!!</b>
#Меня зовут <b>Сюсь</b>'''
#names = re.sub(r'Меня зовут <b>(\w+)</b>',
#       r'\1'
#       s
#)
#print(names) 

date = '03/24/2018'
#24.03.2018
new_date = re.sub(
    r"(\d\d)/(\d\d)/(\d\d\d\d)",
    r"\2.\1.\3",
    # \1 - то, что стоит в первых скобках
    # \2 -\9 от 2 до 9 скобок 
    date
)

print(new_date)
# * - 0; беск
# + - 1; беск
# ? - 0;1
# {k,n} - k,n
# {k} - k

s = '<b>Иван</b> пришел на <i>пару</i>'
print(re.findall(r'<(\w+)>(.*?)</\1>', s))

s = "addrjjgiiikkkerihuisosi"
s_plus = re.sub(r'(\w)\1+', r'\1+', s)
print(s_plus)

#(\w) - 1 скобка(любая буква
# \1+ - 1 скобка повторяется больше 1 раза(+)

def reformat_date(text)
date = re.sub(
    r'(\d{2})/(\d{1,2})/(\d{4})'
    r'\2.\1.\3'
    text
    )
return date
print(reformat_date('03/24/2018'))
print(reformat_date('02/1/2000'))































