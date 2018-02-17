import re

a = re.findall('a', 'abracadabra')
print(a)

a  = re.findall('a.', 'aaabracadabra')
print(a)

a = re.findall('[abc]', 'abracadabra')
print(a)

a = re.findall('[ac].[bd]', 'abracadabra')
print(a)


# . - любой символ
# [..] - любой из
# [^..] - любой кроме
# [..-..] - диапазон

a = re.findall("\d", "10:56 17.02.2018")
print(''.join(a))

a = re.findall("\w", "aDFt6-_+>SЫ")
print(a)

# \w - все буквы
# \W - все небуквы

a = re.findall("\s", """ ыыыы я буква ыЭЭЭЭЭ
\tрырр рыр
""")
print(a)

# \s - " ", \t, \n
# \S - not \s

a = re.findall('^a', """abd
abdf
"""
)
print(a)

# "^a" finds "a" in the begining of the sentence
# "a$" finds "a" in the end

a = re.findall(r"\\" , r"17.02.2018")
print(a)

# если нужна сырая строка,
# без функции или подобного, перед этим надо поставить "r"


#a+ - печатать места. где символ встречается один раз и больше

a = re.findall("a+", "aaabraaaacadaaaaabreea")
print(a)

a = re.findall("\S", """Мама мама мылу раму раму
\t маму
мыла""")
print(a)

a = re.findall('\w+-?\w+',
               "что-нибудь какое где и")
print(a)

# wikipedia.readthedocs.io



