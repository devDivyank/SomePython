def swap(a,b):
    return (b, a)
  
def bubbleSort(mylist):
    for i in range(1, len(mylist)):
        for j in range(len(mylist)-i):
            if mylist[j] > mylist[j+1]:
                mylist[j+1], mylist[j] = swap(mylist[j+1], mylist[j])
    return mylist
