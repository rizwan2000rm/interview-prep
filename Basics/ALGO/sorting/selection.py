def getSmallestElement(array):
  smallestElement = array[0]
  smallestIndex = 0
  for i in range(1, len(array)):
    if array[i] < smallestElement:
      smallestElement = array[i]
      smallestIndex = i
  return smallestIndex

def selectionSort(array):
  newArray = []
  for i in range(len(array)):
    smallest = getSmallestElement(array)
    newArray.append(array.pop(smallest))
  return newArray

print(selectionSort([35,12,40,-41,120,-145]))