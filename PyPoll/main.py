import os
import csv

election_csv = os.path.join('.', 'Resources', 'election_data.csv')

total_votes = 0

with open(election_csv) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    
    # Initialize lists
    
    candidates = {}
   

   
    # Read each row of data after the header
    for row in csvreader:
        total_votes = total_votes + 1
        current_candidate = row[2]
        
        if current_candidate in candidates:
            candidates[current_candidate] = candidates[current_candidate] + 1
        else:
            candidates[current_candidate] = 1
    

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

for candidate in candidates:
    print(f"{candidate}: {round(candidates[candidate]*100/total_votes, 3)}% ({candidates[candidate]})")

print("-------------------------")    
print(f"Winner: {max(candidates, key=candidates.get)}")
print("-------------------------")

# Export the results to text file
analysis_txt = os.path.join('.', 'analysis', 'analysis.txt')
with open(analysis_txt, "w") as txt_file:
  
    txt_file.write("Election Results\n-------------------------" + '\n')
    txt_file.write(f"Total Votes: {total_votes}" + '\n')
    txt_file.write("-------------------------" + '\n')
    for candidate in candidates:
        txt_file.write(f"{candidate}: {round(candidates[candidate]*100/total_votes, 3)}% ({candidates[candidate]})" + '\n')
    
    txt_file.write("-------------------------" + '\n')
    txt_file.write(f"Winner: {max(candidates, key=candidates.get)}" + '\n')
    txt_file.write("-------------------------" + '\n')
    txt_file.close()