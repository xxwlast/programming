
#word_lenght = len(word)
#print(word_length)
year_str = input("Введите год:")
if len(year_str) != 4:
    print("Введите четырехзначное число")
 else:
     year = int(year_str)
     print(year)
     
if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Високосный)
