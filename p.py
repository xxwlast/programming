lines2016 = []
with open("freq.txt", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        #print(line)
        cells = line.split(' | ')
        if cells[1] == "гл несов непер инф":
            lines2016.append(cells)
print(lines)
