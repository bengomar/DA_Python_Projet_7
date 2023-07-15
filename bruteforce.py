import csv
import time
from termcolor import colored


start_time = time.time()

BUDGET_MAX = 500
file = "actions_list.csv"


# file = "list.csv"


def create_actions_list():
    with open("./data_input/"+file, newline="") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        header = next(reader)
        output = []
        if header is not None:
            for row in reader:
                output.append((row[0], float(row[1]), float(row[2])))
    return output


def algoinvest_bruteforce(budget_max, actions_list, actions_selection=None):
    # Si la liste des éléments n'est pas vide
    if actions_selection is None:
        actions_selection = []
    if actions_list:
        # alors nous appellons la fonction en passant en paramètre le budjet max
        # en ignorant le 1er élément de la liste des actions,
        # la liste action_selection reste inchangé !
        val1, lst_val1 = algoinvest_bruteforce(
            budget_max, actions_list[1:], actions_selection
        )

        # On affecte a une variable le 1er élément de la liste ( celui ignoré précédemment)
        val = actions_list[0]

        # on vérifie si le prix (cost) du 1er élément est inférieur ou égal au budget maxi ( ici 500 €)
        if val[1] <= budget_max:
            # alors nous appellons le fonction en ôtant au budget_max le prix (cost) du 1er élément
            # puis on ignore le 1er élément de la liste des actions
            # on met a jour la liste action_selection avec le 1er élément
            val2, lst_val2 = algoinvest_bruteforce(
                budget_max - val[1], actions_list[1:], actions_selection + [val]
            )

            # si le prix du 1er élément est inférieur au suivant
            if val1 < val2:
                return val2, lst_val2
        return val1, lst_val1
    # Si la liste des actions est vide
    else:
        # donne la somme maximum de profits + les éléments sélectionnés
        return (
            f"{round(sum([(i[1] * i[2] / 100) for i in actions_selection]), 2)} €",
            actions_selection
        )


def display_results(best_result):
    print("")
    print(" ************************")
    print(" * Bruteforce algorithm *")
    print(" ************************")
    print("")
    print(colored("Best profit after 2 years:", "yellow", attrs=["bold"]), best_result[0])
    print(colored("With following actions:", "yellow", attrs=["bold"]), [i[0] for i in best_result[1]])
    print(colored("With best actions sum:", "yellow", attrs=["bold"]), sum([i[1] for i in best_result[1]]))
    print(colored("Time elapsed: ", "white", attrs=["bold"]), time.time() - start_time, "seconds")
    print("")


def main():
    display_results(algoinvest_bruteforce(BUDGET_MAX, create_actions_list()))


if __name__ == "__main__":
    main()
