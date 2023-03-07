nums = [4,5,2,8,9]
target = 10


class Solution:
  
  def __init__(self):
    self.nums = []
    self.target = 0
    
  def twoSum(self, numerot, tavoite):
    self.nums = numerot
    self.target = tavoite
    for x in numerot:
      for y in numerot:
        if numerot.index(y) != numerot.index(x):
          if x + y == tavoite:  
            return [numerot.index(x), numerot.index(y)]
            #print(numerot.index(x), numerot.index(y))
            #print(x, y)

      
ratkaisu = Solution()

lista = ratkaisu.twoSum(nums, target)

print(lista)