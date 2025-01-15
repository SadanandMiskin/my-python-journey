arr = [0, 21, 13, 55, 12, 12, 54, 83, 11]

def sort(arr):
  for index in range(1, len(arr)):
    if arr[index] < arr[index - 1]:
      temp = arr[index -1]
      arr[index -1 ] = arr[index]
      arr[index] = temp
  return arr



print(sort(arr))