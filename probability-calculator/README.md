# __fcc5-probability-calculator__

## __Code Description__

The Probability Calculator project is a Python module that provides a class for a `Hat` object and a `experiment` function that can be used to conduct probability experiments. The `Hat` class allows for the creation of a "hat" containing a certain number of balls of different colors, and the drawing of a certain number of balls from the hat. The `experiment` function allows for the calculation of the probability of drawing a certain number of balls of different colors from the hat.

## Hat Class
---

### `__init__(self, **kwargs)`

The constructor method of the `Hat` class initializes a `Hat` object with a certain number of balls of different colors. The method takes a variable number of keyword arguments, where each keyword argument represents a color of ball and its corresponding value represents the number of balls of that color. For example, `Hat(red=3, blue=2)` creates a `Hat` object with 3 red balls and 2 blue balls.

### `draw(self, num_balls)`

The `draw` method of the `Hat` class is used to draw a certain number of balls from the hat. The method takes an integer `num_balls` that represents the number of balls to be drawn from the hat. The method returns a list of the drawn balls. If the number of balls to be drawn is greater than or equal to the number of balls in the hat, the method returns all the balls in the hat.

## Experiment Function
---

### `experiment(hat, expected_balls, num_balls_drawn, num_experiments)`

The `experiment` function is used to calculate the probability of drawing a certain number of balls of different colors from the hat. The function takes in a `Hat` object, a dictionary of `expected_balls` containing the number of balls of each color expected to be drawn, the `num_balls_drawn` that is the number of balls to be drawn from the hat, and the `num_experiments` that is the number of times to run the experiment.

The function creates a copy of the `Hat` object using the `copy` module to ensure that the original hat is not modified. It then draws a certain number of balls from the copied hat using the `draw` method of the `Hat` class. A dictionary is created to store the number of times each color is drawn. The function then checks if the number of balls of each color drawn matches the expected number of balls of each color. If the number of balls of each color matches the expected number, the function increments a counter `M`. The function then returns the probability of drawing the expected number of balls of different colors from the hat.

## Testing
---

The `unittest` module is used to test the functionality of the `Hat` class and `experiment` function.

The `test_draw` method of the `TestHat` class tests the `draw` method of the `Hat` class. The method creates a `Hat` object and draws a certain number of balls from the hat. The method then checks if the length of the list of drawn balls is equal to the number of balls drawn and if each ball drawn is in the original hat.

The `test_experiment` method of the `TestHat` class tests the `experiment` function. The method creates a `Hat` object and runs the `experiment` function with a certain number of expected balls, a certain number of balls to be drawn, and a certain number of experiments. The method then checks if the calculated probability is within a certain delta of the expected probability.

## Example
---

Here's an example of how to use the `Hat` class and `experiment` function:

```
from probability_calculator import Hat, experiment

hat = Hat(red=3, blue=2)
probability = experiment(hat=hat, expected_balls={"red": 2, "blue": 1}, num_balls_drawn=4, num_experiments=1000)
print(probability)

```

This code creates a `Hat` object with 3 red balls and 2 blue balls. It then runs the `experiment` function to calculate the probability of drawing 2 red balls and 1 blue ball when drawing 4 balls from the hat, based on 1000 experiments. The output is the calculated probability.

In summary, the Probability Calculator project provides a useful tool for conducting probability experiments, and the `unittest` module is useful for testing its functionality.

### License
---

This code is licensed under the MIT License.
