#import os and csv moduels
import os
import csv

#path for csv file
pybank = os.path.join ("resources","beudget_data.csv")


#store data
profit = []
monthly_change = []
date = []

#starting variables
number = 0
tot_profit = 0
tot_profit_change = 0
starting_profit = 0


#open the csv
with open(pybank, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimeter= ",")
    csv_header = next(csvreader)

    for row in csvreader:

        #number of months in the csv
        number = number + 1

        #collect the increase or decrease in profits
        date.append(row[0])

        #calculate tot profit
        profit.append(row[1])
        tot_profit = tot.profit + int(row[1])

        #calculate change in monthly profits
        ending_profit = int([1])
        monthly_profit_change = ending_profits - starting_profit

        #store changes to the monthly chnages
        monthly_change.append(monthly.profit.change)

        tot_profit_change = tot_profit_change + monthly_profit_change
        starting_profit = ending_profit

        avg_profit_change = (tot_profit_change/number)

        greatest_profit_increase = max(monthly_change)
        greatest_profit_decrease = min(monthly_change)

        increase_date = date[monthly_change.index(greatest_profit_increase)]
        decrease_date = date[monthly_change.index(greatest_profit_decrease)]

    print("Financial Analysis")
    print("Total Months: " + str(number))
    print("Total Profits: " + "$" + str(tot_profit))
    print("Average Change: " + "$" + str(int(avg_profit_change)))
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_profit_increase) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_profit_decrease) + ")")
