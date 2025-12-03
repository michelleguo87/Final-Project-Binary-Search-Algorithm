def binarySearch(nums, target): 
   """
      parameter: nums is a list of numbers in ascending order, target is an integer 
      output: index if target is found, -1 if not found 
   """ 
   #initalize index of upper and lower bounds 
   upper = len(nums)-1
   lower = 0 
   while upper > lower:  
      mid = (lower + upper)//2 
      if nums[mid] == target: 
         return mid
      elif nums[mid] < target: 
         lower = mid + 1 
      elif nums[mid] > target: 
         upper = mid - 1

   return -1        

#sample call 
nums = [2, 3, 5, 7, 9, 10] 
target = 12 
print(binarySearch(nums, target))
