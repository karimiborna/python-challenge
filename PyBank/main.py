import os
import csv

path = os.path.join("Resources","budget_data.csv")

profitloss = 0
date_list = []
pl_list = []
changes_list = []


with open(path, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)

    for row in csvreader:

        profitloss += int(row[1])
        date_list.append(row[0])
        pl_list.append(int(row[1]))

greatest = 0
greatest_loc = 0
least = 0
least_loc = 0
i = 0

while i < (len(pl_list)):
    if i == 0 :
        i+=1
    else:
        first = pl_list[(i-1)]
        second = pl_list[i]
        difference = second - first
        if difference > greatest:
            greatest = difference
            greatest_loc = i
        if difference < least:
            least = difference
            least_loc = i

        changes_list.append(difference)
        i += 1

date_great = date_list[greatest_loc]
date_least = date_list[least_loc]
avg_change = (sum(changes_list)) / (len(changes_list))
avg_change = round(avg_change, 2)

#OUTPUT

quote = "Total Months: " + str(len(pl_list)) + "\n" + "Total: $" + str(profitloss) + "\n" + "Average Change: $" + str(avg_change) + "\n" + "Greatest Increase in Profits: " + date_great + " ($" + str(greatest) + ")" + "\n" + "Greatest Decrease in Profits: " + date_least + " ($" + str(least) +")"

print(quote)

#NEW FILE

with open(os.path.join("analysis","PyBank_Analysis.txt"),"w") as file:
    file.write(quote)
    file.close

    