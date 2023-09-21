import time

def insertion_sort(data, drawData, timeTick):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        drawData(data, getColorArray(len(data), i, j, j+1))
        time.sleep(timeTick)

        while j >= 0 and data[j] > key:
            drawData(data, getColorArray(len(data), i, j, j+1))
            time.sleep(timeTick)

            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key

        drawData(data, getColorArray(len(data), i, j+1, j+1, True))
        time.sleep(timeTick)

def getColorArray(dataLen, currIdx, sortedIdx, compIdx, isSwapping = False):
    colorArray = []
    for i in range(dataLen):
        if i == currIdx:
            colorArray.append('yellow')
        elif i <= sortedIdx:
            colorArray.append('green')
        elif i == compIdx:
            colorArray.append('blue')
        else:
            colorArray.append('white')

        if isSwapping:
            if i == compIdx or i == compIdx + 1:
                colorArray[i] = 'red'

    return colorArray
