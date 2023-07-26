import numpy as np
import matplotlib.pyplot as plt
import csv
import time
import psutil

from termcolor import colored

start_time = time.time()
BUDGET_MAX = 500
file = "./data_input/actions_list.csv"
cpu_usage = []
ram_usage = []

def create_actions_list():
    with open(file, newline="") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        header = next(reader)
        output = []
        if header is not None:
            for row in reader:
                if not (float(row[1]) <= 0 or float(row[2]) <= 0):
                    output.append(
                        (row[0], float(row[1]), float(row[1]) * float(row[2]) / 100)
                    )
    return output


def algoinvest_dynamique(budget_max, actions_list):
    """création d'un tableau"""
    matrice = [[0 for x in range(budget_max + 1)] for x in range(len(actions_list) + 1)]
    counter = 0

    for action in range(1, len(actions_list) + 1):
        cpu_usage.append((counter, psutil.cpu_percent(interval=0.01)))
        ram_usage.append((counter, psutil.virtual_memory().percent))
        for budget in range(1, budget_max + 1):
            if actions_list[action - 1][1] <= budget:
                matrice[action][budget] = max(
                    actions_list[action - 1][2]
                    + matrice[action - 1][int(budget - actions_list[action - 1][1])],
                    matrice[action - 1][budget],
                )
            else:
                matrice[action][budget] = matrice[action - 1][budget]
        counter += 1

    print("")
    print(" ***********************************")
    print(" * Optimized algorithm - 20 shares *")
    print(" ***********************************")
    print("")
    budget = budget_max
    n = len(actions_list)
    actions_selection = []

    while budget >= 0 and n >= 0:
        action = actions_list[n - 1]
        if (
            matrice[n][int(budget)]
            == matrice[n - 1][int(budget - action[1])] + action[2]
        ):
            actions_selection.append(action)
            budget -= action[1]
        n -= 1

    return matrice[-1][-1], actions_selection


def display_results(best_result):
    print(
        colored(" Best profit after 2 years:", "yellow", attrs=["bold"]),
        round(best_result[0], 2),
    )
    print(
        colored(" With following actions:", "yellow", attrs=["bold"]),
        [i[0] for i in best_result[1]],
    )
    print(
        colored(" With best actions sum:", "yellow", attrs=["bold"]),
        round(sum([i[1] for i in best_result[1]]), 2),
    )
    print(
        colored(" Time elapsed: ", "white", attrs=["bold"]),
        time.time() - start_time,
        "seconds",
    )
    print("")


def perf_cpu():
    ord = [x[0] for x in cpu_usage]
    abs = [y[1] for y in cpu_usage]
    # print(f'{ord=}')
    # print(f'{abs=}')
    return ord, abs


def perf_ram():
    ord = [x[0] for x in ram_usage]
    abs = [y[1] for y in ram_usage]
    print(f'{ord=}')
    print(f'{abs=}')
    return ord, abs


def cpu_graphe():
    x = perf_cpu()[0]
    y = perf_cpu()[1]

    plt.plot(x, y)
    plt.show()


def ram_graphe():
    x = perf_ram()[0]
    y = perf_ram()[1]

    plt.plot(x, y)
    plt.show()


def main():
    display_results(algoinvest_dynamique(BUDGET_MAX, create_actions_list()))
    # cpu_graphe()
    ram_graphe()


if __name__ == "__main__":
    main()
