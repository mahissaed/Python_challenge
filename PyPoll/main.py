import os
os.chdir('/Users/mahi/Desktop/Python/python_challenge/PyPoll')

import csv

# Open the file and create a reader object
with open("Resources/election_data.csv", "r") as file:
    reader = csv.reader(file)
    
    # Skip the header row
    next(reader)
    
    # Initialize a variable to keep track of the total votes
    total_votes = 0
    
    # Iterate over the rows of the file
    for row in reader:
        # Increment the total votes for each row
        total_votes += 1

# Print the total votes
print("total votes:", total_votes)
import csv

with open("Resources/election_data.csv", "r") as file:
   reader = csv.reader(file)
   header = next(reader)
   column = header.index('Candidate')
   candidates = set()
   for row in reader:
        candidate = row[column]
        if candidate not in candidates:
            candidates.add(candidate)
            print(candidate)



import csv

with open("Resources/election_data.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)
    candidate_column = header.index('Candidate')
    total_votes = 0
    candidate_votes = {}
    for row in reader:
        candidate = row[candidate_column]
        total_votes += 1
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1
    for candidate, votes in candidate_votes.items():
        percentage = 100 * votes / total_votes
        print(f'{candidate}: {percentage:.2f}% ({votes} votes)')


import csv

with open("Resources/election_data.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)
    candidate_column = header.index('Candidate')
    total_votes = 0
    candidate_votes = {}
    for row in reader:
        candidate = row[candidate_column]
        total_votes += 1
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1
    winner = max(candidate_votes, key=candidate_votes.get)
    for candidate, votes in candidate_votes.items():
        percentage = 100 * votes / total_votes
        print(f'{candidate}: {percentage:.2f}% ({votes} votes)')
    print(f'\nThe winner of the election is {winner}.')