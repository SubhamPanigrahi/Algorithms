def insertion_sort(l):

    for x in range(len(l)):
        pos = x

        while pos > 0 and l[pos-1] > l[pos]:
            l[pos-1], l[pos] = l[pos], l[pos-1]
            pos -= 1


list1 = [9, 2, 6, 5, 1, 7]
insertion_sort(list1)
print(list1)
