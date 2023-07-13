import csv
import time
from pprint import pprint

start_time = time.time()

BUDGET_MAX = 500
file = "list.csv"


def create_actions_list():
    with open(file, newline="") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        header = next(reader)
        output = []
        if header is not None:
            for row in reader:
                output.append((row[0], float(row[1]), round(float(row[1]) * float(row[2])) / 100))

    return output


print(create_actions_list())


def algoinvest_dynamique(budget_max, actions_list):
    matrice = [[0 for x in range(budget_max + 1)] for x in range(len(actions_list) + 1)]
    nb = 0
    for i in range(1, len(actions_list) + 1):
        for w in range(1, budget_max + 1):
            if actions_list[i - 1][1] <= w:
                # print("actions_list[i-1]", actions_list[i - 1])
                # print("OK 1er argument max ")
                # print(actions_list[i - 1][2] + matrice[i - 1][w - actions_list[i - 1][1]])
                # print("OK 2eme argument max")
                # print(matrice[i - 1][w])

                matrice[i][w] = max(actions_list[i - 1][2] + matrice[i - 1][w - actions_list[i - 1][1]],
                                    matrice[i - 1][w])
            else:
                matrice[i][w] = matrice[i - 1][w]
                # print("NOK argument max (else)")
                # print(matrice[i - 1][w])
            nb += 1

    print("Nombre d'itération:", nb)
    w = budget_max
    n = len(actions_list)
    actions_selection = []

    while w >= 0 and n >= 0:
        action = actions_list[n - 1]
        if matrice[n][w] == matrice[n - 1][w - action[1]] + action[2]:
            w -= action[1]
            actions_selection.append(action)
        n -= 1

    return matrice[-1][-1], actions_selection


def display_results(best_result):
    print("")
    print("-" * 160)
    print("Best profit after 2 years : ", round(best_result[0], 2))
    print("With following actions : ", [i[0] for i in best_result[1]])
    print("With best actions Sum : ", sum([i[1] for i in best_result[1]]))
    print("Time elapsed : ", time.time() - start_time, "seconds")
    print("-" * 160)


def main():
    display_results(algoinvest_dynamique(BUDGET_MAX, create_actions_list()))


if __name__ == "__main__":
    main()
