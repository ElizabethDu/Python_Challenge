#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote

# import modules

import os
import csv

# Paths
election_csv = r'C:\Projects\Python_Challenge\PyPoll\Resources\election_data.csv'
output_path = r'C:\Projects\Python_Challenge\PyPoll\Analysis\PyPollAnalysis.txt'

#election_csv = os.path.join('Resources', 'election_data.csv')
#output_path = os.path.join('Analysis', 'PyPollAnalysis.txt')

# -----------------------------------------------------------------------------

# variables
candidateList = []
voteCountList = []
mostVotes = ["",0]
voteTotal = 0
spacer = " ------------------------------------------------ "

with open(election_csv, 'r') as csvfile:

    # split the data
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    # Run through csv file
    for row in csvreader:
        voteTotal += 1
        currentCandidate = str(row[2])
        if currentCandidate in candidateList:
            index = candidateList.index(currentCandidate)
            voteCountList[index] += 1
        else:
            candidateList.append(currentCandidate)
            voteCountList.append(1)

#---------------------------------------------------------

# Saving output
output=[
    ("Election Results"),
    (spacer),
    (f'Total Votes: {voteTotal}'),
    (spacer)
]

# Run through candidate list
for i in range(len(candidateList)):
    if voteCountList[i] > mostVotes[1]:
        mostVotes = [candidateList[i], voteCountList[i]]
    output.append(f'{candidateList[i]}: {format(voteCountList[i]/voteTotal,".3%")} ({voteCountList[i]})')

# Print out the winner
output.append(spacer)
output.append(f'Winner: {mostVotes[0]}')
output.append(spacer)

# Print out winner in terminal
for printline in output:
    print(printline)

# ---------------------------------------------------------

# Open textwriter
textwriter = open(output_path, 'w')

for textline in output:
    textwriter.write(textline)
    textwriter.write("\n")

# Close textwriter
textwriter.close()
