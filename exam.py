import os

def opening(a):
    with open(a, encoding="UTF-8") as f:
        t = f.read()
    return t

def something(b):
    for root, dirs, files in os.walk(b):
        print(files)
        for i in files:
            heh = b + '/' + file
            openfile(heh)

def main():
    something(opening("news.zip"))

if __name__ == "__main__":
	main()

#пожалуйста не ставьте 0, я не хочу вылетать из универа Т_Т
