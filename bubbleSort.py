def bubbleSort(nums):
  length = len(nums)

  for i in range(length):
    # Initialize a flag to track if any swaps are made in this pass
    swapped = False

    # Iterate through the unsorted part of the list
    for j in range(0, length - i - 1):
      # Compare adjacent elements and swap if needed
      if nums[j] > nums[j + 1]:
        nums[j], nums[j + 1] = nums[j + 1], nums[j]
        swapped = True

    # If no swaps were made in this pass, the list is already sorted
    if not swapped:
      # Without the swapped check, Bubble Sort would always go through the entire inner loop
      # for each iteration of the outer loop, even if the list is already sorted.
      # This would result in unnecessary comparisons and swaps.
      break

  print("Sorted Array:", nums)


# Example usage
bubbleSort([5, 2, 1, 3, 0])
