import csv
import time
from itertools import combinations

# profits = {}
profits = []
start_time = time.time()
BUDGET_MAX = 500
file = "actions_list.csv"
# file = "list.csv"


with open(file, newline="") as csvfile:
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
print("-" * 160)
print("Best profit after 2 years : ", round(best_profit, 2), "€")
print("With following actions : ", best_actions)
print("With best actions sum : ", best_price)
print("Time elapsed : ", time.time() - start_time, "seconds")
print("-" * 160)
