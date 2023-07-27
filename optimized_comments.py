import csv
import time
from pprint import pprint

from termcolor import colored

start_time = time.time()

BUDGET_MAX = 5
actions = [("Action-1", 2.0, 6.0), ("Action-2", 1.0, 2.5), ("Action-3", 4.0, 8.0)]


def algoinvest_dynamique(budget_max, actions_list):
    """création d'un tableau"""
    matrice = [[0 for x in range(budget_max + 1)] for x in range(len(actions_list) + 1)]
    print("matrice", matrice)
    for action in range(1, len(actions_list) + 1):
        for budget in range(1, budget_max + 1):
            print("")
            print("*" * 100)
            print("action", action, "budget", budget)
            print(actions_list)
            print(
                f"si le prix de l'action en cours d'index {actions_list.index(actions_list[action - 1])} ({actions_list[action - 1][1]}) <= au budget ({budget})"
            )

            if actions_list[action - 1][1] <= budget:
                print("ALORS")
                print(
                    "Le max entre les valeurs suivantes:",
                    colored(
                        (
                            actions_list[action - 1][2]
                            + matrice[action - 1][
                                int(budget - actions_list[action - 1][1])
                            ],
                            matrice[action - 1][budget],
                        ),
                        "green",
                        attrs=["bold"],
                    ),
                )

                matrice[action][budget] = max(
                    actions_list[action - 1][2]
                    + matrice[action - 1][int(budget - actions_list[action - 1][1])],
                    matrice[action - 1][budget],
                )
                print("RESULTAT", matrice[action][budget])
                print(
                    "------------------------------------------------------------------------------------------------------------------------------"
                )
                print(
                    "max(actions_list[action - 1][2] + matrice[action - 1][int(budget - actions_list[action - 1][1])], matrice[action - 1][budget])"
                )
                print(
                    "------------------------------------------------------------------------------------------------------------------------------"
                )

                print(f"action={action}, budget={budget}")
                print("actions_list[action - 1] = ", actions_list[action - 1])
                print(
                    "actions_list[action - 1][2] = ",
                    colored(actions_list[action - 1][2], "red", attrs=["bold"]),
                )
                print(
                    "budget - actions_list[action - 1][1] = ",
                    budget - actions_list[action - 1][1],
                )
                print("matrice[action - 1] = ", matrice[action - 1])
                print(
                    "matrice[action - 1][int(budget - actions_list[action - 1][1])] = ",
                    colored(
                        matrice[action - 1][int(budget - actions_list[action - 1][1])],
                        "red",
                        attrs=["bold"],
                    ),
                )
                print("")
                print("ARGUMENT 1")
                print(
                    "actions_list[action - 1][2] + matrice[action - 1][int(budget - actions_list[action - 1][1])]",
                    colored(
                        actions_list[action - 1][2]
                        + matrice[action - 1][
                            int(budget - actions_list[action - 1][1])
                        ],
                        "green",
                        attrs=["bold"],
                    ),
                )
                print("ARGUMENT 2")
                print(
                    "matrice[action - 1][budget] = ",
                    colored(matrice[action - 1][budget], "green", attrs=["bold"]),
                )

            else:
                print("SINON")
                matrice[action][budget] = matrice[action - 1][budget]
                print("---------------------------")
                print("matrice[action - 1][budget]")
                print("---------------------------")
                print(f'{matrice= }')
                print(f'[action - 1] = [{action-1}]')
                print(f'[budget] = [{budget}]')
                print("matrice[0][1] = ", matrice[action - 1][0])

                print(
                    "RESULTAT",
                    colored(matrice[action][budget], "green", attrs=["bold"]),
                )

    print("")
    print()
    pprint(matrice)

    print("")
    print(" ***********************************")
    print(" * Optimized algorithm - 20 shares *")
    print(" ***********************************")
    print("")
    budget = budget_max
    n = len(actions_list)
    actions_selection = []

    while budget >= 0 and n >= 0:
        print("*" * 100)
        print(f"budget= {budget}, nb d'actions dans la liste --> n = {n}")
        print("tant que le budget >= 0 et que la liste des actions >= 0 ")
        print(
            f'affectation d\'une variable "action" égale à actions_list[{n} - 1] --> actions_list[{n-1}] '
        )
        print("actions_list =", actions_list)
        action = actions_list[n - 1]
        print(f"{action = }")
        print(
            "-----------------------------------------------------------------------------------"
        )
        print(
            "IF matrice[n][int(budget)] == matrice[n - 1][int(budget - action[1])] + action[2]"
        )
        print(
            "-----------------------------------------------------------------------------------"
        )
        print("ARGUMENT 1")
        print(f"matrice[n]= {matrice[n]}")
        print(
            f'matrice[n][int(budget ({budget}))] = {colored(matrice[n][int(budget)], "green", attrs=["bold"])}'
        )
        print("")
        print("ARGUMENT 2")
        print(f"matrice[n - 1] = {matrice[n - 1]}")
        print(f"matrice[n - 1][int(budget ({budget}) - action[1] ({action[1]}))]")
        print(
            f"matrice[n - 1][{int(budget) - action[1]}] = {matrice[n - 1][int(budget - action[1])]}"
        )
        print(f"action[2] {action[2]}")
        print(
            f'{matrice[n - 1][int(budget - action[1])]} + {action[2]} = {colored(matrice[n - 1][int(budget - action[1])] + action[2], "green", attrs=["bold"])}'
        )
        print(
            f'SI {colored(matrice[n][int(budget)], "green", attrs=["bold"])} == {colored(matrice[n - 1][int(budget - action[1])] + action[2], "green", attrs=["bold"])}'
        )
        if (
            matrice[n][int(budget)]
            == matrice[n - 1][int(budget - action[1])] + action[2]
        ):
            actions_selection.append(action)
            print(f"ALORS")
            print(
                f'AJOUTER l\'action en cours {action} dans une nouvelle liste "action_selection"'
            )
            budget -= action[1]
            print(
                f"DIMINUER le budget {budget} du prix de l'action en cours {action[1]}"
            )
            print(f"budget après: {budget}")
        n -= 1
        print(f"REDUIRE de 1 le nb d'action: {n}")

    return matrice[-1][-1], actions_selection


def display_results(best_result):
    print("")
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
    display_results(algoinvest_dynamique(BUDGET_MAX, actions))


if __name__ == "__main__":
    main()
