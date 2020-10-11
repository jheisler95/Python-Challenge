import os
import csv

# path for the CSV file in PyPollcsv

PyPollcsv = os.path.join("Resource", "electiondata.csv")

# Create the lists to store data

number = 0

candidatelist = []
uniquecandidate = []
votes = []
vote_percent = []

# Open the CSV 

with open(PyPollcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    
    for row in csvreader:
        # Count the total number of votes
        number = number + 1
        # Set the candidate names to candidatelist
        candidatelist.append(row[2])
        # Create a set from the candidatelist 
    for x in set(candidatelist):
        uniquecandidate.append(x)
        # y is the total number of votes per candidate
        y = candidatelist.count(x)
        votes.append(y)
        # z is the percent of total votes per candidate
        z = (y / count) * 100
        vote_percent.append(z)

    winningvotes = max(vote_count)
    winner = uniquecandidate[votes.index(winningvotes)]




print("Election Results")
print("Total Votes :" + str(number))
for i in range(len(uniquecandidate)):
    print(uniquecandidate[i] + ": " + str(vote_percent[i]) + "% (" + str(votes[i]) + ")")
print("The winner is: " + winner)
