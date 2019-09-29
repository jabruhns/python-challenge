import os
import csv

poll_csv_path = os.path.join("..", "Resources", "election_data.csv")

with open(poll_csv_path, newline="") as csvfile:
        read_poll = csv.reader(csvfile, delimiter = ",")

def print_values(read_poll):
    voter_id = int(read_poll[0])
    county = str(read_poll[1])
    candidate = str(read_poll[2])

print(read_poll)