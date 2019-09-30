import os
import csv
import pandas as pd
import numpy as np

bank_csv_path = os.path.join("..", "Resources", "budget_data.csv")

read_bank = pd.read_csv(bank_csv_path)
for row in read_bank:
    all_months = read_bank.count

def print_values(read_bank):
    date = str(read_bank[0])
    change = int(read_bank[1])

total_months = read_bank['Date'].count()
net_total = read_bank['Profit/Losses'].sum()
avg_chg = read_bank['Profit/Losses'].mean()
great_up = read_bank['Profit/Losses'].max()
great_down = read_bank['Profit/Losses'].min()

print("'''''''")
print("Financial Analysis")
print("-------------------------")
print("Total months: " + str(total_months))
print("Total: $" + str(net_total))
print("Av. Change: $" + str(avg_chg))
print("Greatest Increase in Profits: $" + str(great_up))
print("Greatest Decrease in Profits: $" + str(great_down))
print("'''''''")