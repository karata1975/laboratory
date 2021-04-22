negs = 0
pos = 0
for i in map(int, input().split()):
    if i < 0:
        negs += 1
    elif i > 0:
        pos += 1
print("Положительных больше" if pos > negs else "Отрицательных больше" if negs > pos else "Поровну")
