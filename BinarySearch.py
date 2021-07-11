def binarySearch(numList, targetNum, startIndex, endIndex):
    if startIndex > endIndex:
        return False

    midIndex = (startIndex + endIndex) // 2
    if midIndex >= len(numList) or midIndex <= 0:
        return False
    midNumber = numList[midIndex]
    if midNumber == targetNum:
        return True

    if midNumber > targetNum:
        endIndex = midIndex - 1
    else:
        startIndex = midIndex + 1

    return binarySearch(numList, targetNum, startIndex, endIndex)
