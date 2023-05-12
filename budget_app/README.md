# __fcc3-budget-app__
## __Code Details__
This Python code defines two classes: `Category` and `create_spend_chart`.

---



### __`Category` Class__
---

The `Category` class represents a budget category. It has the following 
methods:

- `deposit(amount, description)`: adds an amount to the category balance 
with an optional description.
- `withdraw(amount, description)`: subtracts an amount from the category 
balance with an optional description. Returns False if there are 
insufficient funds.
- `get_balance()`: returns the current balance of the category.
- `transfer(amount, category)`: transfers an amount from this category to 
another category.
- `check_funds(amount)`: returns True if there are sufficient funds for an 
amount, False otherwise.
- `__str__()`: returns a string representation of the category ledger.



### __`create_spend_chart` Function__

----

The `create_spend_chart` function takes a list of `Category` objects and 
returns a string representation of a bar chart showing the percentage 
spent by category.

### __Usage__
----


To use the `Category` class and `create_spend_chart` function, you can 
import the module and create instances of the `Category` class. For 
example:

```
from budget import Category, create_spend_chart

food_category = Category("Food")
food_category.deposit(1000, "initial deposit")
food_category.withdraw(10.15, "groceries")

clothing_category = Category("Clothing")
clothing_category.deposit(500, "initial deposit")
clothing_category.transfer(100, food_category)

print(food_category)
print(clothing_category)
print(create_spend_chart([food_category, clothing_category]))

```

Output:

```
*************Food*************
initial deposit              1000.00
groceries                     -10.15
Total: 989.85
***********Clothing***********
initial deposit               500.00
Transfer to Food             -100.00
Total: 400.00
Percentage spent by category
100|
 90|
 80|
 70|
 60|
 50|
 40|
 30|
 20| o
 10| o
  0| o
    ----------
     F  C
     o  l
     o  o
     d  t
        h
        i
        n
        g

```

### License
---

This code is licensed under the MIT License.
