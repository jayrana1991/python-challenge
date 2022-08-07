import csv
import os


csv_path = "Resources\election_data.csv"

cand_names = []
votes = []
voters_dict = {}

    # it = iter(a)
    # res_dct = dict(zip(it, it))
total_votes = 0

with open(csv_path) as handler:
    csv_reader = csv.reader(handler,delimiter=",")
    csv_header = next(csv_reader)
    # ['Ballot ID', 'County', 'Candidate']
    for r in csv_reader:
        cand_names.append(r[2])
        votes.append(r[0])
        voters_dict[r[2]] = voters_dict.get(r[2], 0) + 1

total_votes = len(votes)        
print(total_votes)
print(voters_dict)

# Election Results
# -------------------------
# Total Votes: 369711
# -------------------------
# Charles Casper Stockham: 23.049% (85213)
# Diana DeGette: 73.812% (272892)
# Raymon Anthony Doane: 3.139% (11606)
# -------------------------
# Winner: Diana DeGette
# -------------------------    

with open("analysis/analysis_result.txt", "w") as out:
    print("Election Results\n")
    print("----------------------------\n")
    out.write("Election Results\n")
    out.write("----------------------------\n")
    print(f"Total Months:  {total_votes}\n")
    out.write(f"Total Months:  {total_votes}\n")    
    for i in voters_dict.keys():
        perct_votes = round((voters_dict[i]/total_votes) * 100,3)
        print(i + ": " + str(perct_votes) + "%" + "(" + str(voters_dict[i]) + ")\n")
        out.write(i + ": " + str(perct_votes) + "%" + "(" + str(voters_dict[i]) + ")\n")
        if voters_dict[i] == max(voters_dict.values()):
            winner = i
        else:
            pass
    print("----------------------------\n")
    print("Winner: "+ winner + "\n")
    print("----------------------------\n")
    out.write("----------------------------\n")
    out.write("Winner: "+ winner + "\n")
    out.write("----------------------------\n")


    # for i in voters_dict.keys():
    #     out.write(i )

    # out.write(f"Total Months:  {totalmonth}\n")
    # out.write(f"Total:  ${total_profit}\n")
    # out.write(f"Average Change:  ${(round(sum(PL_set)/ len(PL_set),2))}\n")
    # out.write(f"Greatest Increase in Profits:  {In_Month} (${Increase})\n")
#     # out.write(f"Greatest Decrease in Losses:  {De_Month} (${Decrease})\n")

