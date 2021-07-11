def swap(a,b):
    return (b, a)
    
def selectionSort(mylist):
    for i in range(len(mylist)-1, 0, -1):
        for j in range(i):
            if mylist[j] > mylist[i]:
                mylist[j], mylist[i] = swap(mylist[j], mylist[i])
    return mylist
