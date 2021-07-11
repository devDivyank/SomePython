def swap(a,b):
    return (b, a)

def shellSort(mylist):
    mylist = list(set(mylist))
    size = len(mylist)
    gap = size // 2
    while gap > 0:
        for i in range(gap, size):
            anchor = mylist[i]
            j = i
            while j >= gap and  mylist[j-gap] > anchor:
                mylist[j], mylist[j-gap] = swap(mylist[j], mylist[j-gap])
                j -= gap
        gap //= 2
    return mylist
