import copy
import random
# Consider using the modules imported above.


class Hat:

  def __init__(self, **kwargs):
    self.contents = []
    for key, value in kwargs.items():
      for i in range(value):
        self.contents.append(key)

  def draw(self, num_balls):
    if num_balls >= len(self.contents):
      return self.contents
    else:
      drawn_balls = []
      for i in range(num_balls):
        drawn_balls.append(
          self.contents.pop(random.randrange(len(self.contents))))
      return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  M = 0
  for i in range(num_experiments):
    hat_copy = copy.deepcopy(hat)
    drawn_balls = hat_copy.draw(num_balls_drawn)
    drawn_balls_dict = {}
    for ball in drawn_balls:
      if ball in drawn_balls_dict:
        drawn_balls_dict[ball] += 1
      else:
        drawn_balls_dict[ball] = 1
    success = True
    for key, value in expected_balls.items():
      if key not in drawn_balls_dict or drawn_balls_dict[key] < value:
        success = False
        break
    if success:
      M += 1
  return M / num_experiments

