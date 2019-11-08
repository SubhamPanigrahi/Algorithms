

def selection_sort(l):

    for start in range(len(l)):
        min_pos = start

        for i in range(start, len(l)):

            if l[i] < l[min_pos]:
                min_pos = i

        l[start], l[min_pos] = l[min_pos], l[start]


pl = [9, 4, 7, 3]

selection_sort(pl)
print(pl)
