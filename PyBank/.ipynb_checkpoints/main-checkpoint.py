#The total number of months included in the dataset

#The changes in "Profit/Losses" over the entire period, and then the average of those changes
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in profits (date and amount) over the entire period

#import modules
import os 
import csv

#Path
budget_csv = os.path.join('Resources', 'budget_data.csv')
output_path = os.path.join('Analysis', 'PyBankAnalysis.txt')

with open(budget_csv, 'r') as csvfile:
    #split the data
    csvreader = csv.reader(csvfile, delimiter=',')
    # Pull the header
    header = next(csvreader)
    # Grab first row
    firstRow = next(csvreader)
    #The net total amount of "Profit/Losses" over the entire period
    netTotal = int(firstRow[1])
    # Hold to comp
    lastMonth = netTotal
    monthCount = 1
    # Change from last month
    thisMonthChange = 0
    # All changes
    totalChange = 0.00
    #The greatest increase in profits (date and amount) over the entire period
    greatestInc = [" ", 0]
    #The greatest decrease in profits (date and amount) over the entire period
    greatestDec = [" ", 0]

    for row in csvreader:
        monthCount += 1
        netTotal += int(row[1])

        thisMonthChange = int(row[1]) - lastMonth
        totalChange += thisMonthChange
        lastMonth = int(row[1])

        if thisMonthChange > greatestInc[1]:
            greatestInc[0] = str(row[0])
            greatestInc[1] = thisMonthChange
        elif thisMonthChange < greatestDec[1]:
            greatestDec[0] = str(row[0])
            greatestDec[1] = thisMonthChange

    output=[
        ("Financial Analysis"),
        ("------------------------------------"),
        (f'Total Months: {monthCount}'),
        (f"Total: ${netTotal}"),
        (f"Average Change: $"'{0:.2f}'.format(totalChange/(monthCount-1))),
        (f'Greatest Increase in Profits: {greatestInc[0]} (${greatestInc[1]})'),
        (f'Greatest Decrease in Profits: {greatestDec[0]} (${greatestDec[1]})')
    ]

    for printLine in output: 
        print(printLine)

    textwriter = open(output_path, 'w')

    for textline in output:
        textwriter.write(textline)
        textwriter.write("\n")

    textwriter.close()