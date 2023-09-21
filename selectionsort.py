import time

def selection_sort(data, drawData, timeTick):
    for i in range(len(data)):
        min_idx = i

        drawData(data, getColorArray(len(data), i, min_idx))
        time.sleep(timeTick)

        for j in range(i+1, len(data)):
            if data[j] < data[min_idx]:
                min_idx = j

            drawData(data, getColorArray(len(data), i, min_idx))
            time.sleep(timeTick)

        # Swap the minimum element with the current element
        data[i], data[min_idx] = data[min_idx], data[i]

        drawData(data, getColorArray(len(data), i, min_idx, True))
        time.sleep(timeTick)


def getColorArray(dataLen, currIdx, minIdx, isSwaping=False):
    colorArray = []
    for i in range(dataLen):
        # Base coloring
        colorArray.append('white')

        if i == currIdx:
            colorArray[i] = 'yellow'
        elif i == minIdx:
            colorArray[i] = 'red'

        if isSwaping:
            if i == currIdx or i == minIdx:
                colorArray[i] = 'green'

    return colorArray
