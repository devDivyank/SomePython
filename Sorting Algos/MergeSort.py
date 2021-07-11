def swap(a,b):
    return (b, a)

def mergeSort(mylist):
    if len(mylist) <= 1 :
        return
    mid = len(mylist) // 2
    firstHalf = mylist[:mid]
    lastHalf = mylist[mid:]
    mergeSort(firstHalf)
    mergeSort(lastHalf)

    i = j = k = 0
    while i < len(firstHalf) and j < len(lastHalf):
        if firstHalf[i] < lastHalf[j]:
            mylist[k] = firstHalf[i]
            i += 1
        else:
            mylist[k] = lastHalf[j]
            j += 1
        k += 1
    while i < len(firstHalf):
        mylist[k] = firstHalf[i]
        k += 1
        i += 1
    while j < len(lastHalf):
        mylist[k] = lastHalf[j]
        k += 1
        j += 1
