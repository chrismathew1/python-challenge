import os
import csv

budget_csv = os.path.join('.', 'Resources', 'budget_data.csv')

with open(budget_csv) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    
    # Initialize lists
    months = []
    profit_loss = []
    average_change = []
   
    # Initializes variable for average change calculation
    previous_profit = 0
   
    # Read each row of data after the header
    for row in csvreader:
        
        # print(row[0])
        months.append(row[0])
        profit_loss.append(int(row[1]))
        average_change.append(int(row[1]) - previous_profit)
        previous_profit = int(row[1])
    
    # Pops the first element in average_change because 
    average_change.pop(0)
## Analysis

## Print output
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(months)}")
print(f"Total: ${sum(profit_loss)}")
print(f"Average Change: ${round(sum(average_change)/len(average_change), 2)}")
print(f"Greatest Increase in Profits: {months[average_change.index(max(average_change)) + 1]} (${max(average_change)})")
print(f"Greatest Decrease in Profits: {months[average_change.index(min(average_change)) + 1]} (${min(average_change)})")


# Export the results to text file

analysis_txt = os.path.join('.', 'analysis', 'analysis.txt')
with open(analysis_txt, "w") as txt_file:
  
    txt_file.write("Financial Analysis\n----------------------------" + '\n')
    txt_file.write(f"Total Months: {len(months)}" + '\n')
    txt_file.write(f"Total: ${sum(profit_loss)}" + '\n')
    txt_file.write(f"Average Change: ${round(sum(average_change)/len(average_change), 2)}" + '\n')
    txt_file.write(f"Greatest Increase in Profits: {months[average_change.index(max(average_change)) + 1]} (${max(average_change)})" + '\n')
    txt_file.write(f"Greatest Decrease in Profits: {months[average_change.index(min(average_change)) + 1]} (${min(average_change)})" + '\n')
    txt_file.close()