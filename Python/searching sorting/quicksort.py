def quick_sort(l, min, max):

    if max-min <= 1:
        return ()
    sri = min+1

    for gri in range(min+1, max):

        if l[min] >= l[gri]:
            l[sri], l[gri] = l[gri], l[sri]
            sri += 1

    l[sri-1], l[min] = l[min], l[sri-1]
    quick_sort(l, min, sri-1)
    quick_sort(l, sri, max)


lst = [3, 9, 5, 2, 8]
print(lst)
quick_sort(lst, 0, 5)
print(lst)
