def mergesort(list):
    if len(list) < 2:
        return list

    middle = len(list) // 2
    left = mergesort(list[:middle])
    right = mergesort(list[middle:])
    return merge(list, left, right)


def merge(datalist, left, right):
    left.append(99999999999999999999999999999999999999999)  # dummy variable
    right.append(99999999999999999999999999999999999999999)  # dummy variable
    i, j = 0, 0
    for k in range(len(datalist)):
        if left[i] <= right[j]:
            datalist[k] = left[i]
            i += 1
        else:
            datalist[k] = right[j]
            j += 1
    return datalist


list1 = [-3,10,99,33,12,11,12,14,25,1000,-666,0,1,13,14,15,116,19,14,13,12,22]
print(list1)

list2 = mergesort(list1)

print(list2)