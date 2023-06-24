actions = [('Action-1', 20, 1),
           ('Action-2', 30, 3),
           ('Action-3', 50, 7.5),
           ('Action-4', 70, 14)]

# actions = [('Action-1', 20, 5),
#            ('Action-2', 30, 10),
#            ('Action-3', 50, 15),
#            ('Action-4', 70, 20)]
           # ('Action-5', 60, 17),
           #  ('Action-6', 80, 25),
           #  ('Action-7', 22, 7),
           #  ('Action-8', 26, 11),
           #  ('Action-9', 48, 13),
           #  ('Action-10', 34, 27),
           #  ('Action-11', 42, 17),
           #  ('Action-12', 110, 9),
           #  ('Action-13', 38, 23),
           #  ('Action-14', 14, 1),
           #  ('Action-15', 18, 3),
           #  ('Action-16', 8, 8),
           #  ('Action-17', 4, 12),
           #  ('Action-18', 10, 14),
           #  ('Action-19', 24, 21),
           #  ('Action-20', 114, 18)]


def algoinvest_bruteforce(budget_max, actions_list, actions_selection=[]):
    # Si la liste des éléments n'est pas vide
    if actions_list:
        # alors nous appellons la fonction en passant en paramètre le budjet max, puis on ignore le 1er élément de la liste des actions,
        # la liste tampon action_selection reste inchangé !
        val1, lst_val1 = algoinvest_bruteforce(budget_max, actions_list[1:], actions_selection)

        # On affecte a une variable le 1er élément de la liste ( celui ignoré précédemment)
        val = actions_list[0]

        # on vérifie si le prix (cost) du 1er élément est inférieur ou égal au budget maxi ( ici 500 €)
        if val[1] <= budget_max:
            # alors nous appellons le fonction en otant au budget_max le prix (cost) du 1er élément
            # puis on ignore le 1er élément de la liste des actions
            # on met a jour la liste tampon avec le 1er élément
            val2, lst_val2 = algoinvest_bruteforce(budget_max - val[1], actions_list[1:], actions_selection + [val])

            # si le prix du 1er élément est inférieur
            if val1 < val2:
                return val2, lst_val2
        return val1, lst_val1
    # Si la liste des actions est vide
    else:
        # donne la somme maximum de profits + les éléments sélectionnés
        return f'{sum([i[2] for i in actions_selection])}', f'{actions_selection}'

print(algoinvest_bruteforce(500, actions))

