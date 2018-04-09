#import sys
import re

def o(a):
    #non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
    with open(a, encoding="UTF-8") as f:
        t = f.read()
    return t

def r(b):
    sos = re.sub("Финлянди(\w[1-2])*","Малайзи\\1", b)
    sas = print(sos)
    return sas

def main():
    r(o("f.txt"))

if __name__ == "__main__":
    main()
        
