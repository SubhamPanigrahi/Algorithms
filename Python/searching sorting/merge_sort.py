def merge(a, b):
    (c, m, n) = ([], len(a), len(b))
    i, j = 0, 0

    while i+j < m+n:
        if i == m:
            c.append(b[j])
            j += 1
        elif j == n:
            c.append(a[i])
            i += 1
        elif a[i] <= b[j]:
            c.append(a[i])
            i += 1
        elif a[i] > b[j]:
            c.append(b[j])
            j += 1
    return c


def merge_sort(l, mini, maxi):
    mid = (mini + maxi) // 2
    if maxi-mini <= 1:
        return l[mini:maxi]
    else:
        x = merge_sort(l, mini, mid)
        y = merge_sort(l, mid, maxi)
        return merge(x, y)


lst = [9, 34, 1, 12, 7]
print(lst)
print(merge_sort(lst, 0, 5))
