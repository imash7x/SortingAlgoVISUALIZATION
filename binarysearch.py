import time
def binary_search(data, target, drawData, timeTick):
    low = 0
    high = len(data) - 1
    found = False

    while low <= high and not found:
        mid = (low + high) // 2

        # Visualization of the current state
        drawData(data, getColorArray(len(data), low, high, mid, target))

        # Delay for visualization
        time.sleep(timeTick)

        if data[mid] == target:
            found = True
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    # Visualization of the final state
    drawData(data, getColorArray(len(data), low, high, mid, target, found))
    time.sleep(timeTick*5)

    return found

def getColorArray(dataLen, low, high, mid, target, found=False):
    colorArray = []
    for i in range(dataLen):
        if i >= low and i <= high:
            colorArray.append('gray')
        else:
            colorArray.append('white')

        if i == mid:
            colorArray[i] = 'yellow'

        if i == target:
            colorArray[i] = 'red'

        if found and i == mid:
            colorArray[i] = 'green'

    return colorArray

