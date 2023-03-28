import os
import csv

path = os.path.join("Resources","election_data.csv")

votecount = {}
rowcount = 0
candidatelist = []

with open(path, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    csv_header = next(csvfile)

    for row in csvreader:

        rowcount += 1
        if row[2] in votecount:
            votecount[row[2]] = votecount[row[2]] + 1
        else: 
            candidatelist.append(row[2])
            votecount[row[2]] = 1

print("Election Results")
print("\n----------------------")
print("Total months = " + str(rowcount))
print("----------------------")

winnervotes = 0
i = 0
for item in votecount:
    percent = (votecount[item] / rowcount)*100
    print(candidatelist[i] + ": " + str((round(percent, 2)))+ "% (" + str(votecount[item]) + ")")
    if votecount[item] > winnervotes:
        winnervotes = votecount[item]
        winner = candidatelist[i]
    i+=1

print("-----------------------")
print("Winner: " + winner)
print("-----------------------")

