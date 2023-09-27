Sure, here's a random Python method named 'calculate_average' which receives a list of numbers and calculates its average:

```python
def calculate_average(numbers):
    # Ensure the input is a list
    if type(numbers) != list:
        raise TypeError("`numbers` should be a list")

    # Ensure the list is not empty
    if len(numbers) == 0:
        raise ValueError("`numbers` should not be an empty list")

    # Ensure every element in the list is a number
    for num in numbers:
        if type(num) != int and type(num) != float:
            raise ValueError("All elements in `numbers` should be a number")

    # Calculate and return the average
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average
```

This method will raise an exception if the input is not a list, the list is empty, or if any of the list elements is not a number. It finishes by calculating and returning the average of the numbers.