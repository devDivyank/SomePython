def swap(a,b):
    return (b, a)
    
def quickSort(mylist):
    if len(mylist) <= 1:
        return mylist
    else:
        pivot = mylist.pop()

    lower = []
    greater = []

    for val in mylist:
        if val <= pivot:
            lower.append(val)
        else:
            greater.append(val)
    return quickSort(lower) + [pivot] + quickSort(greater)
