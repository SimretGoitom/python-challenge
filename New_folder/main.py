# Import Libraries
import os
import csv

# Set File Path for Input and Output
PyPoll = os.path.join("../Resources", "election_data.csv")
file_output = "Output/poll_results.txt"
# Declaring the Variables 
total_votes = 0
candidates = {}
candidates_percent = {}
winner_count = 0
winner = ""
