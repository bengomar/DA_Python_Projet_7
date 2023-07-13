import csv
import time
from pprint import pprint

start_time = time.time()

BUDGET_MAX = 500
file = "actions_list.csv"


# file = "list.csv"


def create_actions_list():
    with open(file, newline="") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        header = next(reader)
        output = []
        if header is not None:
            for row in reader:
                output.append((row[0], int(row[1]), int(row[2])))

    return output


def algoinvest_dynamique(budget_max, actions_list):
    matrice = [[0 for x in range(budget_max + 1)] for x in range(len(actions_list) + 1)]

    print(actions_list)
    # print(range(1, len(actions_list) + 1))
    # print(range(1, budget_max + 1))

    nb = 0

    for i in range(1, len(actions_list) + 1):
        print("i=", i)
        for w in range(1, budget_max + 1):
            if actions_list[i - 1][1] <= w:
                print("actions_list[i-1]", actions_list[i - 1])
                print("argument max 1")
                print(actions_list[i - 1][2] + matrice[i - 1][w - actions_list[i - 1][1]])
                print("argument max 2")
                print(matrice[i - 1][w])

                matrice[i][w] = max(actions_list[i - 1][2] + matrice[i - 1][w - actions_list[i - 1][1]],
                                    matrice[i - 1][w])
            else:
                matrice[i][w] = matrice[i - 1][w]
                print("argument max 2")
                print(matrice[i - 1][w])

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

    # return (
    #     f"{round(sum([(i[1] * i[2] / 100) for i in actions_selection]), 2)} €",
    #     f"{actions_selection}",

    # )
    return matrice[-1][-1], actions_selection


def display_results(best_result):
    print("")
    print("-" * 254)
    print("Best profit after 2 years : ", sum([(i[1] * i[2] / 100) for i in best_result[1]]))
    print("Best sum actions : ", best_result[0])
    print("With following actions : ", best_result[1])
    print("Time elapsed : ", time.time() - start_time, "seconds")
    print("-" * 254)


def main():
    display_results(algoinvest_dynamique(BUDGET_MAX, create_actions_list()))

if __name__ == "__main__":
    main()
