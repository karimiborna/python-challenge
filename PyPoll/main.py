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
print("Total votes = " + str(rowcount))
print("----------------------")

winnervotes = 0
i = 0
quotes = []
for item in votecount:
    percent = (votecount[item] / rowcount)*100
    print(candidatelist[i] + ": " + str((round(percent, 2)))+ "% (" + str(votecount[item]) + ")")
    quotes.append(candidatelist[i] + ": " + str((round(percent, 2)))+ "% (" + str(votecount[item]) + ") \n")
    if votecount[item] > winnervotes:
        winnervotes = votecount[item]
        winner = candidatelist[i]
    i+=1

print("-----------------------")
print("Winner: " + winner)
print("-----------------------")

with open(os.path.join("analysis","PyPoll_Analysis.txt"),"w") as file:
    file.write("Election Results")
    file.write("\n----------------------")
    file.write("\nTotal votes = " + str(rowcount))
    file.write("\n----------------------" + "\n")
    file.writelines(quotes)
    file.write("-----------------------")
    file.write("\nWinner: " + winner)
    file.write("\n-----------------------")
    file.close