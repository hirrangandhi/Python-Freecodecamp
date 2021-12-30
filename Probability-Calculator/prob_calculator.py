import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self,**kwargs):
    self.hatList = []
    self.contents = []
    for key,value in kwargs.items():
      self.hatList.append([key,value])
      for v in range(value):
        self.contents.append(key)
    #print(self.hatList)
    #print(self.contents)
  
  def draw(self,numToDraw):
    drawn = []
    if numToDraw > len(self.contents):
      return self.contents
    for i in range(numToDraw):
      randIdx = random.randrange(len(self.contents))
      drawn.append(self.contents[randIdx])
      self.contents.pop(randIdx)
    return drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  count = 0
  for i in range(num_experiments):
    hatObj = copy.deepcopy(hat)
    drawn = hatObj.draw(num_balls_drawn)
    #print(drawn)
        
    match = True
    for key in expected_balls.keys():
      if drawn.count(key) < expected_balls[key]:
        match = False
        break
    if match == True:
      count += 1
  
  probability = count / num_experiments
  #print(count, probability)

  return probability