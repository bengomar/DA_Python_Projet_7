import csv
import time
from itertools import combinations
from termcolor import colored


# profits = {}
profits = []
start_time = time.time()
BUDGET_MAX = 500
file = "actions_list.csv"


with open("./data_input/"+file, newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    header = next(reader)
    actions = []
    if header is not None:
        for row in reader:
            actions.append((row[0], int(row[1]), int(row[2])))


# Génération des combinaisons via itertools.combinations
for elements in range(len(actions)):
    combos = combinations(actions, elements + 1)

    for combo in combos:
        cost = sum([i[1] for i in combo])

        if cost <= BUDGET_MAX:
            profit = sum([(j[1] * j[2] / 100) for j in combo])
            price = sum([i[1] for i in combo])
            # print(price)
            name = [i[0] for i in combo]
            # profits[profit] = name
            profits.append([profit, name, price])

# profits = sorted(profits.items(), key=lambda x: x[0], reverse=True)
profits = sorted(profits, key=lambda x: x[0], reverse=True)
best_profit = profits[0][0]
best_actions = profits[0][1]
best_price = profits[0][2]

print("")
print(" ***************************************")
print(" * Bruteforce algorithm with itertools *")
print(" ***************************************")
print("")
print(colored("Best profit after 2 years:", "yellow", attrs=["bold"]), round(best_profit, 2), "€")
print(colored("With following actions:", "yellow", attrs=["bold"]), best_actions)
print(colored("With best actions sum:", "yellow", attrs=["bold"]), best_price)
print(colored("Time elapsed: ", "white", attrs=["bold"]), time.time() - start_time, "seconds")
print("")
