def selectoionSort(nums):
  l = len(nums)
  for i in range(l):
    min = nums[i]
    for j in range(i+1, l):
      if nums[j]<min:
        min = nums[j]
        nums[i], nums[j] = nums[j], nums[i]
  return nums

print(selectoionSort([5,2,1,3,0,3,4,2]))
