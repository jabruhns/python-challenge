import os
import csv

bank_csv_path = os.path.join("budget_data.csv")
with open(bank_csv_path, newline="") as csvfile:
    read_bank = csv.reader(csvfile, delimiter = ",")
    print(read_bank)