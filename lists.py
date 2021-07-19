# Exercise 8.4
# Find all the unique words from a file and sort them
fname = "romeo.txt"
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()
    words = line.split()
    for word in words:
        if word not in lst:
            lst.append(word.lower())

lst.sort()
print(lst)


# Exercise 8.5
fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
    line = line.rstrip()
    if line.startswith("From "):
        count = count + 1
        words = line.split()

print("There were", count, "lines in the file with From as the first word")