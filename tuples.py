x = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
y = x.items()

# Exercise 10.2
name = "mbox-short.txt"
handle = open(name)

counts = dict()
time = list()
for line in handle:
    line = line.rstrip()
    if line.startswith("From "):
        words = line.split()
        time.append(words[5][:2])

for hour in time:
    counts[hour] = counts.get(hour, 0) + 1

lst = list()
for key, val in list(counts.items()):
    lst.append((key, val))

lst.sort()

for key, val in lst:
    print(key, val)

# print(counts)
