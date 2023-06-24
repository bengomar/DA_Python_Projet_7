
def sacADos_naif(capacite, elements):
    elements_tri = sorted(elements, key=lambda x: x[2])
    print(elements_tri)
    elements_selection = []
    poids_total = 0

    while elements_tri:
        ele = elements_tri.pop()
        #print(ele[1])
        if ele[1] + poids_total <= capacite:
            print(ele[1], '+', poids_total, '<=', capacite)
            elements_selection.append(ele)
            poids_total += ele[1]
            print('poids_total', poids_total)
        else:
            print(ele[1], '+', poids_total, 'est plus grand que', capacite)
    return sum([i[2] for i in elements_selection]), elements_selection

def sacADos_force_brute(capacite, elements, elements_selection = []):
    if elements:
        val1, lstVal1 = sacADos_force_brute(capacite, elements[1:], elements_selection)
        val = elements[0]
        if val[1] <= capacite:
            val2, lstVal2 = sacADos_force_brute(capacite - val[1], elements[1:], elements_selection + [val])
            if val1 < val2:
                return val2, lstVal2

        return val1, lstVal1
    else:
        return sum([i[2] for i in elements_selection]), elements_selection



ele = [('montre à gousset', 2, 6),
       ('Boule de bowling', 3, 10),
       ('Portrait de Germaine', 4, 12)]

#print('Algo naif', sacADos_naif(5, ele))

print('Algo force', sacADos_force_brute(5, ele))