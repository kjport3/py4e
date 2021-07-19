# Exercise 7.2
fname = "mbox-short.txt"
fh = open(fname)
fscore_total = 0
count = 0
for line in fh:
    line = line.rstrip()
    if line.startswith("X-DSPAM-Confidence:"):
        count = count + 1
        fscore = float(line[-6:])
        fscore_total = fscore_total + fscore

avg_score = fscore_total / float(count)
print("Average spam confidence: " + str(avg_score))