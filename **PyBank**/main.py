import os
import csv

bank_csv_path = os.path.join("..", "Resources", "budget_data.csv")

with open(bank_csv_path, newline="") as csvfile:
    read_bank = csv.reader(csvfile, delimiter = ",")
    
def print_values(read_bank):
    date = str(read_bank[0])
    prof_loss = int(read_bank[1])

print(read_bank)