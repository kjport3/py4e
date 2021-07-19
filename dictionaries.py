# Exercise 9.4
name = "mbox-short.txt"
handle = open(name)

counts = dict()
emails = list()
for line in handle:
    line = line.rstrip()
    if line.startswith("From "):
        words = line.split()
        emails.append(words[1])

for email in emails:
    counts[email] = counts.get(email, 0) + 1

max_key = max(counts, key=counts.get)
print(str(max_key) + " " + str(counts[max_key]))

print('')


# 9 Worked Exercise
fname = "clown.txt"
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    words = lin.split()
    for word in words:
        di[word] = di.get(word, 0) + 1
        # # Same as:
        # if word in di:
        #     di[word] = di[word] + 1
        # else:
        #     di[word] = 1

# Find the most common word using maximum loop
largest = -1
keyword = None
for key, value in di.items():
    print(key, value)
    if value > largest:
        largest = value
        keyword = key

print(keyword, largest)
