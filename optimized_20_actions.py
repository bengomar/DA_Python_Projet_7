import csv
import time

from termcolor import colored

start_time = time.time()

BUDGET_MAX = 500
file = "./data_input/actions_list.csv"


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
    for action in range(1, len(actions_list) + 1):
        for budget in range(1, budget_max + 1):
            if actions_list[action - 1][1] <= budget:
                matrice[action][budget] = max(
                    actions_list[action - 1][2]
                    + matrice[action - 1][int(budget - actions_list[action - 1][1])],
                    matrice[action - 1][budget],
                )
            else:
                matrice[action][budget] = matrice[action - 1][budget]

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


def main():
    display_results(algoinvest_dynamique(BUDGET_MAX, create_actions_list()))


if __name__ == "__main__":
    main()
