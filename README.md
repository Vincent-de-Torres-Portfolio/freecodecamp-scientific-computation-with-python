# fcc-scientific-computation-w-python

This is a function for arranging arithmetic problems in a visually appealing way. It takes a list of problems and returns a string representing the arranged problems. The `show_answer` parameter can be used to include the answers in the output.

## Usage

To use this function, simply call `arithmetic_arranger` with a list of arithmetic problems as the first argument. The function will return a string representing the arranged problems.

```
from arithmetic import arithmetic_arranger

# Example usage
problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
arranged_problems = arithmetic_arranger(problems)

print(arranged_problems)

```

The above code will output:

```
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----

```

By default, the answers are not included in the output. To include the answers, set the `show_answer` parameter to `True`:

```
from arithmetic import arithmetic_arranger

# Example usage
problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
arranged_problems = arithmetic_arranger(problems, show_answer=True)

print(arranged_problems)

```

The above code will output:

```
  32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
 7301      3799      88      172

```

## Error handling

The function includes error handling for cases where the input is invalid. If there are more than 5 problems in the input list, the function will return an error message:

```
Error: Too many problems.

```

If the operator in a problem is not `+` or `-`, the function will return an error message:

```
Error: Operator must be '+' or '-'.

```

If either of the numbers in a problem contains non-digit characters, the function will return an error message:

```
Error: Numbers must only contain digits.

```

If either of the numbers in a problem is more than four digits long, the function will return an error message:

```
Error: Numbers cannot be more than four digits.

```

## Testing

To test the function, you can use a testing framework such as `unittest`. Here's an example of a test function for the `arithmetic_arranger` function using `unittest`:

```
import unittest
from my_project.arithmetic import arithmetic_arranger

class TestArithmeticArranger(unittest.TestCase):
    def test_arrangement(self):
        # Define input and expected output values
        problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
        expected_output = "  32      3801      45      123\\\\n+ 698    -    2    + 43    +  49\\\\n-----    ------    ----    -----\\\\n 7301      3799      88      172"

        # Call the function being tested and store the result
        result = arithmetic_arranger(problems, True)

        # Use assertions to check that the result matches the expected output
        self.assertEqual(result, expected_output)

        # Test the function with an empty list of problems
        result = arithmetic_arranger([], True)
        self.assertEqual(result, "")

        # Test the function with a list of problems that contains an invalid operator
        problems = ["32 $ 698"]
        expected_output = "Error: Operator must be '+' or '-'."
        result = arithmetic_arranger(problems, True)
        self.assertEqual(result, expected_output)

        # Test the function with a list of problems that contains a number with too many digits
        problems = ["12345 + 678"]
        expected_output = "Error: Numbers cannot be more than four digits."
        result = arithmetic_arranger(problems, True)
        self.assertEqual(result, expected_output)

```

This test function includes additional tests for edge cases, such as an empty list of problems and invalid operators or numbers with too many digits. By testing for these edge cases, you can ensure that your function is robust and can handle unexpected input.