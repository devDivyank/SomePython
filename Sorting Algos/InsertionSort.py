def swap(a,b):
    return (b, a)

def insertionSort(mylist):
    for i in range(len(mylist)):
        currentVal = mylist[i]
        currentPos = i
        while currentPos > 0 and mylist[currentPos-1] > currentVal:
            mylist[currentPos] = mylist[currentPos-1]
            currentPos -=1
        mylist[currentPos] = currentVal
    return mylist
