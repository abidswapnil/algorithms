def bubbleSort(nums):
  l = len(nums)
  for i in range(l):
    swapped = False
    for j in range(0, l-i-1):
      if nums[j] > nums[j + 1]:
        nums[j], nums[j+1] = nums[j+1], nums[j]
        swapped = True
    if not swapped:
      break
  print(nums)

bubbleSort([5,2,1,3,0])