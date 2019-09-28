import os
import csv

poll_csv_path = os.path.join("..", "Resources", "election_data.csv")
with open(poll_csv_path, newline="") as csvfile:
        read_poll = csv.reader(csvfile, delimiter = ",")
        print (read_poll)