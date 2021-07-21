import re

fh = open("regex_sum_practice.txt")

lst = list()
for line in fh:
    line = line.rstrip()
    x = re.findall('[0-9]+', line)
    if len(x) > 0:
        for num in x:
            lst.append(num)

total = 0
for num in lst:
    total = int(num) + total

print(total)
