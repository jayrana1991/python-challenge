import csv
import os

csv_path = "../PyBank/Resources/budget_data.csv"

month_set = []
PL_set = []
total_profit = 0
Current_PL = 0
Perivous_PL = 0
Increase = 0
Decrease = 99999999999
In_Month = ""
De_Month = ""

with open(csv_path) as handler:
    csv_reader = csv.reader(handler,delimiter=",")
    csv_header = next(csv_reader)
    csv_First_row = next(csv_reader)
    month_set.append(csv_First_row[0])
    total_profit = total_profit + int(csv_First_row[1])
    Perivous_PL = int(csv_First_row[1])

    
    for r in csv_reader:
        month_set.append(r[0])
        total_profit = total_profit + int(r[1])
        Current_PL = int(r[1])
        Net_PL = Current_PL-Perivous_PL
        Perivous_PL=Current_PL
        PL_set.append(Net_PL)

        if Net_PL > Increase:
            Increase= Net_PL
            In_Month=r[0]   

        if Net_PL < Decrease:
            Decrease= Net_PL
            De_Month=r[0]   
    
    totalmonth = len(month_set)
    print("Financial Analysis\n")
    print("----------------------------\n")
    print ("Total Months: " + str(totalmonth) + "\n")
    print ("Total:  $" + str(total_profit) + "\n")
    print("Average Change:  $" + str((round(sum(PL_set)/ len(PL_set),2))) + "\n") 
    print("Greatest Increase in Profits: " + In_Month + " ($" + str(Increase) + ")\n")
    print("Greatest Decrease in Losses:  " + De_Month + " ($" + str(Decrease) + ")\n")


with open("analysis/analysis_result.txt", "w") as out:
    out.write("Financial Analysis\n")
    out.write("----------------------------\n")
    out.write(f"Total Months:  {totalmonth}\n")
    out.write(f"Total:  ${total_profit}\n")
    out.write(f"Average Change:  ${(round(sum(PL_set)/ len(PL_set),2))}\n")
    out.write(f"Greatest Increase in Profits:  {In_Month} (${Increase})\n")
    out.write(f"Greatest Decrease in Losses:  {De_Month} (${Decrease})\n")