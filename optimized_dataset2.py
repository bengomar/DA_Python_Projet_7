import csv
import time
from termcolor import colored

start_time = time.time()

BUDGET_MAX = 500
file = "dataset2.csv"


def create_actions_list():
    with open("./data_input/"+file, newline="") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        header = next(reader)
        output = []
        if header is not None:
            for row in reader:
                if float(row[1]) <= 0:
                    pass
                else:
                    output.append(
                        (row[0], float(row[1]), float(row[1]) * float(row[2]) / 100)
                    )
    return output


def algoinvest_dynamique(budget_max, actions_list):
    matrice = [[0 for x in range(budget_max + 1)] for x in range(len(actions_list) + 1)]
    nb = 0
    for i in range(1, len(actions_list) + 1):
        for w in range(1, budget_max + 1):
            if actions_list[i - 1][1] <= w:
                matrice[i][w] = max(
                    actions_list[i - 1][2]
                    + matrice[i - 1][int(w - actions_list[i - 1][1])],
                    matrice[i - 1][w],
                )
            else:
                matrice[i][w] = matrice[i - 1][w]
            nb += 1

    print("")
    print(" #######################")
    print(" # Optimized algorithm #")
    print(" #######################")
    print("")
    print(colored(" Number of iterations: ", "white", attrs=["bold"]), nb)
    w = budget_max
    n = len(actions_list)
    actions_selection = []

    while w >= 0 and n >= 0:
        action = actions_list[n - 1]
        if matrice[n][int(w)] == matrice[n - 1][int(w - action[1])] + action[2]:
            actions_selection.append(action)
            w -= action[1]
        n -= 1

    return matrice[-1][-1], actions_selection


def display_results(best_result):
    print(colored(" Best profit after 2 years:", "yellow", attrs=["bold"]), round(best_result[0], 2))
    print(colored(" With following actions:", "yellow", attrs=["bold"]), [i[0] for i in best_result[1]])
    print(colored(" With best actions sum:", "yellow", attrs=["bold"]), round(sum([i[1] for i in best_result[1]]), 2))
    print(colored(" Time elapsed: ", "white", attrs=["bold"]), time.time() - start_time, "seconds")
    print("")


def main():
    display_results(algoinvest_dynamique(BUDGET_MAX, create_actions_list()))


if __name__ == "__main__":
    main()
