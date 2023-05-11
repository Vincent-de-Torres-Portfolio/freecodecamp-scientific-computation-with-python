def arithmetic_arranger(problems, show_answer=False):

  if len(problems) > 5:
    return Error: Too many problems.

  first_line = 
  second_line = 
  third_line = 
  fourth_line = 

  for problem in problems:
    problem_split = problem.split()

    first_number = problem_split[0]
    operator = problem_split[1]
    second_number = problem_split[2]

    if operator not in +-:
      return Error: Operator must be + or -.

    if not first_number.isdigit() or not second_number.isdigit():
      return Error: Numbers must only contain digits.

    if len(first_number) > 4 or len(second_number) > 4:
      return Error: Numbers cannot be more than four digits.

    if operator == +:
      answer = int(first_number) + int(second_number)
    else:
      answer = int(first_number) - int(second_number)

    length = max(len(first_number), len(second_number)) + 2

    first_line += first_number.rjust(length)
    second_line += operator + second_number.rjust(length - 1)
    third_line += - * length
    fourth_line += str(answer).rjust(length)

    if problem != problems[-1]:
      first_line +=  
      second_line +=  
      third_line +=  
      fourth_line +=  

  if show_answer:
    return first_line + n + second_line + n + third_line + n + fourth_line
  else:
    return first_line + n + second_line + n + third_line
