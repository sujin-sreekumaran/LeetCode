
def myFunc(nums,target):
  """
  A function that takes in a list of numbers `nums` and a target number `target`. 
  It iterates through the list and checks if any two numbers in the list add up to the target. 
  If a pair is found, it sets `result` to True, stores the indices of the pair in `solution`, 
  and returns `solution`. If no pair is found, it returns None.
  """
  
  result = False
  solution = []
  for i in range(len(nums)):
   if(result==False):
    for j in range(i+1):
     if nums[i]+nums[j]==target and result==False:
      result = True
      print('Inside >>>',j,i)
      solution = [j,i]
      break
   elif(result==True):
    return solution
  else:
   return
  
  



result = myFunc([2,4,4,3,6],7)
print("Result >>>",result)
