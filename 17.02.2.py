import re

with open('C:\\Users\\student\\Desktop\\cosmos.txt', encoding = "utf-8") as f:
    text = f.read()

years = re.findall("[12]\d\d\d", text)
print(years)

sections = re.findall('=+ .+ =+', text)
print(sections)

#stations  = re.findall("[А-Яа-яа-zA-Z]+[-]\d+", text)
#print(stations)

dates = re.findall('\d\d? [а-я]+ [12]\d\d\d \w*\s* - .+»', text)
print(dates)

# find all words which begin with "косм"
words = re.findall('косм[а-я]+', text)
print(words)
