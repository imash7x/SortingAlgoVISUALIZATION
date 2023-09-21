import time

def counting_sort(data, drawData, timeTick):
    # Find the maximum element in the list
    max_value = max(data)

    # Create a count list to store the count of each element
    count = [0] * (max_value + 1)

    # Count the occurrences of each element
    for num in data:
        count[num] += 1

    # Calculate the cumulative sum of the count list
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Create a sorted list to store the sorted elements
    sorted_data = [0] * len(data)

    # Visualization of the counting step
    for i in range(len(count)):
        drawData(data, getColorArray(len(data), i, count[i] - 1, i))
        time.sleep(timeTick)

    # Traverse the original list in reverse order
    for i in range(len(data) - 1, -1, -1):
        # Get the value and index of the current element
        value = data[i]
        index = count[value] - 1

        # Place the element at its correct position in the sorted list
        sorted_data[index] = value

        # Decrement the count for the current element
        count[value] -= 1

        # Visualization of placing the value in sorted form
        drawData(sorted_data, getColorArray(len(sorted_data), i, index, value))
        time.sleep(timeTick)

    # Copy the sorted list back to the original list
    for i in range(len(data)):
        data[i] = sorted_data[i]

    # Visualization of the final sorted list
    drawData(data, ['green'] * len(data))


def getColorArray(dataLen, currIndex, sortedIndex, value):
    colorArray = []
    for i in range(dataLen):
        # Base coloring
        colorArray.append('white')

        # Color the current element being considered
        if i == currIndex:
            colorArray[i] = 'blue'

        # Color the sorted elements
        if i <= sortedIndex:
            colorArray[i] = 'green'

        # Color the element being placed at its correct position
        if i == sortedIndex + 1:
            colorArray[i] = 'yellow'

        # Highlight the value being considered
        if i == currIndex or i == sortedIndex + 1:
            colorArray[i] = 'red'

    return colorArray

