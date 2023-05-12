# __fcc2-time-calculator__

## __Code Details__
---

This python function takes a starting time and a duration as inputs and returns the time it will be after the given duration has passed. The function can also optionally take a day of the week and will return the day of the week along with the time. For example, if we start at `3:00 PM` and add a duration of `3:10`, we get the result `6:10 PM`.

The function works by first taking the starting time and splitting it into its components of hours, minutes, and meridian (AM/PM). Then it takes the duration and also splits it into hours and minutes. It converts the starting time into 24-hour format and then adds the duration to it. The result is then converted back to 12-hour format and returned as a string.

If a day of the week is given, the function will also determine the day of the week of the result. If the result is the next day, the output will include the text `" (next day)"`. If the result is more than one day later, the output will include the text `" (n days later)"`, where `n` is the number of days later.

## __Usage__
---

### __Inputs__

The `add_time()` function takes three inputs:

- `start` - a string representing the starting time in the format `"hh:mm AM/PM"`. The hours are in the range of `1` to `12` and the minutes are in the range of `00` to `59`. The meridian can be either `"AM"` or `"PM"`.
- `duration` - a string representing the duration of time in the format `"hh:mm"`. The hours are in the range of `00` to `23` and the minutes are in the range of `00` to `59`.
- `day` - an optional string representing the starting day of the week, formatted as a capitalized string, e.g. `"Monday"`

### __Outputs__

The function returns a string representing the time after the given duration has passed, formatted as follows:

- If a day of the week is given, the output will be in the format `"hh:mm AM/PM, Day of Week"`
- If no day of the week is given, the output will be in the format `"hh:mm AM/PM"`

## __Demo__
---

```
add_time("3:00 PM", "3:10")

```

This will return the string `"6:10 PM"`.

```
add_time("11:30 AM", "2:32", "Monday")

```

This will return the string `"2:02 PM, Monday"`.

```
add_time("11:43 AM", "00:20")

```

This will return the string `"12:03 PM"`.

```
add_time("10:10 PM", "3:30")

```

This will return the string `"1:40 AM (next day)"`.

```
add_time("11:43 PM", "24:20", "tueSday")

```

This will return the string `"12:03 AM, Thursday (2 days later)"`.

```
add_time("6:30 PM", "205:12")

```

This will return the string `"7:42 AM (9 days later)"`.

## Unit Test

```
def test_add_time():
    assert add_time("3:00 PM", "3:10") == "6:10 PM"
    assert add_time("11:30 AM", "2:32", "Monday") == "2:02 PM, Monday"
    assert add_time("11:43 AM", "00:20") == "12:03 PM"
    assert add_time("10:10 PM", "3:30") == "1:40 AM (next day)"
    assert add_time("11:43 PM", "24:20", "tueSday") == "12:03 AM, Thursday (2 days later)"
    assert add_time("6:30 PM", "205:12") == "7:42 AM (9 days later)"
    print("All test cases pass")

```
---

```
add_time("11:30 AM", "2:32", "Monday")

```

This will return the string `"2:02 PM, Monday"`.

```
add_time("11:43 PM", "24:20", "tueSday")

```

This will return the string `"12:03 AM, Thursday (2 days later)"`.
---
## __Notes__
---

The `add_time()` function assumes that the input strings will always be correctly formatted. It also assumes that the duration will be less than 24 hours, and that the result will always be within a week of the starting time.

This function is useful for calculating the time after a certain duration has passed, for example, when scheduling appointments or events. It can also be used to calculate the duration between two times by subtracting the starting time from the result.


### License
---

This code is licensed under the MIT License.
