import os
import pandas as pd
import csv
import numpy as np


def print_values(read_poll):
    voter_id = int(read_poll[0])
    county = str(read_poll[1])
    candidate = str(read_poll[2])


poll_csv_path = os.path.join("..", "Resources", "election_data.csv")

read_poll = pd.read_csv(poll_csv_path)
for row in read_poll:
        total_votes = read_poll.count
        
print(total_votes)
