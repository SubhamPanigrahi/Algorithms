def binary_search(l, v, min, max):
    if max-min == 0:
        return -1
    mid = (max+min)//2
    if l[mid] == v:
        return mid
    elif l[mid] < v:
        return binary_search(l, v, mid+1, max)
    elif l[mid] > v:
        return binary_search(l, v, min, mid)


lst = [1, 3, 5, 7, 9]
print(lst)
print(binary_search(lst, 7, 0, 5))
