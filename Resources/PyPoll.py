# The data we need to retrive.
# Total number of votes cast
# A complete list of candidates who received votes
# Total number of votes each candidate received
# Percentage of votes each candidate won
# The winner of the election based on popular vote

# Add our dependencies.
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load='Resources/election_results.csv'
# Assign a variable to save the file to a path.
file_to_save = os.path.join("Analysis","election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

# To do : read and analyze the data here.
    file_reader = csv.reader(election_data)

    # Read and Print the hearder row.
    headers = next(file_reader)
    print(headers)



