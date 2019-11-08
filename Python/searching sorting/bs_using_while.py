def bs(l, v, min, max):

    while max-min:
        mid = (min+max)//2

        if l[mid] < v:
            min = mid+1

        elif l[mid] > v:
            max = mid-1

        elif l[mid] == v:
            return mid
    return -1


lst = [2, 5, 6, 9, 10]
print(lst)
print(bs(lst, 5, 0, 4))
