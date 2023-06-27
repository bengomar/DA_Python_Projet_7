from itertools import combinations
from pprint import pprint
import time

#
actions = [('Action-1', 20, 5),
           ('Action-2', 30, 10),
           ('Action-3', 50, 15),
           ('Action-4', 70, 20),
           ('Action-5', 60, 17),
           ('Action-6', 80, 25),
           ('Action-7', 22, 7),
           ('Action-8', 26, 11),
           ('Action-9', 48, 13),
           ('Action-10', 34, 27),
           ('Action-11', 42, 17),
           ('Action-12', 110, 9),
           ('Action-13', 38, 23),
           ('Action-14', 14, 1),
           ('Action-15', 18, 3),
           ('Action-16', 8, 8),
           ('Action-17', 4, 12),
           ('Action-18', 10, 14),
           ('Action-19', 24, 21),
           ('Action-20', 114, 18)]

start_time = time.time()
profits = []
# Génération des combinaisons via itertools.combinations
for elements in range(len(actions)):
    combos = combinations(actions, elements+1)

    #
    for combo in combos:
        cost = sum([i[1] for i in combo])
        # print('cost', cost)

        if cost <= 500:
            profit = sum([(j[1] * j[2] / 100) for j in combo])
            name = [i[0] for i in combo]
            profits.append([profit, name])

profits = sorted(profits, key=lambda x: x[0], reverse=True)
best_profit = profits[0][0]
best_actions = profits[0][1]

print("-" * 50)
print("Best profit after 2 years : ", round(best_profit, 2), "€")
print("Best actions concerned : ", best_actions)
print("Time elapsed : ", time.time() - start_time, "seconds")
print("-" * 50)

